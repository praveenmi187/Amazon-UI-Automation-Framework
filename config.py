import os

BASE_URL = 'https://www.amazon.in'

# SECURITY: Do NOT hardcode credentials in source code.
# Read credentials from environment variables and fail fast if missing.
email_id = os.environ.get('AMAZON_EMAIL')
password_id = os.environ.get('AMAZON_PASSWORD')

if not email_id or not password_id:
    raise EnvironmentError(
        "Required environment variables AMAZON_EMAIL and AMAZON_PASSWORD are not set. "
        "Set them in your shell or CI environment; do NOT store secrets in source control."
    )
