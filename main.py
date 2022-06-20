#!/usr/bin/env python3
import sys
import argparse
import json
"""
A script to read or write a json value.
I'm 99% sure this would be easier in nodejs.
But, since I'm not much of a JS coder, I wrote it in the quickest language I knew.
"""


def _readJson(filename: str, fields) -> str:
    """
    read the requested json field and return it
    """
    obj = json.load(open(filename))
    path = _listToEvalPath(fields)
    print(f"GET {fields} == {path}")
    cmd = f"obj{path}" 
    value = eval(cmd)
    return value


def _writeJson(filename: str, fields, value: str):
    """
    write the requested field to the json file.
    """
    file = open(filename, "r")
    obj = json.load(file)
    file.close()

    _validateDict(obj, fields)
    
    path = _listToEvalPath(fields)
    cmd = f"obj{path} = value" 
    print(f"SET {cmd}")
    exec(cmd)

    file = open(filename, "w")
    file.write(json.dumps(obj, indent = 2))
    file.flush()
    file.close()
    
def _validateDict(obj, fields):
    """
    simply recursively ensure each field is in the obj
    """
    if len(fields) > 1:
        field = fields[0]
        if field not in obj or not isinstance(obj[field], dict):
            obj[field] = {}
        return _validateDict(obj[field], fields[1:])
    else:
        return obj

def _fieldToList(field: str):
    """
    Convert a dot-notation sequence, into a named dict reference.
    eg.  "user.address.zip" == ['user']['address']['zip']
    Doesn't yet handle arrays
    """
    return field.split('.')

def _listToEvalPath(fields):
    """
    Convert a list to the dict eval string
    ['root', 'name', 'first'] --> ['root']['name']['first']
    """
    path = ""
    for f in fields:
        path += f"['{f}']"
    return path


def main():
    """
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--action',    dest='action',    type=str,   required=True,  choices=['read', 'write'], default='write')
    parser.add_argument('--filename',  dest='filename',  type=str,   required=True,  default=None)
    parser.add_argument('--field',     dest='field',     type=str,   required=True,  default=None)
    parser.add_argument('--value',     dest='value',     type=str,   required=False, default='')
    
    args = parser.parse_args()

    fields = _fieldToList(args.field)

    if args.action == 'write':
        _writeJson(args.filename, fields, args.value)
    else:
        val = _readJson(args.filename, fields)
        print(f"::set-output name=value::{val}")

if __name__ == '__main__':
    main()

