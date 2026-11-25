#!/usr/bin/env python3
"""Generate the public case catalog from curated data and the English Menu."""

import argparse
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
CURATED_DATA = ROOT / 'data/gpt-6-2-sol-usecase-curated.json'
CATALOG = ROOT / 'docs/usecase-catalog.md'


def cell(value):
    return value.replace('|', r'\|').replace('\n', ' ')


def render_catalog():
    data = json.loads(CURATED_DATA.read_text(encoding='utf-8'))
    cases = {case['number']: case for case in data['cases']}
    readme = (ROOT / 'README.md').read_text(encoding='utf-8')
    _, menu_anchor, after_menu = readme.partition('<a id="menu"></a>')
    menu = re.split(r'^## ', after_menu, maxsplit=2, flags=re.M)[1] if menu_anchor else ''
    order = [int(number) for number in re.findall(r'^\| \[[^\n]+?\]\(#case-(\d+)\) \|', menu, re.M)]

    if len(order) != len(cases) or set(order) != set(cases) or len(cases) != data['total_cases']:
        raise ValueError('The English Menu and curated data must list the same cases once each.')

    lines = [
        '# GPT-6.2 Sol case catalog',
        '',
        f'{len(cases)} source-backed cases, newest first. The [README](../README.md) contains the case notes and media.',
        '',
        '| Case | Date | Type | Original source |',
        '| --- | --- | --- | --- |',
    ]
    for number in order:
        case = cases[number]
        title = cell(case['title'])
        lines.append(
            f"| [{title}](../README.md#case-{number}) | {case['date']} | {case['type']} "
            f"| [Source]({case['source_url']}) |"
        )
    return '\n'.join(lines) + '\n'


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='Check that the catalog matches the source files.')
    args = parser.parse_args()
    expected = render_catalog()
    if args.check:
        if not CATALOG.is_file() or CATALOG.read_text(encoding='utf-8') != expected:
            parser.exit(1, 'Case catalog is stale. Run python3 scripts/build_case_index.py.\n')
        print('Case catalog matches the English Menu and curated data.')
    else:
        CATALOG.write_text(expected, encoding='utf-8')


if __name__ == '__main__':
    main()
