#!/usr/bin/env python3
"""Flag common AI-report patterns before sending a Chen-style reply."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REPORT_PATTERNS = [
    (r"首先[，,]?", "report transition: 首先"),
    (r"其次[，,]?", "report transition: 其次"),
    (r"最后[，,]?$", "report transition: 最后"),
    (r"综上所述|综上[，,]?", "summary voice"),
    (r"值得注意的是", "academic filler"),
    (r"从[^。\n]{0,16}角度来看", "framing filler"),
    (r"希望(?:这些建议|对你)有?帮助", "assistant sign-off"),
    (r"可以理解你的感受", "therapy-template phrasing"),
    (r"这是一个复杂的问题", "generic opener"),
    (r"需要综合判断", "generic disclaimer"),
    (r"本质上|核心在于", "lecture voice"),
    (r"以下是|接下来(?:我们|我)?", "assistant setup"),
    (r"作为一个?(?:AI|人工智能|语言模型|助手)", "self-referential AI voice"),
    (r"我可以帮你|我建议你", "assistant framing"),
]

STRUCTURE_PATTERNS = [
    (r"(?m)^#{1,6}\s+", "Markdown heading in conversational reply"),
    (r"(?m)^\s*(?:[-*+]|\d+\.)\s+", "list formatting in conversational reply"),
]

SIGNATURE_RE = re.compile(r"老子|嘿嘿|妈的|狗日的|卧槽|有卵子用")


def audit_reply(text: str, structured: bool = False) -> list[str]:
    """Return style violations for the default conversational mode."""
    problems: list[str] = []
    for pattern, label in REPORT_PATTERNS:
        if re.search(pattern, text):
            problems.append(label)

    if not structured:
        for pattern, label in STRUCTURE_PATTERNS:
            if re.search(pattern, text):
                problems.append(label)

    if len(SIGNATURE_RE.findall(text)) > 1:
        problems.append("more than one signature phrase")

    long_sentences = [
        sentence
        for sentence in re.split(r"[。！？!?]\s*", text)
        if len(sentence.strip()) > 70
    ]
    if long_sentences:
        problems.append("sentence longer than 70 characters")

    return problems


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Check a draft for AI-report voice before sending it."
    )
    parser.add_argument("file", nargs="?", help="UTF-8 text file; omit to read stdin")
    parser.add_argument("--text", help="Check this text directly")
    parser.add_argument(
        "--structured",
        action="store_true",
        help="Allow headings and lists when the user explicitly requested a report.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.text is not None:
        text = args.text
    elif args.file:
        text = Path(args.file).read_text("utf-8")
    else:
        text = sys.stdin.read()
    problems = audit_reply(text, structured=args.structured)
    if not problems:
        print("PASS")
        return 0
    print("FAIL")
    for problem in problems:
        print(f"- {problem}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
