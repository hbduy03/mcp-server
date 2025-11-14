from mcp.server.fastmcp import FastMCP

# Khởi tạo MCP server
mcp = FastMCP("Demo")

# Tool cộng hai số
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# Resource mẫu
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Return a greeting for the given name"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()
