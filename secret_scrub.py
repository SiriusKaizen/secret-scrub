#!/usr/bin/env python3
"""Redact common secrets from text before sharing it."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


REDACTIONS: list[tuple[re.Pattern[str], str]] = [
    (re.compile(r"(?i)(authorization:\s*bearer\s+)[A-Za-z0-9._~+/=-]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(x-api-key:\s*)[A-Za-z0-9._~+/=-]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(api[_-]?key\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(webhook[_-]?secret\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(mcp[_-]?token\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(n8n[_-]?api[_-]?key\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(token\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(password\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"(?i)(secret\s*[:=]\s*)[^\s,;]+"), r"\1[REDACTED]"),
    (re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"), "[OPENAI_KEY_REDACTED]"),
    (re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"), "[GITHUB_TOKEN_REDACTED]"),
    (re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b"), "[SLACK_TOKEN_REDACTED]"),
    (re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"), "[EMAIL_REDACTED]"),
    (re.compile(r"(?i)(https?://)([^/\s:@]+):([^@\s]+)@"), r"\1[USER]:[PASSWORD]@"),
]


def scrub_text_with_count(text: str) -> tuple[str, int]:
    redacted = text
    total = 0
    for pattern, replacement in REDACTIONS:
        redacted, count = pattern.subn(replacement, redacted)
        total += count
    return redacted, total


def scrub_text(text: str) -> str:
    return scrub_text_with_count(text)[0]


def read_input(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="secret-scrub")
    parser.add_argument("path", nargs="?", help="File to redact. Reads stdin when omitted.")
    parser.add_argument("--output", "-o", help="Write redacted text to this file")
    parser.add_argument("--check", action="store_true", help="Exit with 1 when input needs redaction")
    parser.add_argument("--count", action="store_true", help="Print redaction count to stderr")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    original = read_input(args.path)
    redacted, redaction_count = scrub_text_with_count(original)
    if args.check:
        return 1 if redacted != original else 0
    if args.output:
        Path(args.output).write_text(redacted, encoding="utf-8")
    else:
        print(redacted, end="")
    if args.count:
        print(f"redactions={redaction_count}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
