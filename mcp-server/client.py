import sys
import asyncio
from pathlib import Path
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    # Launch the server using the same Python interpreter and the server.py
    # located in this same directory.
    server_path = Path(__file__).resolve().parent / "server.py"
    server_params = StdioServerParameters(
        command=sys.executable,
        args=[str(server_path)],
    )
    async with stdio_client(server_params) as (reader, writer):
        async with ClientSession(reader, writer) as session:
            await session.initialize()

            result = await session.call_tool("add", arguments={"a": 3, "b": 4})
            print(f"Result of add tool: {result}")

if __name__ == "__main__":
    asyncio.run(main())