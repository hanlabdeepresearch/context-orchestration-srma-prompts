#!/usr/bin/env python3
"""Verify the published Markdown against recorded original prompt SHA-256 values.

This is an archive consistency check, not a reconstruction or execution of the
research workflow. Exactly one terminal LF may be restored for explicitly
labelled TERMINAL_NEWLINE_ONLY display records. No other normalization is used.
Run from a repository clone: python validation/verify_published_prompts.py
"""
from __future__ import annotations
import csv
import hashlib
import re
import sys
from pathlib import Path


def check(root: Path) -> tuple[list[str], list[str]]:
    failures: list[str] = []
    display_notes: list[str] = []
    index = root / 'prompt_index.csv'
    if not index.is_file():
        return ['prompt_index.csv is missing'], []
    with index.open(encoding='utf-8-sig', newline='') as handle:
        rows = list(csv.DictReader(handle))
    if len(rows) != 55 or len({r['Prompt_ID'] for r in rows}) != 55:
        failures.append('Expected 55 unique preserved prompt occurrence IDs')
    for row in rows:
        pid = row['Prompt_ID']
        path_part, _, anchor = row['Prompt_Page'].partition('#')
        path = (root / path_part).resolve()
        if not path.is_relative_to(root.resolve()) or not path.is_file():
            failures.append(f'{pid}: missing or unsafe Markdown path')
            continue
        text = path.read_text(encoding='utf-8')
        heading = re.search(r'^#{1,2} ' + re.escape(pid) + r'\s*$', text, re.M)
        if not heading:
            failures.append(f'{pid}: heading not found')
            continue
        section = re.split(r'\n<a id=|\n#{1,2} D[123]-[UP]\d+', text[heading.end():], maxsplit=1)[0]
        block = re.search(r'```text\n(.*?)\n```', section, re.S)
        if not block:
            failures.append(f'{pid}: prompt code block not found')
            continue
        value = block.group(1)
        digest = hashlib.sha256(value.encode('utf-8')).hexdigest()
        status = row['Display_Check']
        if digest == row['Original_SHA256']:
            if status != 'EXACT':
                failures.append(f'{pid}: index display status needs updating')
            continue
        restored = hashlib.sha256((value + '\n').encode('utf-8')).hexdigest()
        if status == 'TERMINAL_NEWLINE_ONLY' and restored == row['Original_SHA256']:
            display_notes.append(f'{pid}: original has one additional terminal LF')
        else:
            failures.append(f'{pid}: prompt content does not match original SHA-256')
    mapping = root / 'output_prompt_map.csv'
    if not mapping.is_file():
        failures.append('output_prompt_map.csv is missing')
    else:
        with mapping.open(encoding='utf-8-sig', newline='') as handle:
            outputs = list(csv.DictReader(handle))
        if {r['Output_ID'] for r in outputs} != {f'{n:02}' for n in range(1, 33)}:
            failures.append('Output IDs must cover 01 through 32')
        valid_ids = {r['Prompt_ID'] for r in rows}
        for out in outputs:
            for field in ['Core_Prompts', 'Supporting_Prompts', 'Other_Recorded_Prompts']:
                for pid in [p.strip() for p in out[field].split(';') if p.strip()]:
                    if pid not in valid_ids:
                        failures.append(f"Output {out['Output_ID']}: unknown prompt {pid}")
    return failures, display_notes


def main() -> int:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    failures, notes = check(root)
    for note in notes:
        print('DISPLAY NOTE:', note)
    for failure in failures:
        print('FAIL:', failure)
    if failures:
        print(f'FAILED: {len(failures)} issue(s)')
        return 1
    print(f'PASS: 55 prompt occurrences; 32 output mappings; {len(notes)} documented terminal-LF display differences')
    print('This does not authenticate original platform logs or validate the research results.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
