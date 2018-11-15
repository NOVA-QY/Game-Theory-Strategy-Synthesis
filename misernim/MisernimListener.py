# Generated from Misernim.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MisernimParser import MisernimParser
else:
    from MisernimParser import MisernimParser

# This class defines a complete listener for a parse tree produced by MisernimParser.
class MisernimListener(ParseTreeListener):

    # Enter a parse tree produced by MisernimParser#domain.
    def enterDomain(self, ctx:MisernimParser.DomainContext):
        pass

    # Exit a parse tree produced by MisernimParser#domain.
    def exitDomain(self, ctx:MisernimParser.DomainContext):
        pass


    # Enter a parse tree produced by MisernimParser#objectDefine.
    def enterObjectDefine(self, ctx:MisernimParser.ObjectDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#objectDefine.
    def exitObjectDefine(self, ctx:MisernimParser.ObjectDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#numericDefine.
    def enterNumericDefine(self, ctx:MisernimParser.NumericDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#numericDefine.
    def exitNumericDefine(self, ctx:MisernimParser.NumericDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#numericSymbol.
    def enterNumericSymbol(self, ctx:MisernimParser.NumericSymbolContext):
        pass

    # Exit a parse tree produced by MisernimParser#numericSymbol.
    def exitNumericSymbol(self, ctx:MisernimParser.NumericSymbolContext):
        pass


    # Enter a parse tree produced by MisernimParser#typeDefine.
    def enterTypeDefine(self, ctx:MisernimParser.TypeDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#typeDefine.
    def exitTypeDefine(self, ctx:MisernimParser.TypeDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#terconditionDefine.
    def enterTerconditionDefine(self, ctx:MisernimParser.TerconditionDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#terconditionDefine.
    def exitTerconditionDefine(self, ctx:MisernimParser.TerconditionDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#predicateDefine.
    def enterPredicateDefine(self, ctx:MisernimParser.PredicateDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#predicateDefine.
    def exitPredicateDefine(self, ctx:MisernimParser.PredicateDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#atomFormSkeleton.
    def enterAtomFormSkeleton(self, ctx:MisernimParser.AtomFormSkeletonContext):
        pass

    # Exit a parse tree produced by MisernimParser#atomFormSkeleton.
    def exitAtomFormSkeleton(self, ctx:MisernimParser.AtomFormSkeletonContext):
        pass


    # Enter a parse tree produced by MisernimParser#predicate.
    def enterPredicate(self, ctx:MisernimParser.PredicateContext):
        pass

    # Exit a parse tree produced by MisernimParser#predicate.
    def exitPredicate(self, ctx:MisernimParser.PredicateContext):
        pass


    # Enter a parse tree produced by MisernimParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:MisernimParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by MisernimParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:MisernimParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by MisernimParser#type.
    def enterType(self, ctx:MisernimParser.TypeContext):
        pass

    # Exit a parse tree produced by MisernimParser#type.
    def exitType(self, ctx:MisernimParser.TypeContext):
        pass


    # Enter a parse tree produced by MisernimParser#actionDefine.
    def enterActionDefine(self, ctx:MisernimParser.ActionDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#actionDefine.
    def exitActionDefine(self, ctx:MisernimParser.ActionDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#actionSymbol.
    def enterActionSymbol(self, ctx:MisernimParser.ActionSymbolContext):
        pass

    # Exit a parse tree produced by MisernimParser#actionSymbol.
    def exitActionSymbol(self, ctx:MisernimParser.ActionSymbolContext):
        pass


    # Enter a parse tree produced by MisernimParser#emptyOrPreGD.
    def enterEmptyOrPreGD(self, ctx:MisernimParser.EmptyOrPreGDContext):
        pass

    # Exit a parse tree produced by MisernimParser#emptyOrPreGD.
    def exitEmptyOrPreGD(self, ctx:MisernimParser.EmptyOrPreGDContext):
        pass


    # Enter a parse tree produced by MisernimParser#emptyOrEffect.
    def enterEmptyOrEffect(self, ctx:MisernimParser.EmptyOrEffectContext):
        pass

    # Exit a parse tree produced by MisernimParser#emptyOrEffect.
    def exitEmptyOrEffect(self, ctx:MisernimParser.EmptyOrEffectContext):
        pass


    # Enter a parse tree produced by MisernimParser#listName.
    def enterListName(self, ctx:MisernimParser.ListNameContext):
        pass

    # Exit a parse tree produced by MisernimParser#listName.
    def exitListName(self, ctx:MisernimParser.ListNameContext):
        pass


    # Enter a parse tree produced by MisernimParser#listVariable.
    def enterListVariable(self, ctx:MisernimParser.ListVariableContext):
        pass

    # Exit a parse tree produced by MisernimParser#listVariable.
    def exitListVariable(self, ctx:MisernimParser.ListVariableContext):
        pass


    # Enter a parse tree produced by MisernimParser#oneofDefine.
    def enterOneofDefine(self, ctx:MisernimParser.OneofDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#oneofDefine.
    def exitOneofDefine(self, ctx:MisernimParser.OneofDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#gd.
    def enterGd(self, ctx:MisernimParser.GdContext):
        pass

    # Exit a parse tree produced by MisernimParser#gd.
    def exitGd(self, ctx:MisernimParser.GdContext):
        pass


    # Enter a parse tree produced by MisernimParser#termAtomForm.
    def enterTermAtomForm(self, ctx:MisernimParser.TermAtomFormContext):
        pass

    # Exit a parse tree produced by MisernimParser#termAtomForm.
    def exitTermAtomForm(self, ctx:MisernimParser.TermAtomFormContext):
        pass


    # Enter a parse tree produced by MisernimParser#termLiteral.
    def enterTermLiteral(self, ctx:MisernimParser.TermLiteralContext):
        pass

    # Exit a parse tree produced by MisernimParser#termLiteral.
    def exitTermLiteral(self, ctx:MisernimParser.TermLiteralContext):
        pass


    # Enter a parse tree produced by MisernimParser#constTerm.
    def enterConstTerm(self, ctx:MisernimParser.ConstTermContext):
        pass

    # Exit a parse tree produced by MisernimParser#constTerm.
    def exitConstTerm(self, ctx:MisernimParser.ConstTermContext):
        pass


    # Enter a parse tree produced by MisernimParser#term.
    def enterTerm(self, ctx:MisernimParser.TermContext):
        pass

    # Exit a parse tree produced by MisernimParser#term.
    def exitTerm(self, ctx:MisernimParser.TermContext):
        pass


    # Enter a parse tree produced by MisernimParser#effect.
    def enterEffect(self, ctx:MisernimParser.EffectContext):
        pass

    # Exit a parse tree produced by MisernimParser#effect.
    def exitEffect(self, ctx:MisernimParser.EffectContext):
        pass


    # Enter a parse tree produced by MisernimParser#assignop.
    def enterAssignop(self, ctx:MisernimParser.AssignopContext):
        pass

    # Exit a parse tree produced by MisernimParser#assignop.
    def exitAssignop(self, ctx:MisernimParser.AssignopContext):
        pass


    # Enter a parse tree produced by MisernimParser#pEffect.
    def enterPEffect(self, ctx:MisernimParser.PEffectContext):
        pass

    # Exit a parse tree produced by MisernimParser#pEffect.
    def exitPEffect(self, ctx:MisernimParser.PEffectContext):
        pass


    # Enter a parse tree produced by MisernimParser#problemName.
    def enterProblemName(self, ctx:MisernimParser.ProblemNameContext):
        pass

    # Exit a parse tree produced by MisernimParser#problemName.
    def exitProblemName(self, ctx:MisernimParser.ProblemNameContext):
        pass


    # Enter a parse tree produced by MisernimParser#domainName.
    def enterDomainName(self, ctx:MisernimParser.DomainNameContext):
        pass

    # Exit a parse tree produced by MisernimParser#domainName.
    def exitDomainName(self, ctx:MisernimParser.DomainNameContext):
        pass


    # Enter a parse tree produced by MisernimParser#agentDefine.
    def enterAgentDefine(self, ctx:MisernimParser.AgentDefineContext):
        pass

    # Exit a parse tree produced by MisernimParser#agentDefine.
    def exitAgentDefine(self, ctx:MisernimParser.AgentDefineContext):
        pass


    # Enter a parse tree produced by MisernimParser#objectDeclaration.
    def enterObjectDeclaration(self, ctx:MisernimParser.ObjectDeclarationContext):
        pass

    # Exit a parse tree produced by MisernimParser#objectDeclaration.
    def exitObjectDeclaration(self, ctx:MisernimParser.ObjectDeclarationContext):
        pass


    # Enter a parse tree produced by MisernimParser#numericSetting.
    def enterNumericSetting(self, ctx:MisernimParser.NumericSettingContext):
        pass

    # Exit a parse tree produced by MisernimParser#numericSetting.
    def exitNumericSetting(self, ctx:MisernimParser.NumericSettingContext):
        pass


    # Enter a parse tree produced by MisernimParser#init.
    def enterInit(self, ctx:MisernimParser.InitContext):
        pass

    # Exit a parse tree produced by MisernimParser#init.
    def exitInit(self, ctx:MisernimParser.InitContext):
        pass


    # Enter a parse tree produced by MisernimParser#constTermAtomForm.
    def enterConstTermAtomForm(self, ctx:MisernimParser.ConstTermAtomFormContext):
        pass

    # Exit a parse tree produced by MisernimParser#constTermAtomForm.
    def exitConstTermAtomForm(self, ctx:MisernimParser.ConstTermAtomFormContext):
        pass


