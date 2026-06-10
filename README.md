# secret-scrub

A tiny CLI for sanitizing logs, prompts, and config snippets before sharing them with AI tools, GitHub issues, or teammates.

## What it does

- Redacts common API keys, bearer tokens, and authorization headers.
- Redacts `.env` style secret assignments.
- Masks email addresses and obvious sensitive URLs.
- Masks common operator-log details such as local endpoints, user paths, vault references, bot usernames, chat ids, topic ids, and agent profile names.
- Works from a file or standard input.

## Status

Small MVP. It is intentionally conservative and easy to audit.

## Quick Start

```bash
python3 secret_scrub.py sample.log
cat sample.log | python3 secret_scrub.py
python3 secret_scrub.py sample.log --check
python3 secret_scrub.py sample.log --count
```

`--check` exits with code `1` when the input would be changed. This is useful in pre-commit hooks or CI jobs.
`--count` prints the number of redactions to stderr without changing the redacted output stream.

## Operator Log Patterns

The default rules include extra coverage for local automation logs: `op://...` secret references, `chat_id`, `topic_id`, `thread_id`, bot usernames, local `127.0.0.1` or `localhost` URLs, `/Users/...` paths, and named OpenClaw/Hermes/agent profile fields. These are treated as operational metadata that should be removed before sharing public issue reports.

## Safety

This tool does not send content over the network. Redaction happens locally.

## License

MIT
