"""Validate that the sample software factory repository keeps its core surfaces."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "AGENTS.md",
    "DESIGN.md",
    "README.md",
    ".agents/skills/plan-before-code/SKILL.md",
    ".agents/skills/agentic-code-review/SKILL.md",
    ".cursor/rules/software-factory.mdc",
    ".github/workflows/ci.yml",
    ".github/pull_request_template.md",
    "docs/SOFTWARE_FACTORY.md",
    "docs/FACTORY_METRICS.md",
    "docs/MCP_TRUST_BOUNDARY.md",
    "docs/AI_CODE_REVIEW_LOOP.md",
    "docs/SECURITY_AND_PERMISSIONS.md",
    "docs/CONTAINERS_AND_RUNTIME_IMAGES.md",
    "docs/MODEL_RUNTIME.md",
    "docs/SUBAGENT_WORKFLOW.md",
    "specs/use-cases/use-case-001-example.md",
    "plans/PLAN_EXAMPLE_FEATURE.md",
    "templates/plans/PLAN_TEMPLATE.md",
    "templates/specs/USE_CASE_TEMPLATE.md",
    "templates/review/REVIEW_CHECKLIST.md",
    "templates/skills/SKILL_TEMPLATE.md",
    "templates/mcp/TOOL_POLICY.md",
]


def main() -> None:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing:
        formatted = "\n".join(f"- {path}" for path in missing)
        raise SystemExit(f"Missing required factory files:\n{formatted}")

    docs = ROOT / "docs"
    if len(list(docs.glob("*.md"))) < 8:
        raise SystemExit("Expected at least 8 docs files in docs/.")

    skills = ROOT / ".agents" / "skills"
    if len(list(skills.glob("*/SKILL.md"))) < 2:
        raise SystemExit("Expected at least 2 agent skills.")

    print("factory validation passed")


if __name__ == "__main__":
    main()
