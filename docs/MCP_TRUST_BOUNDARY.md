# MCP Trust Boundary

MCP servers and tools should be treated as privileged integration surfaces.

## Rules

- Do not put secrets in prompts.
- Do not give raw provider tools to every agent by default.
- Prefer backend-issued short-lived credentials.
- Use allowlists for tool names, scopes, and sessions.
- Log tool execution without storing secret payloads.
- Treat destructive writes as approval-gated operations.

## Example Boundary

```mermaid
sequenceDiagram
    participant Agent
    participant MCP as MCP Tool
    participant Policy as Policy Layer
    participant Provider

    Agent->>MCP: request tool call
    MCP->>Policy: validate session, scope, and input
    Policy->>Provider: execute authorized action
    Provider-->>Policy: result
    Policy-->>MCP: redacted result
    MCP-->>Agent: response
```

