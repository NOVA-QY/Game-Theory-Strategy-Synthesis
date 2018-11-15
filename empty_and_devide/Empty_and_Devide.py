import sys
from antlr4 import *
from Empty_and_DevideLexer import Empty_and_DevideLexer
from Empty_and_DevideParser import Empty_and_DevideParser


def main(argv):
    input = FileStream(argv[1])
    lexer = Empty_and_DevideLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Empty_and_DevideParser(stream)
    tree = parser.domain()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)