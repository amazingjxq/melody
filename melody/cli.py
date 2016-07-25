#!/usr/bin/env python
"""melody
Usage:
    melody render <markdown-file> [<listen-addr>] [--static-dir=<dir>]

"""
import docopt
import melody.core
import melody.svr

def main():
    args = docopt.docopt(__doc__, version='melody 0.1')

    if args['render']:
        melody.svr.run_server(args['<markdown-file>'],
                              args['--static-dir'])
