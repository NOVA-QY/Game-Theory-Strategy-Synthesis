# Generated from Chomp_Game.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Chomp_GameParser import Chomp_GameParser
else:
    from Chomp_GameParser import Chomp_GameParser

# This class defines a complete generic visitor for a parse tree produced by Chomp_GameParser.

class Chomp_GameVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Chomp_GameParser#domain.
    def visitDomain(self, ctx:Chomp_GameParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#objectDefine.
    def visitObjectDefine(self, ctx:Chomp_GameParser.ObjectDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#numericDefine.
    def visitNumericDefine(self, ctx:Chomp_GameParser.NumericDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#numericSymbol.
    def visitNumericSymbol(self, ctx:Chomp_GameParser.NumericSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#typeDefine.
    def visitTypeDefine(self, ctx:Chomp_GameParser.TypeDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#terconditionDefine.
    def visitTerconditionDefine(self, ctx:Chomp_GameParser.TerconditionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#predicateDefine.
    def visitPredicateDefine(self, ctx:Chomp_GameParser.PredicateDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#atomFormSkeleton.
    def visitAtomFormSkeleton(self, ctx:Chomp_GameParser.AtomFormSkeletonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#predicate.
    def visitPredicate(self, ctx:Chomp_GameParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:Chomp_GameParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#type.
    def visitType(self, ctx:Chomp_GameParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#actionDefine.
    def visitActionDefine(self, ctx:Chomp_GameParser.ActionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#actionSymbol.
    def visitActionSymbol(self, ctx:Chomp_GameParser.ActionSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#emptyOrPreGD.
    def visitEmptyOrPreGD(self, ctx:Chomp_GameParser.EmptyOrPreGDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#emptyOrEffect.
    def visitEmptyOrEffect(self, ctx:Chomp_GameParser.EmptyOrEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#listName.
    def visitListName(self, ctx:Chomp_GameParser.ListNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#listVariable.
    def visitListVariable(self, ctx:Chomp_GameParser.ListVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#oneofDefine.
    def visitOneofDefine(self, ctx:Chomp_GameParser.OneofDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#gd.
    def visitGd(self, ctx:Chomp_GameParser.GdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#termAtomForm.
    def visitTermAtomForm(self, ctx:Chomp_GameParser.TermAtomFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#termLiteral.
    def visitTermLiteral(self, ctx:Chomp_GameParser.TermLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#constTerm.
    def visitConstTerm(self, ctx:Chomp_GameParser.ConstTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#term.
    def visitTerm(self, ctx:Chomp_GameParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#effect.
    def visitEffect(self, ctx:Chomp_GameParser.EffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#assignop.
    def visitAssignop(self, ctx:Chomp_GameParser.AssignopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#pEffect.
    def visitPEffect(self, ctx:Chomp_GameParser.PEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#problemName.
    def visitProblemName(self, ctx:Chomp_GameParser.ProblemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#domainName.
    def visitDomainName(self, ctx:Chomp_GameParser.DomainNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#agentDefine.
    def visitAgentDefine(self, ctx:Chomp_GameParser.AgentDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:Chomp_GameParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#numericSetting.
    def visitNumericSetting(self, ctx:Chomp_GameParser.NumericSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#init.
    def visitInit(self, ctx:Chomp_GameParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Chomp_GameParser#constTermAtomForm.
    def visitConstTermAtomForm(self, ctx:Chomp_GameParser.ConstTermAtomFormContext):
        return self.visitChildren(ctx)



del Chomp_GameParser