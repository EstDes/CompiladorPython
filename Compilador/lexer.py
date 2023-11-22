import ply.lex as lex

# Tokens
tokens = (
    'INICIO',
    'FIN',
    'ID',
    'DIGITO',
    'DEFINIR',
    'COMO',
    'ESCRIBIR',
    'ENTERO',
    'REAL',
    'ASIGNACION',
    'SUMA',
    'RESTA',
    'MULTIPLICACION',
    'DIVISION',
    'MODULO',
    'PARENTESIS_IZQ',
    'PARENTESIS_DER',
    'PUNTO_Y_COMA',
    'CADENA',
)

# Expresiones regulares para los tokens
def t_INICIO(t):
    r'inicio'
    return t

def t_FIN(t):
    r'fin'
    return t

def t_DEFINIR(t):
    r'definir'
    return t

def t_COMO(t):
    r'como'
    return t

def t_ESCRIBIR(t):
    r'escribir'
    return t

def t_ENTERO(t):
    r'entero'
    return t

def t_REAL(t):
    r'real'
    return t

def t_ASIGNACION(t):
    r':='
    return t

def t_SUMA(t):
    r'\+'
    return t

def t_RESTA(t):
    r'-'
    return t

def t_MULTIPLICACION(t):
    r'\*'
    return t

def t_DIVISION(t):
    r'/'
    return t

def t_MODULO(t):
    r'%'
    return t

def t_PARENTESIS_IZQ(t):
    r'\('
    return t

def t_PARENTESIS_DER(t):
    r'\)'
    return t

def t_PUNTO_Y_COMA(t):
    r';'
    return t

def t_ID(t):
    r'[a-zA-Z]+'
    return t

def t_DIGITO(t):
    r'\d+(\.\d+)?'
    return t

def t_CADENA(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_espacio(t):
    r'\s+'
    pass

def t_error(t):
    print("Carácter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)

class Resul:
    def __init__(self):
        self.lexer = lex.lex()

    def tokenize(self, data):
        self.lexer.input(data)
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            tokens.append(tok.value)
        return tokens
    
class Lexer:
    def __init__(self):
        self.lexer = lex.lex()

    def tokenize(self, data):
        self.lexer.input(data)
        tokens = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            tokens.append(tok.type)
        return tokens

lexer = lex.lex()