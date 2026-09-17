from mcp.server.fastmcp import FastMCP

mcp = FastMCP("lab-server")

@mcp.tool()
def word_count(text: str) -> int:
    """Count words in the given text."""
    return len(text.split())

if __name__ == "__main__":
    mcp.run()