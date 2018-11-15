# Generated from Take_Away.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Take_AwayParser import Take_AwayParser
else:
    from Take_AwayParser import Take_AwayParser

# This class defines a complete generic visitor for a parse tree produced by Take_AwayParser.

class Take_AwayVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Take_AwayParser#domain.
    def visitDomain(self, ctx:Take_AwayParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#objectDefine.
    def visitObjectDefine(self, ctx:Take_AwayParser.ObjectDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#numericDefine.
    def visitNumericDefine(self, ctx:Take_AwayParser.NumericDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#numericSymbol.
    def visitNumericSymbol(self, ctx:Take_AwayParser.NumericSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#typeDefine.
    def visitTypeDefine(self, ctx:Take_AwayParser.TypeDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#terconditionDefine.
    def visitTerconditionDefine(self, ctx:Take_AwayParser.TerconditionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#predicateDefine.
    def visitPredicateDefine(self, ctx:Take_AwayParser.PredicateDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#atomFormSkeleton.
    def visitAtomFormSkeleton(self, ctx:Take_AwayParser.AtomFormSkeletonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#predicate.
    def visitPredicate(self, ctx:Take_AwayParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:Take_AwayParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#type.
    def visitType(self, ctx:Take_AwayParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#actionDefine.
    def visitActionDefine(self, ctx:Take_AwayParser.ActionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#actionSymbol.
    def visitActionSymbol(self, ctx:Take_AwayParser.ActionSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#emptyOrPreGD.
    def visitEmptyOrPreGD(self, ctx:Take_AwayParser.EmptyOrPreGDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#emptyOrEffect.
    def visitEmptyOrEffect(self, ctx:Take_AwayParser.EmptyOrEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#listName.
    def visitListName(self, ctx:Take_AwayParser.ListNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#listVariable.
    def visitListVariable(self, ctx:Take_AwayParser.ListVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#oneofDefine.
    def visitOneofDefine(self, ctx:Take_AwayParser.OneofDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#gd.
    def visitGd(self, ctx:Take_AwayParser.GdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#termAtomForm.
    def visitTermAtomForm(self, ctx:Take_AwayParser.TermAtomFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#termLiteral.
    def visitTermLiteral(self, ctx:Take_AwayParser.TermLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#constTerm.
    def visitConstTerm(self, ctx:Take_AwayParser.ConstTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#term.
    def visitTerm(self, ctx:Take_AwayParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#effect.
    def visitEffect(self, ctx:Take_AwayParser.EffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#assignop.
    def visitAssignop(self, ctx:Take_AwayParser.AssignopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#pEffect.
    def visitPEffect(self, ctx:Take_AwayParser.PEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#problemName.
    def visitProblemName(self, ctx:Take_AwayParser.ProblemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#domainName.
    def visitDomainName(self, ctx:Take_AwayParser.DomainNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#agentDefine.
    def visitAgentDefine(self, ctx:Take_AwayParser.AgentDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:Take_AwayParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#numericSetting.
    def visitNumericSetting(self, ctx:Take_AwayParser.NumericSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#init.
    def visitInit(self, ctx:Take_AwayParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Take_AwayParser#constTermAtomForm.
    def visitConstTermAtomForm(self, ctx:Take_AwayParser.ConstTermAtomFormContext):
        return self.visitChildren(ctx)



del Take_AwayParser