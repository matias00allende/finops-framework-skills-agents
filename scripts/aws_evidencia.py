"""Recolector de evidencia FinOps en AWS (SOLO LECTURA, sin escrituras).

Uso: python -I aws_evidencia.py --profile <perfil> --tag-key <clave_tag> --months 3 --out evidencia.json

Entrega metricas objetivas que sirven de evidencia para criterios Crawl/Walk/Run:
  - allocation: % del gasto sin la clave de tag (Cost Explorer, group by TAG) y si la clave esta activada
  - rate_optimization: cobertura y utilizacion de Savings Plans; cobertura de RI por servicio
  - anomaly_management: monitores, suscripciones, frecuencia, umbral y tipo de suscriptor
  - budgeting: presupuestos, notificaciones y acciones
  - data_ingestion: Data Exports (tipo de tabla: CUR 2.0 / FOCUS) y CUR legado
  - usage_optimization: recomendaciones de Compute Optimizer (si esta habilitado)
Cada bloque falla de forma aislada: un error no aborta el resto y queda en "errores".
No imprime ni guarda credenciales.

Permisos IAM minimos de solo lectura (nombres segun la documentacion oficial de AWS):
  ce:GetCostAndUsage, ce:ListCostAllocationTags, ce:GetSavingsPlansCoverage, ce:GetSavingsPlansUtilization,
  ce:GetReservationCoverage, ce:GetAnomalyMonitors, ce:GetAnomalySubscriptions,
  budgets:ViewBudget (+ aws-portal:ViewBilling segun el modelo de permisos de la cuenta),
  bcm-data-exports:ListExports, bcm-data-exports:GetExport, cur:DescribeReportDefinitions,
  compute-optimizer:GetEnrollmentStatus, compute-optimizer:GetRecommendationSummaries.
budgets:ViewBudget cubre DescribeBudgets, DescribeNotificationsForBudget y DescribeBudgetActionsForBudget.
sts:GetCallerIdentity no requiere permiso explicito.
NO usar ce:* (incluye acciones de escritura como crear o borrar monitores).
El JSON de salida contiene el ID de cuenta y nombres de presupuestos y monitores: tratarlo como dato sensible y guardarlo fuera del repositorio.
Nota de costo: cada llamada a Cost Explorer se factura (aprox. USD 0,01); el script hace menos de 15 por corrida.
"""
import argparse
import datetime as dt
import json
import sys

import boto3

SERVICIOS_RI = ["Amazon Elastic Compute Cloud - Compute", "Amazon Relational Database Service",
                "Amazon ElastiCache", "Amazon Redshift", "Amazon OpenSearch Service"]


def pct(v):
    return round(float(v), 1)


def rango(meses):
    fin = dt.date.today().replace(day=1)
    ini = (fin - dt.timedelta(days=30 * meses)).replace(day=1)
    return ini.isoformat(), fin.isoformat()


def seguro(res, clave, fn):
    try:
        res[clave] = fn()
    except Exception as e:  # un bloque fallido no aborta el resto
        res.setdefault("errores", {})[clave] = f"{type(e).__name__}: {str(e)[:200]}"


def paginar(fn, token_in="NextPageToken", token_out="NextPageToken", **kw):
    """Itera paginas de una operacion que usa token en la respuesta (Cost Explorer)."""
    while True:
        r = fn(**kw)
        yield r
        t = r.get(token_out)
        if not t:
            return
        kw[token_in] = t


def tag_activado(ce, tag_key):
    """Verifica si la clave esta activada como cost allocation tag; sin eso todo cae en 'sin tag'."""
    estados = []
    for r in paginar(ce.list_cost_allocation_tags, token_in="NextToken", token_out="NextToken",
                     TagKeys=[tag_key], MaxResults=100):
        estados += [{"clave": t["TagKey"], "estado": t["Status"], "tipo": t["Type"]}
                    for t in r.get("CostAllocationTags", [])]
    return estados


def tag_coverage(ce, tag_key, ini, fin):
    # UnblendedCost incluye creditos y reembolsos; es una medida de cobertura, no de factura.
    meses = {}
    for r in paginar(ce.get_cost_and_usage, TimePeriod={"Start": ini, "End": fin}, Granularity="MONTHLY",
                     Metrics=["UnblendedCost"], GroupBy=[{"Type": "TAG", "Key": tag_key}]):
        for m in r["ResultsByTime"]:
            acc = meses.setdefault(m["TimePeriod"]["Start"], [0.0, 0.0])
            for g in m["Groups"]:
                v = float(g["Metrics"]["UnblendedCost"]["Amount"])
                acc[0] += v
                if g["Keys"][0] == f"{tag_key}$":  # clave sin valor = sin tag
                    acc[1] += v
    out = []
    for mes, (total, sin) in sorted(meses.items()):
        out.append({"mes": mes, "total_usd": round(total, 2), "sin_tag_usd": round(sin, 2),
                    "pct_asignado": round(100 * (1 - sin / total), 1) if total else None})
    activado = []
    try:
        activado = tag_activado(ce, tag_key)
    except Exception as e:
        activado = f"no verificable: {type(e).__name__}"
    return {"tag_key": tag_key, "activacion": activado, "meses": out}


