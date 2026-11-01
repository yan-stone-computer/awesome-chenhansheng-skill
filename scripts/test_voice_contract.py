import unittest
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


if __name__ == "__main__":
    unittest.main()
