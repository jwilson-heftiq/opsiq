import re
from pathlib import Path

FORBIDDEN = [
    "fastapi",
    "boto3",
    "requests",
    "httpx",
    "sqlalchemy",
    "databricks",
    "pyspark",
    "os", "sys",
]

DOMAIN_DIRS = [
    Path("engines") / "retention" / "domain",
    Path("platform_core") / "domain",
]

IMPORT_RE = re.compile(
    r"^\s*import\s+([a-zA-Z0-9_\.]+)|^\s*from\s+([a-zA-Z0-9_\.]+)\s+import", re.M
)

def test_domain_has_no_forbidden_imports():
    violations = []
    for base in DOMAIN_DIRS:
        for py in base.rglob("*.py"):
            text = py.read_text(encoding="utf-8")
            for m in IMPORT_RE.finditer(text):
                mod = (m.group(1) or m.group(2) or "").split(".")[0]
                if mod in FORBIDDEN:
                    violations.append(f"{py}: forbidden import '{mod}'")
    assert not violations, "ADR violation(s):\n" + "\n".join(violations)
