import os

BASE_URL = 'https://www.amazon.in'

# Optional support for local .env files (convenience only). This does not change
# security posture: never commit .env to source control. The project suggests
# using CI/CD secret stores for production runs.
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    # python-dotenv is optional; environment variables can be set directly.
    pass

# SECURITY: Do NOT hardcode credentials in source code.
# Read credentials from environment variables and fail fast if missing.
email_id = os.environ.get('AMAZON_EMAIL')
password_id = os.environ.get('AMAZON_PASSWORD')

if not email_id or not password_id:
    raise EnvironmentError(
        "Required environment variables AMAZON_EMAIL and AMAZON_PASSWORD are not set. "
        "Set them in your shell, CI environment, or create a local .env file (not committed)."
    )
