#!/usr/bin/env python3
import sys
import os
import base64
from string import Template


def replace_base64(input: str) -> str:
    """Replaces tags <BASE64>...</BASE64> with base64 of its internals."""
    start_tag = "<BASE64>"
    end_tag = "</BASE64>"
    while True:
        start = input.find(start_tag)
        if start == -1:
            break
        end = input.find(end_tag, start)
        if end == -1:
            raise Exception("Missing end tag </BASE64>")
        content = input[start + len(start_tag):end]
        content = "\r\n".join(l.strip() for l in content.splitlines() if l.strip() != "")
        encoded = base64.b64encode(content.encode()).decode()
        input = input[:start] + encoded + input[end + len(end_tag):]
    return input


if len(sys.argv) != 2:
    print("Usage: render.py <template_file>", file=sys.stderr)
    sys.exit(1)


with open(sys.argv[1]) as template_file:
    template_text = str(template_file.read())
    template = Template(template_text)
    template_rendered = template.substitute(os.environ)
    result = replace_base64(template_rendered)
    print(result)