from typing import Dict


def to_pretty_str(d: Dict, initial_indent: int = 0, indent_multiple: int = None) -> str:
    if indent_multiple is None:
        indent_multiple = initial_indent

    ret_str = ''
    for key, val in d.items():
        ret_str += (' ' * initial_indent)
        ret_str += key + ': '
        if isinstance(val, dict):
            ret_str += '\n' + to_pretty_str(val, initial_indent + indent_multiple, indent_multiple)
        else:
            ret_str += str(val)
        ret_str += '\n'

    return ret_str[:-1]
