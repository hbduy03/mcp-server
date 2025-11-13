# MCP Server Configuration for VS Code

This file configures the MCP servers available in VS Code.

## Current Servers

### add-numbers
A simple MCP server that performs arithmetic addition on two numbers.

- **Command**: `node`
- **Args**: `build/index.js`
- **Transport**: STDIO
- **Available Tools**:
  - `add_numbers`: Add two numbers together

## Using this Configuration

To enable this server in VS Code:

1. Copy this file to your VS Code settings directory:
   - Windows: `%APPDATA%\Code\User\globalStorage\...`
   - macOS: `~/Library/Application Support/Code/User/globalStorage/...`
   - Linux: `~/.config/Code/User/globalStorage/...`

2. Or configure inline in VS Code settings with the `mcp.servers` setting

3. Restart VS Code to load the configuration

## Adding More Servers

To add additional MCP servers to this configuration:

```json
{
  "servers": {
    "new-server": {
      "type": "stdio",
      "command": "node",
      "args": ["path/to/server/index.js"]
    }
  }
}
```

## Documentation

- [MCP Protocol Documentation](https://modelcontextprotocol.io/)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
