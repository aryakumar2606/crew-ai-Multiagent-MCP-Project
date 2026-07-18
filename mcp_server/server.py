from mcp.server.fastmcp import FastMCP

from mcp_server.registry import register_tools

mcp = FastMCP("Analytics MCP Server")

register_tools(mcp)

if __name__ == "__main__":
    print("Starting MCP Server...")
    mcp.run()