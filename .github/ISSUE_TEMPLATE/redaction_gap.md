---
name: Redaction gap
about: Report a pattern that should be redacted
title: "[redaction-gap] "
labels: security, redaction
assignees: ""
---

## Pattern type

## Safe synthetic example

Do not paste real secrets. Use a fake value with the same shape.

```text
token=example-placeholder
```

## Expected replacement

```text
token=[REDACTED]
```

## Tool context

- CLI version or commit:
- Input source: file or stdin
