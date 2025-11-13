from code.tax.server import is_auth

FAILED_ATTEMPTS = 0
MAX_ATTEMPTS = 5
LOCKOUT_TIME_SECONDS = 300

@mcp.tool()
def admin_task(api_key: str, data: str) -> str:
    global FAILED_ATTEMPTS

    if FAILED_ATTEMPTS >= MAX_ATTEMPTS:
        return "Error: Rate limit exceeded due to too many failed attempts."

    if not is_auth(api_key):
        FAILED_ATTEMPTS += 1  # Tăng số lần thử sai
        return "Error: Invalid or missing authentication credentials."

    FAILED_ATTEMPTS = 0


