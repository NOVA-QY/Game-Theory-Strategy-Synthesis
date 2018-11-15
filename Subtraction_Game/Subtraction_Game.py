import sys
from antlr4 import *
from Subtraction_GameLexer import Subtraction_GameLexer
from Subtraction_GameParser import Subtraction_GameParser


def main(argv):
    input = FileStream(argv[1])
    lexer = Subtraction_GameLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Subtraction_GameParser(stream)
    tree = parser.domain()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)