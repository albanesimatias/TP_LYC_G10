import ply.lex as lex
from pathlib import Path
from utils import guardar_en_tabla_de_simbolos

# 'var':['tipo','long','valor']
# tabla_de_simbolos = {}

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'init': 'INIT',
    'float': 'FLOAT',
    'int': 'INT',
    'str': 'STR',
    'read': 'READ',
    'write': 'WRITE',
    'or': 'OR',
    'and': 'AND',
    'not': 'NOT',
    'suma_los_ultimos': 'SUMA_LOS_ULTIMOS',
}

tokens = [
    'A_PARENTESIS',
    'C_PARENTESIS',
    'A_LLAVE',
    'C_LLAVE',
    'A_CORCHETE',
    'C_CORCHETE',
    'ASIGNACION',
    'N_ENTERO',
    'N_DECIMAL',
    'N_BINARIO',
    'CADENA',
    'VARIABLE',
    'MENORI',
    'DISTINTOQ',
    'MAYORI',
    'IGUALI',
    'MENORQ',
    'MAYORQ',
    'MAS',
    'MENOS',
    'DIVISION',
    'MULTIPLICACION',
    'COMA',
    'PUNTO_Y_COMA',
    'DOS_PUNTOS'
] + list(reserved.values())


# Expresiones regulares para TOKENS simples
t_MENORI = r'\<\='
t_MAYORI = r'\>\='
t_IGUALI = r'\=\='
t_DISTINTOQ = r'!='
t_MENORQ = r'\<'
t_MAYORQ = r'\>'
t_MAS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_A_PARENTESIS = r'\('
t_C_PARENTESIS = r'\)'
t_A_LLAVE = r'\{'
t_C_LLAVE = r'\}'
t_A_CORCHETE = r'\['
t_C_CORCHETE = r'\]'
t_ASIGNACION = r'='
t_COMA = r','
t_PUNTO_Y_COMA = r';'
t_DOS_PUNTOS = r':'


# Expresiones regulares con codigo de accion (validaciones/errores/ignorar)
def t_COMENTARIO(t):
    r'\*-.*-\*'
    pass


def t_VARIABLE(t):
    r'[a-zA-Z](\w|_|-)*'
    t.type = reserved.get(t.value, 'VARIABLE')
    return t


def t_CADENA(t):
    r'"[^"]*"'
    # guardar_en_tabla_de_simbolos("VARIABLE", "hola", tabla_de_simbolos)
    if len(t.value) > 40:
        raise Exception('La cadena exed el limite de caracteres (MAX_40)')
    return t


def t_N_BINARIO(t):
    r'(0|1)+b'
    return t


def t_N_DECIMAL(t):
    r'-?\d+\.\d+'
    if len(t.value) > 10:
        raise Exception('Limite de 32bits para numeros decimales')
    t.value = float(t.value)
    return t


def t_N_ENTERO(t):
    r'-?\d+'
    if len(t.value) > 5:
        raise Exception('Limite de 16bits para numeros enteros')
    t.value = int(t.value)
    return t


# Regla que cuenta la cantidad de lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Ignorar tabulaciones y espacios
t_ignore = ' \t'

# Manejo de errores


def t_error(t):
    print(f"Illegal character {t.value[0]} at line: {t.lexer.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# path = Path('./TESTS/test_01.txt')
# data = path.read_text()
# lexer.input('hola var "cadena" 1 1.5')
# print(tabla_de_simbolos)
# guardar_en_tabla_de_simbolos("VARIABLE", "hola", tabla_de_simbolos)
# print(tabla_de_simbolos)
# while True:
#     token = lexer.token()
#     if not token:
#         break
#     print(token)
