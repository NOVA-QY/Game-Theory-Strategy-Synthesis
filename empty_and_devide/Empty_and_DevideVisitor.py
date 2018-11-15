# Generated from Empty_and_Devide.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Empty_and_DevideParser import Empty_and_DevideParser
else:
    from Empty_and_DevideParser import Empty_and_DevideParser

# This class defines a complete generic visitor for a parse tree produced by Empty_and_DevideParser.

class Empty_and_DevideVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by Empty_and_DevideParser#domain.
    def visitDomain(self, ctx:Empty_and_DevideParser.DomainContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#objectDefine.
    def visitObjectDefine(self, ctx:Empty_and_DevideParser.ObjectDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#numericDefine.
    def visitNumericDefine(self, ctx:Empty_and_DevideParser.NumericDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#numericSymbol.
    def visitNumericSymbol(self, ctx:Empty_and_DevideParser.NumericSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#typeDefine.
    def visitTypeDefine(self, ctx:Empty_and_DevideParser.TypeDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#terconditionDefine.
    def visitTerconditionDefine(self, ctx:Empty_and_DevideParser.TerconditionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#predicateDefine.
    def visitPredicateDefine(self, ctx:Empty_and_DevideParser.PredicateDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#atomFormSkeleton.
    def visitAtomFormSkeleton(self, ctx:Empty_and_DevideParser.AtomFormSkeletonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#predicate.
    def visitPredicate(self, ctx:Empty_and_DevideParser.PredicateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#typeDeclaration.
    def visitTypeDeclaration(self, ctx:Empty_and_DevideParser.TypeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#type.
    def visitType(self, ctx:Empty_and_DevideParser.TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#actionDefine.
    def visitActionDefine(self, ctx:Empty_and_DevideParser.ActionDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#actionSymbol.
    def visitActionSymbol(self, ctx:Empty_and_DevideParser.ActionSymbolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#emptyOrPreGD.
    def visitEmptyOrPreGD(self, ctx:Empty_and_DevideParser.EmptyOrPreGDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#emptyOrEffect.
    def visitEmptyOrEffect(self, ctx:Empty_and_DevideParser.EmptyOrEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#listName.
    def visitListName(self, ctx:Empty_and_DevideParser.ListNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#listVariable.
    def visitListVariable(self, ctx:Empty_and_DevideParser.ListVariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#oneofDefine.
    def visitOneofDefine(self, ctx:Empty_and_DevideParser.OneofDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#gd.
    def visitGd(self, ctx:Empty_and_DevideParser.GdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#termAtomForm.
    def visitTermAtomForm(self, ctx:Empty_and_DevideParser.TermAtomFormContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#termLiteral.
    def visitTermLiteral(self, ctx:Empty_and_DevideParser.TermLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#constTerm.
    def visitConstTerm(self, ctx:Empty_and_DevideParser.ConstTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#term.
    def visitTerm(self, ctx:Empty_and_DevideParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#effect.
    def visitEffect(self, ctx:Empty_and_DevideParser.EffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#assignop.
    def visitAssignop(self, ctx:Empty_and_DevideParser.AssignopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#pEffect.
    def visitPEffect(self, ctx:Empty_and_DevideParser.PEffectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#problemName.
    def visitProblemName(self, ctx:Empty_and_DevideParser.ProblemNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#domainName.
    def visitDomainName(self, ctx:Empty_and_DevideParser.DomainNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#agentDefine.
    def visitAgentDefine(self, ctx:Empty_and_DevideParser.AgentDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:Empty_and_DevideParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#numericSetting.
    def visitNumericSetting(self, ctx:Empty_and_DevideParser.NumericSettingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#init.
    def visitInit(self, ctx:Empty_and_DevideParser.InitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by Empty_and_DevideParser#constTermAtomForm.
    def visitConstTermAtomForm(self, ctx:Empty_and_DevideParser.ConstTermAtomFormContext):
        return self.visitChildren(ctx)



del Empty_and_DevideParser