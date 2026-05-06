# Validation Matrix

| Risk | Validation | Command Or Evidence | Owner | Required Before Merge |
| --- | --- | --- | --- | --- |
| Correctness regression | Unit tests | `make test` | implementation agent | yes |
| Style or syntax drift | Lint | `make lint` | implementation agent | yes |
| Missing factory artifacts | Factory validation | `make validate-factory` | implementation agent | yes |
| Docs/spec drift | Review checklist | PR review evidence | review agent | yes |
| Tool permission issue | MCP policy review | policy doc plus review notes | maintainer | when applicable |
