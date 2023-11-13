#!/usr/bin/env python3

import argparse

class Pox:
    def __init__(self):
        pass

def runFile(f):
    run(f.read())

def runPrompt():
    while True:
        try:
            line = input("> ")
        except EOFError:
            break
        # import atexit

#def quit_gracefully():
#    print 'Bye'

#atexit.register(quit_gracefully)
 
        run(line)

def run(s):
    print(f"interpreted {s}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='pox tree-walk interpreter')
    parser.add_argument('source_file',
                        nargs='?',
                        type=argparse.FileType('r'),
                        help='a pox file to run')

    args = parser.parse_args()
    if args.source_file != None:
        runFile(args.source_file)
    else:
        runPrompt()

