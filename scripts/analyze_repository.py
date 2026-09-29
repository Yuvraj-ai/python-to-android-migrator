#!/usr/bin/env python3
"""Lightweight deterministic inventory for a local Python repository."""
from pathlib import Path
import ast, json, sys

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
IGNORE = {".git", ".venv", "venv", "node_modules", "__pycache__", "build", "dist"}

py_files = [p for p in ROOT.rglob("*.py") if not any(x in IGNORE for x in p.parts)]
imports, funcs, classes, entries = set(), [], [], []
for p in py_files:
    try: tree = ast.parse(p.read_text(errors="ignore"), filename=str(p))
    except SyntaxError: continue
    rel = str(p.relative_to(ROOT))
    for n in ast.walk(tree):
        if isinstance(n, ast.Import): imports.update(a.name.split('.')[0] for a in n.names)
        elif isinstance(n, ast.ImportFrom) and n.module: imports.add(n.module.split('.')[0])
        elif isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef)): funcs.append(f"{rel}:{n.name}")
        elif isinstance(n, ast.ClassDef): classes.append(f"{rel}:{n.name}")
    if p.name in {"app.py", "main.py", "server.py", "api.py"}: entries.append(rel)

print(json.dumps({
    "root": str(ROOT),
    "python_files": [str(p.relative_to(ROOT)) for p in py_files],
    "entry_point_candidates": sorted(set(entries)),
    "top_level_imports": sorted(imports),
    "functions": funcs,
    "classes": classes,
}, indent=2))
