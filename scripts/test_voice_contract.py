import unittest
import importlib.util
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
COMPACT_CONFIGS = [
    ROOT / "configs" / "cursor" / "chen-hansheng-wisdom.mdc",
    ROOT / "configs" / "opencode" / "AGENTS.md",
    ROOT / "configs" / "trae" / "chen-hansheng-wisdom.md",
]


class VoiceContractTests(unittest.TestCase):
    def test_full_skill_prioritizes_voice_before_strategy(self):
        skill = (ROOT / "SKILL.md").read_text("utf-8")
        self.assertIn("## 零、角色声线契约（先于所有策略）", skill)
        self.assertIn("### 0.3 AI 腔避雷", skill)
        self.assertIn("不要把每条回复写成分析报告", skill)
        self.assertIn("## 五、补充技巧库（28–45）", skill)
        self.assertIn("| 45 |", skill)

    def test_claude_variant_contains_the_same_voice_contract(self):
        skill = (ROOT / "configs" / "claude-code" / "SKILL.md").read_text("utf-8")
        self.assertIn("## 零、角色声线契约（先于所有策略）", skill)
        self.assertIn("### 0.3 AI 腔避雷", skill)

    def test_compact_variants_keep_the_highest_priority_constraints(self):
        for path in COMPACT_CONFIGS:
            with self.subTest(path=path.name):
                text = path.read_text("utf-8")
                self.assertIn("## 零、声线硬约束", text)
                self.assertIn("拒绝 AI 报告腔", text)
                self.assertIn("口头禅低频使用", text)
                self.assertIn("28–45", text)

    def test_readme_describes_the_expanded_skill(self):
        readme = (ROOT / "README.md").read_text("utf-8")
        self.assertIn("45 个维度", readme)
        self.assertIn("角色声线契约", readme)
        self.assertIn("语气标定样例", readme)

    def test_voice_calibration_examples_are_wired_into_the_skill(self):
        examples = (ROOT / "references" / "voice-examples.md").read_text("utf-8")
        skill = (ROOT / "SKILL.md").read_text("utf-8")
        self.assertIn("语气标定样例", examples)
        self.assertGreaterEqual(examples.count("**用户：**"), 8)
        self.assertIn("references/voice-examples.md", skill)

    def test_style_checker_rejects_report_voice(self):
        spec = importlib.util.spec_from_file_location(
            "check_reply_style", ROOT / "scripts" / "check_reply_style.py"
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)

        natural = "先别急。你先把时间点发过去，问他明早几点要。别的等他回。"
        report = (
            "首先，这是一个复杂的问题。其次，需要注意的是沟通边界。"
            "最后，希望对你有帮助。"
        )
        self.assertEqual(module.audit_reply(natural), [])
        self.assertGreaterEqual(len(module.audit_reply(report)), 3)

    def test_default_skill_mode_forbids_markdown_reports(self):
        skill = (ROOT / "SKILL.md").read_text("utf-8")
        self.assertIn("默认只输出对话", skill)
        self.assertIn("check_reply_style.py", skill)

    def test_every_voice_example_passes_the_style_checker(self):
        spec = importlib.util.spec_from_file_location(
            "check_reply_style", ROOT / "scripts" / "check_reply_style.py"
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        examples = (ROOT / "references" / "voice-examples.md").read_text("utf-8")
        replies = re.findall(r"\*\*回复：\*\*\s*(.*?)(?=\n---|\Z)", examples, re.S)
        self.assertEqual(len(replies), 12)
        for index, reply in enumerate(replies, start=1):
            with self.subTest(example=index):
                self.assertEqual(module.audit_reply(reply), [])


if __name__ == "__main__":
    unittest.main()
