#!/usr/bin/env python3
"""Find Streamlit usage and common UI/state constructs in a local repository."""
from pathlib import Path
import re, json, sys
ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
IGNORE={".git", ".venv", "venv", "__pycache__", "node_modules", "build", "dist"}
pat=re.compile(r"\bst\.(\w+)|\bstreamlit\b")
findings=[]
for p in ROOT.rglob("*.py"):
    if any(x in IGNORE for x in p.parts): continue
    text=p.read_text(errors="ignore")
    matches=pat.findall(text)
    if matches:
        findings.append({"file":str(p.relative_to(ROOT)),"constructs":sorted(set(m for m in matches if m))})
print(json.dumps({"streamlit_detected":bool(findings),"files":findings},indent=2))
