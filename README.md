# secret-scrub

A tiny CLI for sanitizing logs, prompts, and config snippets before sharing them with AI tools, GitHub issues, or teammates.

## What it does

- Redacts common API keys, bearer tokens, and authorization headers.
- Redacts `.env` style secret assignments.
- Masks email addresses and obvious sensitive URLs.
- Works from a file or standard input.

## Status

Small MVP. It is intentionally conservative and easy to audit.

## Quick Start

```bash
python3 secret_scrub.py sample.log
cat sample.log | python3 secret_scrub.py
```

## Safety

This tool does not send content over the network. Redaction happens locally.

## License

MIT
