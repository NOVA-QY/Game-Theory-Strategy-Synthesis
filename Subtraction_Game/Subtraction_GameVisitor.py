# Generated from Subtraction_Game.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Subtraction_GameParser import Subtraction_GameParser
else:
    from Subtraction_GameParser import Subtraction_GameParser

# This class defines a complete generic visitor for a parse tree produced by Subtraction_GameParser.

class Subtraction_GameVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Subtraction_GameParser#domain.
    def visitDomain(self, ctx:Subtraction_GameParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#objectDefine.
    def visitObjectDefine(self, ctx:Subtraction_GameParser.ObjectDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#numericDefine.
    def visitNumericDefine(self, ctx:Subtraction_GameParser.NumericDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#numericSymbol.
    def visitNumericSymbol(self, ctx:Subtraction_GameParser.NumericSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#typeDefine.
    def visitTypeDefine(self, ctx:Subtraction_GameParser.TypeDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#terconditionDefine.
    def visitTerconditionDefine(self, ctx:Subtraction_GameParser.TerconditionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#predicateDefine.
    def visitPredicateDefine(self, ctx:Subtraction_GameParser.PredicateDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#atomFormSkeleton.
    def visitAtomFormSkeleton(self, ctx:Subtraction_GameParser.AtomFormSkeletonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#predicate.
    def visitPredicate(self, ctx:Subtraction_GameParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:Subtraction_GameParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#type.
    def visitType(self, ctx:Subtraction_GameParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#actionDefine.
    def visitActionDefine(self, ctx:Subtraction_GameParser.ActionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#actionSymbol.
    def visitActionSymbol(self, ctx:Subtraction_GameParser.ActionSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#emptyOrPreGD.
    def visitEmptyOrPreGD(self, ctx:Subtraction_GameParser.EmptyOrPreGDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#emptyOrEffect.
    def visitEmptyOrEffect(self, ctx:Subtraction_GameParser.EmptyOrEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#listName.
    def visitListName(self, ctx:Subtraction_GameParser.ListNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#listVariable.
    def visitListVariable(self, ctx:Subtraction_GameParser.ListVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#oneofDefine.
    def visitOneofDefine(self, ctx:Subtraction_GameParser.OneofDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#gd.
    def visitGd(self, ctx:Subtraction_GameParser.GdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#termAtomForm.
    def visitTermAtomForm(self, ctx:Subtraction_GameParser.TermAtomFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#termLiteral.
    def visitTermLiteral(self, ctx:Subtraction_GameParser.TermLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#constTerm.
    def visitConstTerm(self, ctx:Subtraction_GameParser.ConstTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#term.
    def visitTerm(self, ctx:Subtraction_GameParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#effect.
    def visitEffect(self, ctx:Subtraction_GameParser.EffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#assignop.
    def visitAssignop(self, ctx:Subtraction_GameParser.AssignopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#pEffect.
    def visitPEffect(self, ctx:Subtraction_GameParser.PEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#problemName.
    def visitProblemName(self, ctx:Subtraction_GameParser.ProblemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#domainName.
    def visitDomainName(self, ctx:Subtraction_GameParser.DomainNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#agentDefine.
    def visitAgentDefine(self, ctx:Subtraction_GameParser.AgentDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:Subtraction_GameParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#numericSetting.
    def visitNumericSetting(self, ctx:Subtraction_GameParser.NumericSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#init.
    def visitInit(self, ctx:Subtraction_GameParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Subtraction_GameParser#constTermAtomForm.
    def visitConstTermAtomForm(self, ctx:Subtraction_GameParser.ConstTermAtomFormContext):
        return self.visitChildren(ctx)



del Subtraction_GameParser