def cobertura(ce, ini, fin):
    out = {}
    tp = {"Start": ini, "End": fin}
    try:
        cob, uti = [], []
        for r in paginar(ce.get_savings_plans_coverage, TimePeriod=tp, Granularity="MONTHLY"):
            cob += [{"mes": x["TimePeriod"]["Start"], "pct": pct(x["Coverage"]["CoveragePercentage"])}
                    for x in r["SavingsPlansCoverages"]]
        for r in paginar(ce.get_savings_plans_utilization, TimePeriod=tp, Granularity="MONTHLY"):
            uti += [{"mes": x["TimePeriod"]["Start"], "pct": pct(x["Utilization"]["UtilizationPercentage"])}
                    for x in r["SavingsPlansUtilizationsByTime"]]
        out["savings_plans_cobertura_pct"], out["savings_plans_utilizacion_pct"] = cob, uti
    except Exception as e:
        out["savings_plans_error"] = f"{type(e).__name__}: {str(e)[:120]}"
    ri = {}
    for svc in SERVICIOS_RI:  # sin filtro SERVICE la API mide solo EC2
        try:
            serie = []
            for r in paginar(ce.get_reservation_coverage, TimePeriod=tp, Granularity="MONTHLY",
                             Filter={"Dimensions": {"Key": "SERVICE", "Values": [svc]}}):
                serie += [{"mes": x["TimePeriod"]["Start"],
                           "pct": pct(x["Total"]["CoverageHours"]["CoverageHoursPercentage"])}
                          for x in r["CoveragesByTime"]]
            ri[svc] = serie
        except Exception as e:
            ri[svc] = f"{type(e).__name__}"
    out["ri_cobertura_por_servicio_pct"] = ri
    return out


def anomalias(ce):
    mons = [m for r in paginar(ce.get_anomaly_monitors) for m in r["AnomalyMonitors"]]
    subs = [s for r in paginar(ce.get_anomaly_subscriptions) for s in r["AnomalySubscriptions"]]
    return {"monitores": [{"nombre": m["MonitorName"], "tipo": m["MonitorType"]} for m in mons],
            "suscripciones": [{"nombre": s["SubscriptionName"], "frecuencia": s["Frequency"],
                               "umbral": s.get("ThresholdExpression") or s.get("Threshold"),
                               "suscriptores": [x.get("Type") for x in s.get("Subscribers", [])]}
                              for s in subs]}


def presupuestos(session, cuenta):
    b = session.client("budgets", region_name="us-east-1")
    items = []
    for page in b.get_paginator("describe_budgets").paginate(AccountId=cuenta):
        items += page.get("Budgets", [])
    out = []
    for x in items:
        try:
            n = len(b.describe_notifications_for_budget(AccountId=cuenta, BudgetName=x["BudgetName"])["Notifications"])
        except Exception:
            n = None
        try:
            acc = len(b.describe_budget_actions_for_budget(AccountId=cuenta, BudgetName=x["BudgetName"])["Actions"])
        except Exception:
            acc = None
        out.append({"nombre": x["BudgetName"], "tipo": x["BudgetType"], "periodo": x["TimeUnit"],
                    "limite": x.get("BudgetLimit", {}).get("Amount"), "notificaciones": n, "acciones": acc})
    return out


def exports(session):
    out = {}
    try:
        cli = session.client("bcm-data-exports", region_name="us-east-1")
        lista = []
        for page in cli.get_paginator("list_exports").paginate():
            lista += page["Exports"]
        det = []
        for e in lista:
            item = {"nombre": e["ExportName"], "estado": e.get("ExportStatus", {}).get("StatusCode")}
            try:  # GetExport distingue CUR 2.0 de FOCUS por el nombre de la tabla
                g = cli.get_export(ExportArn=e["ExportArn"])["Export"]
                item["tabla"] = g.get("DataQuery", {}).get("QueryStatement", "")[:200]
            except Exception:
                pass
            det.append(item)
        out["data_exports"] = det
    except Exception as e:
        out["data_exports_error"] = type(e).__name__
    try:
        r = session.client("cur", region_name="us-east-1").get_paginator("describe_report_definitions")
        defs = []
        for page in r.paginate():
            defs += page["ReportDefinitions"]
        out["cur_legado"] = [{"nombre": x["ReportName"], "formato": x["Format"], "tiempo": x["TimeUnit"]} for x in defs]
    except Exception as e:
        out["cur_error"] = type(e).__name__
    return out


def compute_optimizer(session):
    co = session.client("compute-optimizer", region_name="us-east-1")
    st = co.get_enrollment_status()["status"]
    res = {"estado": st}
    if st == "Active":
        s = []
        for page in co.get_paginator("get_recommendation_summaries").paginate():
            s += page["recommendationSummaries"]
        res["resumen"] = [{"tipo": x["recommendationResourceType"], "resumen": x.get("summaries", [])} for x in s]
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--profile", default=None)
    ap.add_argument("--tag-key", required=True, help="clave del tag de asignacion de costos de su organizacion")
    ap.add_argument("--months", type=int, default=3)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    session = boto3.Session(profile_name=a.profile)
    cuenta = session.client("sts").get_caller_identity()["Account"]
    ce = session.client("ce", region_name="us-east-1")
    ini, fin = rango(a.months)
    res = {"cuenta": cuenta, "periodo": {"inicio": ini, "fin": fin}, "solo_lectura": True}
    seguro(res, "allocation_tag_coverage", lambda: tag_coverage(ce, a.tag_key, ini, fin))
    seguro(res, "rate_optimization", lambda: cobertura(ce, ini, fin))
    seguro(res, "anomaly_management", lambda: anomalias(ce))
    seguro(res, "budgeting", lambda: presupuestos(session, cuenta))
    seguro(res, "data_ingestion", lambda: exports(session))
    seguro(res, "usage_optimization_compute_optimizer", lambda: compute_optimizer(session))
    with open(a.out, "w", encoding="utf-8") as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    print(f"Evidencia: {a.out} (errores: {list(res.get('errores', {}))})")


if __name__ == "__main__":
    sys.exit(main())
