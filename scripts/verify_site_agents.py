#!/usr/bin/env python3
"""Verify byte identity of the shared agents and complete original reference bundles."""
import hashlib, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
lock=json.loads((root/'.agents/site-agents.lock.json').read_text())
errors=[]
for name,info in lock['files'].items():
 p=root/name
 if not p.is_file() or hashlib.sha256(p.read_bytes()).hexdigest()!=info['sha256']:errors.append(name)
for route in json.loads((root/'.agents/shared-routing.json').read_text())['families'].values():
 for name in route:
  if not (root/'.agents/skills'/name/'SKILL.md').is_file(): errors.append('Missing workflow '+name)
if errors:raise SystemExit('FAIL: '+', '.join(errors))
print(f"PASS: {len(lock['files'])} files match their pinned source bytes; all workflow families present")
