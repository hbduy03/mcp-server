from mcp.server.fastmcp import FastMCP
ADMIN_KEY = "BaoDuy"
LOCKOUT_END_TIME = 0.0

mcp = FastMCP("Auth_test")

def is_auth(key: str) -> bool:
    return key == ADMIN_KEY

@mcp.tool()
def hello(key: str, text: str) -> str:
    if not is_auth(key):
        print(f'Key doesnt matched with program!')
        return 'Please input another key'
    else:
        return f'Hello {text}'
