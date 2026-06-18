# Contributing

Thanks for helping improve secret-scrub.

## Local Setup

This project uses the Python standard library only.

```bash
python3 -m unittest discover -s tests
python3 secret_scrub.py examples/before.log
python3 secret_scrub.py examples/before.log --check
```

## Contribution Guidelines

- Add tests for every new redaction rule.
- Use fake tokens, fake paths, and example-only metadata in tests.
- Avoid rules that over-redact normal text unless the behavior is documented.
- Keep redaction local-only. The CLI must not send input over the network.

## Useful Areas

- JSON reports for redaction counts.
- More configurable custom patterns.
- Safer diff output for public issue reports.
- Additional examples for common local automation logs.
