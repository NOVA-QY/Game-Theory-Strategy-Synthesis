import sys
from antlr4 import *
from Chomp_GameLexer import Chomp_GameLexer
from Chomp_GameParser import Chomp_GameParser


def main(argv):
    input = FileStream(argv[1])
    lexer = Chomp_GameLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Chomp_GameParser(stream)
    tree = parser.domain()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)