#!/usr/bin/env python3
import re
import sys
import os
import base64
from string import Template


def replace_base64(input: str) -> str:
    """Replaces tags <BASE64>...</BASE64> with base64 of its internals."""
    start_tag = "<BASE64>"
    end_tag = "</BASE64>"
    pattern = re.compile(f'{re.escape(start_tag)}(.*?){re.escape(end_tag)}', re.DOTALL)
    return pattern.sub(_replace_base64_match, input)


def _replace_base64_match(match):
    content = match.group(1)
    content = "\r\n".join(l.strip() for l in content.splitlines() if l.strip() != "")
    encoded = base64.b64encode(content.encode()).decode()
    return f'{encoded}'


def main():
    if len(sys.argv) != 2:
        print("Usage: render.py <template_file>", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1]) as template_file:
        template_text = str(template_file.read())
        template = Template(template_text)
        template_rendered = template.substitute(os.environ)
        result = replace_base64(template_rendered)
        print(result)

if __name__ == "__main__":
    main()