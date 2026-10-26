"""Pruebas del mapeador con evidencia sintetica con la forma que emiten los recolectores."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RAIZ))
import mapear_evidencia as m  # noqa: E402

AWS = {"cuenta": "1", "allocation_tag_coverage": {"meses": [{"pct_asignado": 21.2}, {"pct_asignado": 26.6}]},
       "rate_optimization": {"savings_plans_cobertura_pct": [{"mes": "a", "pct": 73.5}]},
       "anomaly_management": {"monitores": [{"nombre": "m", "tipo": "DIMENSIONAL"}],
                              "suscripciones": [{"umbral": {"x": 1}, "suscriptores": ["EMAIL"]}]},
       "budgeting": [{"tipo": "COST", "notificaciones": 3, "acciones": 0}],
       "data_ingestion": {"data_exports": [], "cur_legado": [{"nombre": "c"}]}}
GCP = {"cuenta_facturacion": "x", "allocation": {"meses": [{"pct_asignado": 95.0}]},
       "budgeting": {"total": 2, "con_pubsub": 1, "presupuestos": []},
       "data_ingestion": {"exports": {"standard": ["t1"], "focus": ["f1"], "detailed": []}}}
AZ = {"scope": "subscriptions/1", "allocation_tag_coverage": {"meses": [{"pct_asignado": 60.0}]},
      "budgeting": {"total": 1, "presupuestos": [{"notificaciones": [{"action_groups": 1}]}]},
      "data_ingestion": {"total": 2, "focus": 0}}


class TestNormalizar(unittest.TestCase):
    def test_nubes(self):
        self.assertEqual(m.normalizar(AWS)["nube"], "aws")
        self.assertEqual(m.normalizar(GCP)["nube"], "gcp")
        self.assertEqual(m.normalizar(AZ)["nube"], "azure")

    def test_aws(self):
        n = m.normalizar(AWS)
        self.assertEqual(n["tag_min"], 21.2)
        self.assertEqual(n["sp_cob"], 73.5)
        self.assertEqual(n["presupuestos"]["notificaciones"], 3)
        self.assertEqual(n["ingestion"], {"total": 1, "focus": 0})

    def test_gcp(self):
        n = m.normalizar(GCP)
        self.assertEqual(n["tag_min"], 95.0)
        self.assertEqual(n["presupuestos"]["integraciones"], 1)
        self.assertEqual(n["ingestion"], {"total": 2, "focus": 1})

    def test_azure(self):
        n = m.normalizar(AZ)
        self.assertEqual(n["presupuestos"]["integraciones"], 1)
        self.assertEqual(n["ingestion"], {"total": 2, "focus": 0})


class TestReglas(unittest.TestCase):
    def test_alloc(self):
        self.assertEqual(m.r_alloc_mayoria(m.normalizar(AWS))[0], "no")
        self.assertEqual(m.r_alloc_alta(m.normalizar(GCP))[0], "cumple")
        self.assertEqual(m.r_alloc_alta(m.normalizar(AZ))[0], "no")

    def test_budget(self):
        self.assertEqual(m.r_budget_acciones(m.normalizar(AWS))[0], "parcial")
        self.assertEqual(m.r_budget_acciones(m.normalizar(GCP))[0], "parcial")

    def test_sin_datos_devuelve_none(self):
        n = m.normalizar({"cuenta": "1"})
        self.assertIsNone(m.r_alloc_mayoria(n))
        self.assertIsNone(m.r_ing_resumen(n))

    def test_otras_nubes_no_evaluan_alertas_rate(self):
        self.assertIsNone(m.r_rate_alerta_util(m.normalizar(GCP)))


class TestIntegracion(unittest.TestCase):
    @unittest.skipUnless((RAIZ.parent / "kb" / "capabilities.json").exists(),
                         "Requiere kb/capabilities.json: generarlo con scrape_raw.py y build_kb.py")
    def test_cli(self):
        with tempfile.TemporaryDirectory() as d:
            q, e = Path(d) / "q.json", Path(d) / "e.json"
            subprocess.run([sys.executable, "-I", str(RAIZ / "finops_assess.py"), "init", "--scope", "t", "--out",
                            str(q), "--caps", "allocation,data-ingestion"], check=True, capture_output=True)
            e.write_text(json.dumps(GCP), encoding="utf-8")
            r = subprocess.run([sys.executable, "-I", str(RAIZ / "mapear_evidencia.py"), str(q), str(e)],
                               check=True, capture_output=True, text=True)
            self.assertIn("Nube: gcp", r.stdout)
            self.assertNotIn("AVISO", r.stdout)
            doc = json.loads(q.read_text(encoding="utf-8"))
            aplic = [c for cap in doc["capacidades"].values() for lv in cap["criterios"].values()
                     for c in lv if c.get("origen") == "evidencia_automatica"]
            self.assertGreaterEqual(len(aplic), 3)
            self.assertTrue(all(c["nube"] == "gcp" for c in aplic))


if __name__ == "__main__":
    unittest.main()
