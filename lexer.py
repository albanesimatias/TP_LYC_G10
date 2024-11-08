import ply.lex as lex
from pathlib import Path
from utils import guardar_en_tabla_de_simbolos, Constantes
import re

reserved = {
    'if': 'IF',
    'else': 'ELSE',
    'while': 'WHILE',
    'init': 'INIT',
    'float': 'FLOAT',
    'int': 'INT',
    'str': 'STR',
    'bin': 'BIN',
    'read': 'READ',
    'write': 'WRITE',
    'or': 'OR',
    'and': 'AND',
    'not': 'NOT',
    'sumar_los_ultimos': 'SUMAR_LOS_ULTIMOS',
    'contar_binarios': 'CONTAR_BINARIOS'
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
    r'\*\-.*?\-\*'
    pass


def t_VARIABLE(t):
    r'[a-zA-Z](\w|_)*'
    t.type = reserved.get(t.value, 'VARIABLE')
    if len(t.value) > Constantes.MAX_LEN_VAR:
        print(f'La variable exede el tamaño de {Constantes.MAX_LEN_VAR} caracteres')
        t.type = 'ERROR'
    else:
        if t.type == 'VARIABLE':
            guardar_en_tabla_de_simbolos(t)
        return t


def t_CADENA(t):
    r'"(\w|\s)*"'
    if len(t.value) > Constantes.MAX_LEN_CAD:
        print(f'La cadena exede el limite de {Constantes.MAX_LEN_CAD} caracteres')
    else:
        guardar_en_tabla_de_simbolos(t)
        return t


def t_N_BINARIO(t):
    r'(0|1)+b'
    guardar_en_tabla_de_simbolos(t)
    return t


def t_N_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    if t.value <= Constantes.FLOAT32_MAX:
        guardar_en_tabla_de_simbolos(t)
        return t
    print('Limite de 32bits para numeros decimales')


def t_N_ENTERO(t):
    r'\d+'
    t.value = int(t.value)
    if t.value <= Constantes.INT16_MAX:
        guardar_en_tabla_de_simbolos(t)
        return t
    print('Limite de 16bits para numeros enteros')


# Regla que cuenta la cantidad de lineas
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# Ignorar tabulaciones y espacios
t_ignore = ' \t'

# Manejo de errores


def t_error(t):
    print(f"Caracter invalido '{t.value[0]}' en la linea: {t.lexer.lineno}")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex(reflags=re.DOTALL)


def ejecutar_lexer():
    path_lexter = Path('./TESTS/lexer_test.txt')
    data = path_lexter.read_text()
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(f'TOKEN: {token.type} LEXEMA: {token.value}')
