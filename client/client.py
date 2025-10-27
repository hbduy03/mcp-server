# client.py
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server_params = StdioServerParameters(
        command="D:\\HocTap\\Python\\calculator-server\\venv\\Scripts\\python.exe",
        args=["main.py"],  # main.py trong folder client này
        env=None
    )

    print("🔌 Connecting to MCP server...")

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            print("✅ Connected!\n")

            # List tools
            tools = await session.list_tools()
            print("📋 Available tools:")
            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description}")
            print()

            # Test add
            print("🧮 Calling add(5, 3)...")
            result = await session.call_tool("add", arguments={"a": 5, "b": 3})
            print(f"Result: {result.content}\n")

            print("🧮 Calling add(100, 250)...")
            result2 = await session.call_tool("add", arguments={"a": 100, "b": 250})
            print(f"Result: {result2.content}\n")

            # List resources
            resources = await session.list_resources()
            print("📦 Available resources:")
            for resource in resources.resources:
                print(f"  - {resource.uri}")
            print()

            # Test resource
            print("👋 Reading greeting://World...")
            greeting = await session.read_resource("greeting://World")
            print(f"Result: {greeting.contents}\n")

            print("👋 Reading greeting://Alice...")
            greeting2 = await session.read_resource("greeting://Alice")
            print(f"Result: {greeting2.contents}\n")


if __name__ == "__main__":
    asyncio.run(main())