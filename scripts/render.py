#!/usr/bin/env python3
import re
import sys
import os
import base64
from string import Template


START, END = "<BASE64>", "</BASE64>"


def render(text: str) -> str:
    template = Template(text)
    template_rendered = template.substitute(os.environ)
    result = _replace_base64(template_rendered)
    return result


def _replace_base64(input: str) -> str:
    """Replaces tags <BASE64>...</BASE64> with base64 of its internals."""
    index = 0
    start_indexes = []
    result = []
    while index < len(input):
        if input.startswith(START, index):
            start_indexes.append(index)
        elif input.startswith(END, index):
            if len(start_indexes) == 1:
                data = input[start_indexes[0] + len(START) : index]
                data = ''.join(l.strip() for l in data.splitlines() if l != '')
                data = _replace_base64(data)
                data = base64.b64encode(data.encode()).decode()
                result = [
                    input[:start_indexes[0]],  # Before START
                    data,  # Between START and END
                    _replace_base64(input[index + len(END) :]),  # After END
                ]
                break
            start_indexes.pop()
        index += 1
    return ''.join(result) or input


def _main():
    if len(sys.argv) != 2:
        print("Usage: render.py <template_file>", file=sys.stderr)
        sys.exit(1)
    with open(sys.argv[1]) as template_file:
        template_text = str(template_file.read())
    result = render(template_text)
    print(result)


if __name__ == "__main__":
    _main()