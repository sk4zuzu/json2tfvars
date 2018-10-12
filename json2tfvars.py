#!/usr/bin/env python

import sys
import argparse
import fileinput
import hcl, json
import functools, operator


def to_json(string, indent):
    return json.dumps(hcl.loads(string), indent=indent)


def to_tfvars(payload, indent):
    if not isinstance(payload, dict):
        return

    def recurse(item, level=0):
        if isinstance(item, dict):
            if level > 0:
                yield "{"

            for key, value in item.items():
                yield "\n"
                yield indent * level * " "
                yield "{} = ".format(key)

                for token in recurse(value, level=level+1):
                    yield token

            if level > 0:
                yield "\n"
                yield indent * (level-1) * " "
                yield "}"

        elif isinstance(item, list):
            if level > 0:
                yield "["

            for index, value in enumerate(item):
                yield "\n"
                yield indent * level * " "

                for token in recurse(value, level=level+1):
                    yield token

                if index < len(item)-1:
                    yield ","

            if level > 0:
                yield "\n"
                yield indent * (level-1) * " "
                yield "]"

        elif isinstance(item, bool):
            yield "true" if item else "false"

        else:
            yield "\"{}\"".format(item)

        if level-1 == 0:
            yield "\n"

    return functools.reduce(operator.add, recurse(payload), "")


def json2tfvars():
    parser, _ = functools.reduce(lambda (p, _), (args, kwargs): (p, p.add_argument(*args, **kwargs)), [
        (['--reverse'], {
            "dest": 'reverse',
            "action": 'store_true',
            "help": "expect tfvars (HCL) input",
        }),
        (['--indent'], {
            "dest": 'indent',
            "type": int,
            "metavar": "N",
            "default": 4,
            "help": "adjust identation levels",
        }),
        (['files'], {
            "nargs": '*',
            "metavar": "FILE",
        }),
    ], (argparse.ArgumentParser(), None))

    args = parser.parse_args()

    data = functools.reduce(operator.add, fileinput.input(
        files=(args.files if len(args.files) > 0 else ('-',))
    ), "")

    if args.reverse:
        print(to_json(data, indent=args.indent))
    else:
        print(to_tfvars(json.loads(data), indent=args.indent))


if __name__ == '__main__':
    json2tfvars()


# vim:ts=4:sw=4:et:syn=python:
