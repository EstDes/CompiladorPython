import ply.yacc as yacc
from lexer import tokens

class Parser:
    def __init__(self):
        self.parser = yacc.yacc()
        self.symbols = {}

    def parse(self, tokens):
        data = ' '.join(tokens)  # convierte la lista de tokens en una cadena
        return self.parser.parse(data, self.symbols)
    
class Symbol:
    def __init__(self, name, datatype):
        self.name = name
        self.datatype = datatype
        self.value = None  

symbol_table = {}

def p_programa(p):
    '''programa : INICIO instrucciones FIN'''
    p[0] = (p[2])

def p_instrucciones(p):
    '''instrucciones : instruccion
                     | instruccion instrucciones'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] is not None else []
    else:
        p[0] = [p[1]] + p[2] if p[1] is not None else p[2]

def p_instruccion(p):
    '''instruccion : definicion
                   | escritura
                   | asignacion'''
    p[0] = p[1]

def p_definicion(p):
    '''definicion : DEFINIR tdato COMO tipo_dato PUNTO_Y_COMA'''
    name = p[2]
    datatype = p[4]
    symbol = Symbol(name, datatype)
    symbol_table[name] = symbol
    p[0] = None
    
def p_asignacion(p):
    '''asignacion : tdato ASIGNACION expresion PUNTO_Y_COMA'''
    name = p[1]
    value = p[3]
    symbol = symbol_table[name]
    
    if symbol.datatype == "entero":
        if type(value) == int or (type(value) == float and value.is_integer()):
            symbol.value = value
        else:
            raise ValueError("Se esperaba un entero")
    elif symbol.datatype == "real":
        if type(value) == float and not value.is_integer():
            symbol.value = value
        else:
            raise ValueError("Se esperaba un número real")
    p[0] = None

def p_tdato(p):
    '''tdato : ID'''
    p[0] = p[1]

def p_tipo_dato(p):
    '''tipo_dato : ENTERO
                 | REAL'''
    p[0] = p[1]

def p_escritura(p):
    '''escritura : ESCRIBIR expresion PUNTO_Y_COMA'''
    p[0] = p[2]

def unir_cadenas(cadenas):
    if len(cadenas) == 1:
        return cadenas[0]
    cadena = ''
    for c in cadenas:
        if c.startswith('"') and c.endswith('"'):
            cadena += c[1:-1]
        else:
            cadena += c
    return cadena

def p_expresion(p):
    '''expresion : ID
                 | DIGITO 
                 | CADENA
                 | expresion SUMA expresion 
                 | expresion RESTA expresion 
                 | expresion MULTIPLICACION expresion 
                 | expresion DIVISION expresion 
                 | expresion MODULO expresion 
                 | PARENTESIS_IZQ expresion PARENTESIS_DER
                 | CADENA SUMA CADENA'''
    if len(p) == 2:
        if isinstance(p[1], str):
            if p[1][0] == '"' and p[1][-1] == '"':
                p[0] = p[1][1:-1] 
            elif p[1].isnumeric() or isfloat(p[1]):  
                p[0] = float(p[1])
            else:
                symbol = symbol_table.get(p[1])
                if symbol is None:
                    raise ValueError(f"La variable {p[1]} no está definida")
                if symbol.value is None:
                    raise ValueError(f"La variable {p[1]} no tiene valor asignado")
                p[0] = symbol.value
        else:
            p[0] = p[1]
    elif p[2] == '+':
        if isinstance(p[1], float) and isinstance(p[3], float):
            p[0] = float(p[1]) + float(p[3])
        else:
            if isinstance(p[1], str) or isinstance(p[3], str):
                p[0] = unir_cadenas([p[1], p[3]])
            else:
                raise ValueError("Operación no permitida")
    elif p[2] == '-':
        p[0] = float(p[1]) - float(p[3])
    elif p[2] == '*':
        p[0] = float(p[1]) * float(p[3])
    elif p[2] == '/':
        p[0] = float(p[1]) / float(p[3])
    elif p[2] == '%':
        p[0] = float(p[1]) % float(p[3])
    elif p[1] == '(' and p[3] == ')':
        p[0] = p[2]

def p_error(p):
    print("Error de sintaxis en '%s'" % p.type)

def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

# Instancia de la clase Parser
parser = Parser()