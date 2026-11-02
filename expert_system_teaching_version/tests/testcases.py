
import unittest
from pathlib import Path

from engine import ForwardChainingEngine
from kb_loader import load_rules


KB_PATH = Path(__file__).resolve().parents[1] / "kb" / "laptop_rules.json"


class TestLaptopAdvisor(unittest.TestCase):

    def setUp(self):
        self.rules = load_rules(str(KB_PATH))

    def check_facts(self, facts, expected):
        engine = ForwardChainingEngine(self.rules)
        engine.assert_facts(facts)
        engine.run()
        self.assertIn(expected, engine.facts)

    def test_premium_ultrabook(self):
        self.check_facts(
            ["budget_high", "portable", "long_battery"],
            "recommend:premium_ultrabook"
        )

    def test_budget_ultrabook(self):
        self.check_facts(
            ["budget_low", "office_only", "portable"],
            "recommend:budget_ultrabook"
        )

    def test_midrange_gaming(self):
        self.check_facts(
            ["gaming", "budget_medium"],
            "recommend:midrange_gaming_laptop"
        )

    def test_high_end_gaming(self):
        self.check_facts(
            ["gaming", "budget_high"],
            "recommend:high_end_gaming_laptop"
        )

    def test_creative_ram(self):
        self.check_facts(
            ["creative_work", "portable"],
            "spec:ram_16_plus"
        )

    def test_creative_display(self):
        self.check_facts(
            ["creative_work", "large_screen"],
            "spec:display_15_plus_color_accurate"
        )

    def test_travel_battery(self):
        self.check_facts(
            ["travel_often", "long_battery"],
            "spec:battery_60wh_plus"
        )

    def test_macos(self):
        self.check_facts(
            ["pref_os_macos"],
            "spec:macos_required"
        )

    def test_ai_acceleration(self):
        self.check_facts(
            ["needs_ai_accel"],
            "spec:gpu_with_tensor_cores"
        )

    def test_linux(self):
        self.check_facts(
            ["pref_os_linux", "office_only"],
            "spec:linux_friendly_hw"
        )

    def test_no_matching_rule(self):
        engine = ForwardChainingEngine(self.rules)
        engine.assert_facts(["pref_os_windows"])
        engine.run()

        self.assertEqual(len(engine.trace), 0)
        self.assertEqual(engine.conclusions()["recommendations"], [])

    def test_all_conditions_required(self):
        engine = ForwardChainingEngine(self.rules)
        engine.assert_facts(["budget_high", "portable"])
        engine.run()

        self.assertNotIn(
            "recommend:premium_ultrabook",
            engine.facts
        )

    def test_no_duplicate_firing(self):
        engine = ForwardChainingEngine(self.rules)
        engine.assert_facts(
            ["budget_high", "portable", "long_battery"]
        )
        engine.run()
        count = len(engine.trace)
        engine.run()

        self.assertEqual(len(engine.trace), count)


if __name__ == "__main__":
    unittest.main()
