import sys
from antlr4 import *
from Take_AwayLexer import Take_AwayLexer
from Take_AwayParser import Take_AwayParser


class item:
    def __init__(self):
        self.domain_name = ''
        self.objects = ''
        self.type = ''

game = item()
game.domain_name = ''
game.objects = ''
game.type = ''

def main(argv):
    input = FileStream(argv[1])
    lexer = Take_AwayLexer(input)
    stream = CommonTokenStream(lexer)
    parser = Take_AwayParser(stream)
    tree = parser.domain()

    # domain解析

    # tree.NAME()
    # print(tree.NAME())                    #  n-take-away

    # domainName = parser.DomainContext.NAME(tree)
    # print(domainName)

    # game.domain_name=parser.DomainContext.NAME(tree)
    # print(game.domain_name)             # n-take-away

    # tree.getText()
    # print(tree.getText())                   #   解析出的pddl文本




    # type 解析

    parser.type()
    parser.typeDefine()
    parser.typeDeclaration()
    parser.TypeDeclarationContext
    parser.TYPE
    parser.TypeDefineContext
    parser.TypeContext

    # parser.type()
    # print(parser.type())            # []

    # parser.typeDefine()
    # print(parser.typeDefine())      # []

    # parser.typeDeclaration()
    # print(parser.typeDeclaration())     # []


    # parser.TypeContext
    # print(parser.TypeContext)           # <class ''>

    # parser.TypeDefineContext
    # print(parser.TypeDefineContext)     # <class ''>

    # parser.TYPE
    # print(parser.TYPE)          # 6

    # parser.TypeDeclarationContext
    # print(parser.TypeDeclarationContext)    #  <class ''>


    # tree.typeDefine()
    # print(tree.typeDefine())            #[73]

    # type = parser.type()
    # typeName = parser.TypeContext.NAME(type)
    # print(typeName)             # None

    # type = parser.type()
    # typeName = parser.TypeDeclarationContext.NAME(type)
    # print(typeName)             # None



    # Objects 解析

    parser.objectDefine()
    parser.objectDeclaration()
    parser.ObjectDeclarationContext
    parser.ObjectDefineContext
    parser.OBJECT

    # object = parser.objectDefine()
    # print(object)           # []
    # print(parser.objectDefine().getText())      # <EOF>

    # parser.objectDeclaration()
    # print(parser.objectDeclaration())   # []
    # print(parser.objectDeclaration().getText())     # <EOF>

    # parser.ObjectDeclarationContext
    # print(parser.ObjectDeclarationContext)  # <class ''>

    # parser.ObjectDefineContext
    # print(parser.ObjectDefineContext)       # <class ''>

    # parser.OBJECT
    # print(parser.OBJECT)            # 24


    # tree.objectDefine()
    # print(tree.objectDefine())        #[72]


if __name__ == '__main__':
    main(sys.argv)