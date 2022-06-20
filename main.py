#!/usr/bin/env python3

import argparse
import json


def _readJson(filename: str, field: str) -> str:
    """
    read the requested json field and return it
    """
    obj = json.load(open(filename))
    print(f"GET {field}")
    cmd = f"obj{field}" 
    value = eval(cmd)
    return value


def _writeJson(filename: str, field: str, value: str):
    """
    write the requested field to the json file.
    """
    obj = json.load(open(filename))
    print(f"SET {field} = {value}")
    cmd = f"obj{field} = value" 
    exec(cmd)
    with (open(filename, "w")) as file:
        file.write(json.dumps(obj, indent = 2))



def main():
    """
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--action',    dest='action',    type=str,   required=True, choices=['read', 'write'], default='write')
    parser.add_argument('--filename',  dest='filename',  type=str,   required=True, default=None)
    parser.add_argument('--field',     dest='field',     type=str,   required=True, default=None)
    parser.add_argument('--value',     dest='value',     type=str,   required=False, default=None)
    
    args = parser.parse_args()

    if args.action == 'write':
        _writeJson(args.filename, args.field, args.value)
    else:
        val = _readJson(args.filename, args.field)
        print(f"::set-output name=value::{val}")


if __name__ == '__main__':
    main()

