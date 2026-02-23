# Launch Guide: Weather Agent MCP

An MCP server that exposes a `get_weather` tool to fetch weather for any city.

## Prerequisites

- Python 3.9+

## Setup

```bash
git clone https://github.com/jackmgorelick/TestMCP.git
cd TestMCP
python -m venv venv
source venv/bin/activate   # macOS/Linux
pip install mcp
```

## Run the server

```bash
python research_agent.py
```

The server starts on stdio and waits for MCP client connections.

## Add to Claude Desktop

Add this to your Claude Desktop config (`~/Library/Application Support/Claude/claude_desktop_config.json` on macOS):

```json
{
  "mcpServers": {
    "weather-agent": {
      "command": "python",
      "args": ["/absolute/path/to/TestMCP/research_agent.py"]
    }
  }
}
```

Replace `/absolute/path/to/` with the actual path, then restart Claude Desktop.

## Add to Claude Code

```bash
claude mcp add weather-agent python /absolute/path/to/TestMCP/research_agent.py
```

## Available Tools

| Tool | Description |
|---|---|
| `get_weather` | Returns temperature, condition, and humidity for a given city |

## Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector python research_agent.py
```

## Troubleshooting

| Problem | Fix |
|---|---|
| `ModuleNotFoundError: mcp` | Run `pip install mcp` |
| Server not showing in Claude | Check the config path and restart the client |
