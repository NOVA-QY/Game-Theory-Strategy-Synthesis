import sys
from antlr4 import *
from MisernimLexer import MisernimLexer
from MisernimParser import MisernimParser


def main(argv):
    input = FileStream(argv[1])
    lexer = MisernimLexer(input)
    stream = CommonTokenStream(lexer)
    parser = MisernimParser(stream)
    tree = parser.domain()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)