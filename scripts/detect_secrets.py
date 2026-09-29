#!/usr/bin/env python3
"""Heuristic secret detector. Review findings manually; false positives are expected."""
from pathlib import Path
import re, json, sys
ROOT=Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
IGNORE={".git", ".venv", "venv", "__pycache__", "node_modules", "build", "dist"}
patterns=[
 ("generic_secret_assignment", re.compile(r"(?i)\b(api[_-]?key|secret|password|token|private[_-]?key)\b\s*[:=]\s*['"][^'"]{8,}['"]")),
 ("database_uri_credentials", re.compile(r"(?i)(mongodb(?:\+srv)?|postgres(?:ql)?|mysql)://[^\s'"]+")),
 ("google_api_key", re.compile(r"AIza[0-9A-Za-z_-]{20,}")),
]
findings=[]
for p in ROOT.rglob("*"):
    if not p.is_file() or any(x in IGNORE for x in p.parts): continue
    if p.stat().st_size>2_000_000: continue
    try:text=p.read_text(errors="ignore")
    except:continue
    for name,rx in patterns:
        for m in rx.finditer(text):
            line=text.count("\n",0,m.start())+1
            findings.append({"type":name,"file":str(p.relative_to(ROOT)),"line":line,"match_preview":m.group(0)[:80]})
print(json.dumps({"findings":findings},indent=2))
