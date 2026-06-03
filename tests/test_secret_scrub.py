import unittest
import tempfile
from pathlib import Path

import secret_scrub


class SecretScrubTests(unittest.TestCase):
    def test_redacts_email_and_openai_key_shape(self):
        fake_key = "sk-" + "test" + ("0" * 24)
        text = f"owner=operator@example.invalid api_key={fake_key}"
        redacted = secret_scrub.scrub_text(text)
        self.assertNotIn("operator@example.invalid", redacted)
        self.assertNotIn(fake_key, redacted)
        self.assertIn("[EMAIL_REDACTED]", redacted)

    def test_redacts_agent_webhook_fields(self):
        text = "webhook_secret=abc123 mcp_token=local-token n8n_api_key=n8n-secret"
        redacted = secret_scrub.scrub_text(text)
        self.assertEqual(redacted.count("[REDACTED]"), 3)

    def test_check_mode_reports_dirty_input(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            sample = Path(tmpdir) / "sample.log"
            sample.write_text("token=abc123", encoding="utf-8")
            exit_code = secret_scrub.main([str(sample), "--check"])
        self.assertEqual(exit_code, 1)


if __name__ == "__main__":
    unittest.main()
