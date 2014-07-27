#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Generates a DOT file using a remote BigML json pml tree model as input.

"""

import sys
import argparse

from bigml.api import BigML
from bigml.fields import Fields


def write_tree(model, out=sys.stdout):
    """Prints a json pml `model` to `out` in dot format.

    """
    out.write('digraph g {\n')
    root = model['object']['model']['root']
    fields = Fields(model['object']['model']['fields'])
    write_root(root, fields, out)
    out.write('}')
    out.flush()


def write_root(root, fields, out):
    """Recursively prints a node and children in dot format.

    """
    if 'children' in root and root['children']:
        for child in root['children']:
            out.write('%s -> %s [label="%s %s"];\n' % (
                      root['id'], child['id'],
                      child['predicate']['operator'],
                      child['predicate']['value']))
            write_root(child, fields, out)
        out.write('%s [label=<<B>%s</B>>, style="filled"];\n' % (
                  root['id'], fields.field_name(child['predicate']['field'])))
        out.flush()
    else:
        out.write('%s [style="bold", label="%s"];\n' % (
                  root['id'], root['output']))
        out.flush()


def main(args=sys.argv[1:]):
    """Parses command-line parameters and calls the actual main function.

    """
    # Process arguments
    parser = argparse.ArgumentParser(
        description="JSON PML to DOT",
        epilog="BigML, Inc")

    # Model
    parser.add_argument('--model',
                        type=str,
                        required=True,
                        action='store',
                        dest='model',
                        default=None,
                        help="Model identifier")

    # Output file
    parser.add_argument('--output',
                        type=str,
                        action='store',
                        dest='output',
                        default=None,
                        help="Output file")

    # Parse args
    args = parser.parse_args(args)

    # Instantiate BigML API
    api = BigML()

    model = api.get_model(args.model)
    api.ok(model)

    if args.output:
        output = open(args.output, 'w')
        write_tree(model, output)
        output.close()
    else:
        write_tree(model)

if __name__ == "__main__":
    main()
