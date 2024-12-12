#!/usr/bin/env python

import sys

from tokenizer import tokenize

from parser import parse

from evaluator import evaluate

def main():
    environment = {}
    debug = False

    # Check for debug flag
    args = sys.argv[1:]
    if "--debug" in args:
        debug = True
        args.remove("--debug")

    if len(args) > 0:
        # Filename provided, read and execute it
        filename = args[0]
        with open(filename, 'r') as f:
            source_code = f.read()

        tokens = tokenize(source_code)
        if debug:
            print("Tokens:")
            for t in tokens:
                if t["tag"] is not None:
                    print(t)
            print()

        ast = parse(tokens)
        if debug:
            print("AST:")
            print(ast)
            print()

        evaluate(ast, environment)
    else:
        # REPL loop
        while True:
            try:
                source_code = input('>> ')

                # Exit condition for the REPL loop
                if source_code.strip() in ['exit', 'quit']:
                    break

                tokens = tokenize(source_code)
                if debug:
                    print("Tokens:")
                    for t in tokens:
                        if t["tag"] is not None:
                            print(t)
                    print()

                ast = parse(tokens)
                if debug:
                    print("AST:")
                    print(ast)
                    print()

                result, _ = evaluate(ast, environment)
                if result is not None:
                    print(result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
