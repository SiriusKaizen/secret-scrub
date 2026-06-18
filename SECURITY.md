# Security Policy

secret-scrub exists to reduce accidental leakage before logs, prompts, and config snippets are shared.

## Supported Scope

The CLI redacts common API keys, bearer tokens, secret assignments, local endpoints, user paths, chat metadata, and operator profile fields. It is not a substitute for manual review before publishing sensitive logs.

## Reporting a Security Issue

Please open a GitHub issue with a minimal fake sample that demonstrates the missed redaction. Do not paste real secrets, tokens, private URLs, chat ids, or production logs.

## Maintainer Notes

- Treat missed secret-like values as security bugs.
- Keep examples fake and easy to audit.
- Prefer conservative local behavior over remote scanning or hidden network calls.
