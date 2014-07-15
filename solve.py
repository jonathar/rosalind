from __future__ import print_function
import argparse
import sys
from rosalind import core


description = '''Solve challenges for Rosalind. Expects input data on stdin.'''


class PrintFunctions(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        for f in core.list_functions():
            print(f)


class ExecuteFunction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if values:
            try:
                fn = getattr(core, values)
                for line in sys.stdin:
                    print(fn(line))
            except AttributeError:
                sys.exit("Could not find target function '%s'" % values)


parser = argparse.ArgumentParser(description=description)
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('function', action=ExecuteFunction, nargs='?',
                   help='The function target to process input data.')
group.add_argument('-l', '--list', action=PrintFunctions, nargs='?',
                   default='', help='Lists available function targets')
args = parser.parse_args()
