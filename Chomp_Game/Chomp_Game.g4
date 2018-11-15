grammar Chomp_Game;

/*
 * Parser Rules
 */

// Domain description
domain: LB DEFINE LB DOMAIN NAME RB
           objectDefine
           typeDefine
           terconditionDefine
           actionDefine*
        RB;

objectDefine: LB COLON OBJS listVariable RB;
numericDefine: LB COLON NUMS numericSymbol+ RB;
numericSymbol: NAME;
typeDefine: LB COLON TYPE NORMAL RB |
            LB COLON TYPE MISER RB;
terconditionDefine: LB COLON TERCONDITION emptyOrPreGD RB;

predicateDefine: LB COLON PREDICATE atomFormSkeleton+ RB;
atomFormSkeleton: LB predicate listVariable oneofDefine? RB;
predicate: NAME;

typeDeclaration: NAME | LB NAME constTerm constTerm RB;

type: OBJECT | AGENT | NAME;
//interval: LSB constTerm constTerm RSB;

actionDefine: LB COLON ACTION actionSymbol
                 (COLON PARAMETER LB listVariable RB)?
                (COLON PRECONDITION emptyOrPreGD)?
                (COLON EFFECT emptyOrEffect)?
              RB;
actionSymbol: NAME;


emptyOrPreGD: gd | LB RB;
emptyOrEffect: effect | LB RB;

listName: NAME* | NAME+ MINUS type listName;
listVariable: VAR* | VAR+ MINUS type listVariable;
oneofDefine: ONEOF VAR+;

gd: termAtomForm
  | LB AND gd+ RB
  | LB OR gd+ RB
  | LB NOT gd RB
  | LB IMPLY gd gd RB
  | LB EXISTS LB listVariable RB gd RB
  | LB FORALL LB listVariable RB gd RB;

termAtomForm: LB predicate term* RB
            | LB EQ term term RB
            | LB NEQ term term RB
            | LB LT term term RB
            | LB LEQ term term RB
            | LB GT term term RB
            | LB GEQ term term RB;
termLiteral: termAtomForm | LB NOT termAtomForm RB;

constTerm: NAME
         | INTEGER
         | LB MINUS constTerm RB
         | LB MINUS constTerm constTerm RB   
         | LB PLUS constTerm constTerm RB;

term: NAME
    | VAR
    | INTEGER
    | LB MINUS term RB
    | LB MINUS term term RB
    | LB PLUS term term RB;

effect: LB AND pEffect+ RB
      | pEffect;
assignop: INC | DEC | ASSGIN;
pEffect: LB assignop VAR term RB;
          

problemName: NAME;
domainName: NAME;
agentDefine: LB COLON AGENT NAME+ RB;
objectDeclaration: LB COLON OBJS listName RB;
numericSetting: LB COLON NUMS (LB numericSymbol INTEGER RB)+
              RB;


init: LB COLON INIT constTermAtomForm* RB;
/*constTermGd: constTermAtomForm
           | constTermLiteral
           | LB AND constTermGd+ RB
           | LB OR constTermGd+ RB
           | LB NOT constTermGd RB
           | LB IMPLY constTermGd constTermGd RB
           | LB EXISTS LB listVariable RB gd RB
           | LB FORALL LB listVariable RB gd RB;*/

constTermAtomForm: LB predicate constTerm* RB
                 | LB EQ constTerm constTerm RB
                 | LB LT constTerm constTerm RB
                 | LB LEQ constTerm constTerm RB
                 | LB GT constTerm constTerm RB
                 | LB GEQ constTerm constTerm RB;
/*constTermLiteral: constTermAtomForm | LB NOT constTermAtomForm RB;*/

/*
 * Lexer Rules
 */

// Keywords
DOMAIN: 'domain';
PROBLEM: 'problem';
DEFINE: 'define';
AGENTID: 'agentid';
CONST: 'constants';
TYPE: 'type';
PREDICATE: 'predicates';
ACTION: 'action';
EVENT: 'event';
EVENTS: 'events';
PLDEGREE: 'pldegree';
EVENTMODEL: 'eventmodel';
PARAMETER: 'parameters';
TERCONDITION: 'tercondition';
PRECONDITION: 'precondition';
RESPONSE: 'response';
OBSERVATION: 'observation';
MIN: 'min';
MAX: 'max';
NUMS: 'numbers';
NORMAL:'normal';
MISER: 'miser';
EFFECT: 'effect';
OBJECT: 'object';
INC: 'increase';
DEC: 'decrease';
ASSGIN: 'assign';
AGENT: 'agent';
EITHER: 'either';

OBJS: 'objects';

INIT: 'init';
GOAL: 'goal';

// Common used in domain and problem
LB: '(';
RB: ')';
LSB: '[';
RSB: ']';
COLON: ':';
QM: '?';
POINT: '.';
UL: '_';
MINUS: '-';
PLUS: '+';
MULT: '*';
DIV: '/';
EQ: '=';
NEQ: '!=';
LT: '<';
LEQ: '<=';
GT: '>';
GEQ: '>=';
AND: 'and';
OR: 'or';
NOT: 'not';
ONEOF: 'oneof';
IMPLY: 'imply';
FORALL: 'forall';
EXISTS: 'exists';
WHEN: 'when';

NAME: LETTER CHAR*;
INTEGER: DIGIT+;


fragment LETTER: [a-zA-Z];
fragment DIGIT: [0-9];
fragment CHAR: LETTER | DIGIT | MINUS | UL;


//NUMBER: 
//DECIMAL: POINT DIGIT+;
VAR: QM NAME;
FUNSYM : NAME;

WS: [ \t\r\n]+ -> channel(HIDDEN);