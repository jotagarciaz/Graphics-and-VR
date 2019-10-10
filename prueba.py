import re
import collections
from functools import wraps, partial

def debug_method(func= None, prefix = ''):
    if func is None:
        return partial(debug, prefix = prefix)
    else:
        msg = prefix + func.__name__
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(msg)
            return func(*args,**kwargs)
        return wrapper

def debug_class(cls):
    for key, val in vars(cls).items():
        if callable(val):
            setattr(cls, key, debug_method(val))
    return cls

separacion = 60

CONST = r'(?P<CONST>[a-z][A-Z]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
OR = r'(?P<OR>∨)'
AND = r'(?P<AND>∧)'
NOT = r'(?P<NOT>¬)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'
VERDADERO = r'(?P<VERDADERO>TRUE)'
FALSO = r'(?P<FALSO>FALSE)'

master_pattern = re.compile('|'.join((CONST, NUM, PLUS, MINUS, OR, AND, NOT,
                                      TIMES, DIVIDE, LPAREN, RPAREN, WS,
                                      VERDADERO, FALSO)))
Token = collections.namedtuple('Token', ['type', 'value'])


def lista_tokens(pattern, text):
    scanner = pattern.scanner(text)
    for m in iter(scanner.match, None):
        token = Token(m.lastgroup, m.group())

        if token.type != 'WS':
            yield token


print(list(lista_tokens(master_pattern, 'x ∨ y')))


class FormulaBooleana:
    '''
    Pequeña implementación de un parser de formulaesiones booleanas.
    Implementation of a recursive descent parser.
    Aquí la asignacion es un diccionario con variables.
    '''

    def parse(self, text, asig):
          self.tokens = lista_tokens(master_pattern, text)
          self.current_token = None
          self.next_token = None
          self._avanza()
          self.asig = asig
          return self.formula()

    def _avanza(self):
            self.current_token, self.next_token = self.next_token, next(
                self.tokens, None)

    def _acepta(self, token_type):
            # if there is next token and token type matches
            if self.next_token and self.next_token.type == token_type:
              self._avanza()
              return True
            else:
              return False

    def _espera(self, token_type):
            if not self._acepta(token_type):
              raise SyntaxError('Expected ' + token_type)

    def formula(self):
            '''
            formula : conjuncion | conjuncion ∨ formula
            '''
            formula_value = self.conjuncion()
            if self._acepta('OR'):
              formula_value = formula_value | self.formula()
            return formula_value

    def conjuncion(self):
            '''
            conjuncion : clausula | clausula ∧ conjuncion
            '''

            conj_value = self.clausula()
            if self._acepta('AND'):
              conj_value = conj_value & self.conjuncion()
            return conj_value

    def clausula(self):
            '''
            clausula : CONST | (formula)

            '''
            # Si aparece un parentesis
            if self._acepta('LPAREN'):
              formula_value = self.formula()
              self._espera('RPAREN')
              return formula_value
            elif self._acepta('CONST'):
              return self.asig[self.current_token.value]

class FormulaGeneral(FormulaBooleana):
    '''
    Pequeña implementación de un parser de formulaesiones booleanas.
    Implementation of a recursive descent parser.
    Aquí la asignacion es un diccionario con variables.
    '''
    
    def clausula(self):
        '''
        clausula:  ¬ CONST | ¬ (formula)
        
        '''
        if self._acepta('LPAREN'):
            formula_value = self.formula()
            self._espera('RPAREN')
            conj_value = formula_value
        elif self._acepta('CONST'):
            conj_value =  self.asig[self.current_token.value]
        if self._acepta('NOT'):
            formula_value = self.formula()
            conj_value = formula_value
            conj_value = not conj_value
        return conj_value


e = FormulaGeneral()
#print(e.parse('¬ x ∨ ¬(y ∧ x)',{'x':True , 'y':False}))

class FormulaDot(FormulaBooleana):

    def clausula(self):
        s = "hey"
        print(s)

e = FormulaDot()
#print(e.parse('¬ x ∨ ¬(y ∧ x)',{'x':True , 'y':False}))