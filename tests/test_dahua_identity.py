from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.dahua_identity import (
    IdentityIndex,
    classify_identifier,
    load_mappings,
    part_family,
)
from src.gks_catalog import extract_models, match_filename


class DahuaIdentityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_mappings(ROOT / "data" / "mapping-0922.csv")
        cls.index = IdentityIndex(cls.rows)

    def test_table_scale(self):
        parts = {r.part_no for r in self.rows if r.part_no}
        self.assertGreaterEqual(len(self.rows), 20000)
        self.assertGreaterEqual(len(parts), 20000)

    def test_classify_part_no(self):
        self.assertEqual(classify_identifier("1.0.01.04.31634-0016"), "part_no")
        self.assertEqual(classify_identifier("1.0.01.04.39197"), "part_no")

    def test_classify_internal_by_lens(self):
        self.assertEqual(
            classify_identifier("DH-IPC-HCBW8442P-0250B-EUR"),
            "internal_model",
        )

    def test_part_lookup_hcbw8442(self):
        result = self.index.lookup("1.0.01.04.31634-0016")
        self.assertTrue(result.rows)
        row = result.rows[0]
        self.assertEqual(row.internal_model, "DH-IPC-HCBW8442P-0250B")
        self.assertEqual(row.external_model, "DH-IPC-HCBW8442P")
        self.assertIn("IPC", part_family(row.part_no))

    def test_external_expands_to_lens_variants(self):
        result = self.index.lookup("DH-IPC-HDW8441X-3D", limit=20)
        internals = {r.internal_model for r in result.rows}
        self.assertTrue(any("0200B" in m for m in internals))
        self.assertTrue(any("0280B" in m for m in internals))
        self.assertTrue(all(r.external_model == "DH-IPC-HDW8441X-3D" for r in result.rows))

    def test_eur_region_maps_to_same_external(self):
        result = self.index.lookup("DH-IPC-HCBW8442P-0250B-EUR")
        self.assertTrue(result.rows)
        self.assertEqual(result.rows[0].external_model, "DH-IPC-HCBW8442P")
        self.assertTrue(result.rows[0].part_no.startswith("1.0.01.04.39197"))

    def test_discount_is_not_a_camera(self):
        self.assertEqual(part_family("1.4.01.07.00001"), "Discount 折扣虚项")

    def test_dae_part_family(self):
        self.assertEqual(part_family("1.0.01.02.11805"), "DAE 车载/移动监控")

    def test_mxvr8212_lookup(self):
        result = self.index.lookup("MXVR8212", limit=10)
        self.assertTrue(result.rows)
        self.assertTrue(any("MXVR8212" in r.internal_model for r in result.rows))

    def test_gks_filename_extracts_external_model(self):
        models = extract_models("Datasheet_DH-IPC-HDW8441X-3D_EN.pdf")
        self.assertEqual(models, ["DH-IPC-HDW8441X-3D"])

    def test_gks_filename_maps_to_part_numbers(self):
        models, rows = match_filename(
            self.index, "Datasheet_DH-IPC-HDW8441X-3D_EN.pdf"
        )
        self.assertEqual(models, ["DH-IPC-HDW8441X-3D"])
        self.assertTrue(rows)
        self.assertTrue(all(r.external_model == "DH-IPC-HDW8441X-3D" for r in rows))

    def test_access_control_part_family(self):
        self.assertEqual(part_family("1.0.01.25.11076"), "门禁/考勤 Access Control")
        self.assertEqual(part_family("1.2.01.27.10287"), "电锁/门禁配件")

    def test_asi_lookup(self):
        result = self.index.lookup("ASI6213J-MW", limit=10)
        self.assertTrue(result.rows)
        self.assertTrue(any("ASI6213J-MW" in r.internal_model for r in result.rows))
        self.assertTrue(result.rows[0].part_no.startswith("1.0.01.25"))

    def test_gks_filename_extracts_access_model(self):
        models = extract_models("DHI-ASI6214J-MFW_1.0.01.25.11077_MTBF Report.pdf")
        self.assertIn("DHI-ASI6214J-MFW", models)
        models2 = extract_models("Datasheet_DHI-ASC2204C-S_EN.pdf")
        self.assertEqual(models2, ["DHI-ASC2204C-S"])


if __name__ == "__main__":
    unittest.main()
