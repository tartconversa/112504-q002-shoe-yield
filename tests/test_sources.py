"""核对业务资料的格式和交接标识。"""
import csv
import unittest
from pathlib import Path

SAMPLES = Path(__file__).resolve().parents[1] / "samples"
SCHEMAS = {'lots': ['lot', 'origin', 'bags', 'unopened_shoes', 'clean_job', 'process_day'], 'sample': ['item', 'lot', 'bag', 'selection', 'side', 'size', 'condition', 'known_on'], 'counts': ['record', 'lot', 'side', 'size', 'usable', 'as_of', 'revision'], 'release': ['release', 'job', 'lot', 'max_pairs', 'reported', 'state'], 'schools': ['school', 'ordered_size', 'acceptable_sizes', 'min_pack', 'requested', 'deadline', 'allowed_jobs'], 'travel': ['truck', 'date', 'cap_pairs', 'stops'], 'receipts': ['delivery', 'school', 'truck', 'lot', 'pairs', 'size', 'at', 'status'], 'sampling_frames': ['stratum', 'lot', 'eligible_bags', 'random_bags', 'revision']}
REFERENCES = [('sample', 'lot', 'lots', 'lot'), ('counts', 'lot', 'lots', 'lot'), ('release', 'lot', 'lots', 'lot'), ('receipts', 'school', 'schools', 'school'), ('receipts', 'truck', 'travel', 'truck'), ('sampling_frames', 'lot', 'lots', 'lot')]
OBSERVED = [('release', 'release', 'R2', 2), ('receipts', 'truck', 'V3', 2), ('sample', 'lot', 'L1', 5)]

class Sources(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tables = {}
        for table, fields in SCHEMAS.items():
            with (SAMPLES / (table + ".csv")).open(encoding="utf-8", newline="") as stream:
                records = csv.DictReader(stream, strict=True)
                if records.fieldnames != fields:
                    raise ValueError(f"字段不一致：{table}")
                cls.tables[table] = list(records)

    def test_records_have_documented_columns(self):
        for table, rows in self.tables.items():
            with self.subTest(table=table):
                self.assertTrue(rows)
                self.assertTrue(all(None not in row and None not in row.values() for row in rows))

    def test_source_links(self):
        for left, field, right, target in REFERENCES:
            with self.subTest(table=left, field=field):
                keys = {row[field] for row in self.tables[left] if row[field]}
                self.assertTrue(keys)
                self.assertLessEqual(keys, {row[target] for row in self.tables[right]})

    def test_shared_source_records_are_available(self):
        for table, field, value, seen in OBSERVED:
            with self.subTest(table=table, field=field, value=value):
                self.assertGreaterEqual(sum(row[field] == value for row in self.tables[table]), seen)
