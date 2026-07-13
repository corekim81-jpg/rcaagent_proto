# demo_mcp.py
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """두 숫자를 더한다"""
    return a + b

if __name__ == "__main__":
    mcp.run()