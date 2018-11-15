# Generated from Misernim.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MisernimParser import MisernimParser
else:
    from MisernimParser import MisernimParser

# This class defines a complete generic visitor for a parse tree produced by MisernimParser.

class MisernimVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MisernimParser#domain.
    def visitDomain(self, ctx:MisernimParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#objectDefine.
    def visitObjectDefine(self, ctx:MisernimParser.ObjectDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#numericDefine.
    def visitNumericDefine(self, ctx:MisernimParser.NumericDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#numericSymbol.
    def visitNumericSymbol(self, ctx:MisernimParser.NumericSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#typeDefine.
    def visitTypeDefine(self, ctx:MisernimParser.TypeDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#terconditionDefine.
    def visitTerconditionDefine(self, ctx:MisernimParser.TerconditionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#predicateDefine.
    def visitPredicateDefine(self, ctx:MisernimParser.PredicateDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#atomFormSkeleton.
    def visitAtomFormSkeleton(self, ctx:MisernimParser.AtomFormSkeletonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#predicate.
    def visitPredicate(self, ctx:MisernimParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:MisernimParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#type.
    def visitType(self, ctx:MisernimParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#actionDefine.
    def visitActionDefine(self, ctx:MisernimParser.ActionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#actionSymbol.
    def visitActionSymbol(self, ctx:MisernimParser.ActionSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#emptyOrPreGD.
    def visitEmptyOrPreGD(self, ctx:MisernimParser.EmptyOrPreGDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#emptyOrEffect.
    def visitEmptyOrEffect(self, ctx:MisernimParser.EmptyOrEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#listName.
    def visitListName(self, ctx:MisernimParser.ListNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#listVariable.
    def visitListVariable(self, ctx:MisernimParser.ListVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#oneofDefine.
    def visitOneofDefine(self, ctx:MisernimParser.OneofDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#gd.
    def visitGd(self, ctx:MisernimParser.GdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#termAtomForm.
    def visitTermAtomForm(self, ctx:MisernimParser.TermAtomFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#termLiteral.
    def visitTermLiteral(self, ctx:MisernimParser.TermLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#constTerm.
    def visitConstTerm(self, ctx:MisernimParser.ConstTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#term.
    def visitTerm(self, ctx:MisernimParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#effect.
    def visitEffect(self, ctx:MisernimParser.EffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#assignop.
    def visitAssignop(self, ctx:MisernimParser.AssignopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#pEffect.
    def visitPEffect(self, ctx:MisernimParser.PEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#problemName.
    def visitProblemName(self, ctx:MisernimParser.ProblemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#domainName.
    def visitDomainName(self, ctx:MisernimParser.DomainNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#agentDefine.
    def visitAgentDefine(self, ctx:MisernimParser.AgentDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:MisernimParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#numericSetting.
    def visitNumericSetting(self, ctx:MisernimParser.NumericSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#init.
    def visitInit(self, ctx:MisernimParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MisernimParser#constTermAtomForm.
    def visitConstTermAtomForm(self, ctx:MisernimParser.ConstTermAtomFormContext):
        return self.visitChildren(ctx)



del MisernimParser