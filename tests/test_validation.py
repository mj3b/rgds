"""Behavior checks for the two validation entry points using derived test records."""
import contextlib
import copy
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import validate_all_examples as batch
import validate_decision_log as single


class ValidationRegressionTests(unittest.TestCase):
    def setUp(self):
        self.record = json.loads((ROOT / 'examples/rgds-dec-0006-ai-assisted-conditional-go.json').read_text())

    def run_record(self, record, strict=True):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'test-record.json'
            path.write_text(json.dumps(record))
            results = []
            for module, args in [(single, [str(path)]), (batch, [])]:
                argv = ['validator'] + args + (['--strict'] if strict else ['--semantic'] if module is single else [])
                output = io.StringIO()
                with patch.object(batch, 'EXAMPLES_DIR', Path(directory)), patch.object(sys, 'argv', argv), contextlib.redirect_stdout(output):
                    try:
                        code = module.main()
                    except SystemExit as exc:
                        results.append((exc.code, output.getvalue()))
                    else:
                        results.append((code, output.getvalue()))
            return results

    def assert_result(self, record, expected, message=None, strict=True):
        for code, output in self.run_record(record, strict):
            self.assertEqual(code, expected, output)
            if message:
                self.assertIn(message, output)

    def test_canonical_records_pass_both_strict_entry_points(self):
        for path in sorted((ROOT / 'examples').glob('*.json')):
            with self.subTest(record=path.name):
                self.assert_result(json.loads(path.read_text()), 0)

    def test_empty_ai_tool_fields_fail(self):
        for field in ['tool_name', 'tool_purpose']:
            with self.subTest(field=field):
                record = copy.deepcopy(self.record)
                record['ai_assistance'][field] = '  '
                self.assert_result(record, 1, field)

    def test_empty_human_review_fails(self):
        self.record['ai_assistance']['human_review'] = []
        self.assert_result(self.record, 1, 'human_review')

    def test_missing_ai_confidence_is_warning_unless_strict(self):
        self.record['ai_assistance']['ai_risk_assessment'] = {}
        self.assert_result(self.record, 0, 'confidence_band', strict=False)
        self.assert_result(self.record, 1, 'confidence_band')

    def test_invalid_calendar_date_fails(self):
        self.record['gate']['decision_deadline'] = '2026-02-30T12:00:00Z'
        self.assert_result(self.record, 1, 'date')

    def test_escalate_is_not_an_outcome(self):
        self.record['decision_outcome']['outcome'] = 'escalate'
        self.assert_result(self.record, 1, 'escalate')

    def test_go_and_defer_are_valid_contract_values(self):
        for outcome in ['go', 'defer']:
            with self.subTest(outcome=outcome):
                record = copy.deepcopy(self.record)
                record['decision_outcome']['outcome'] = outcome
                self.assert_result(record, 0)

    def test_conditional_go_without_conditions_fails(self):
        self.record['decision_outcome']['conditions'] = []
        self.assert_result(self.record, 1, 'conditions')

    def test_required_evidence_deferral_requires_follow_up(self):
        record = json.loads((ROOT / 'examples/rgds-dec-0003-defer-required-evidence.json').read_text())
        record['actions'] = []
        self.assert_result(record, 1, 'actions')


if __name__ == '__main__':
    unittest.main()
