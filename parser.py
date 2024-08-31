# BNF y Logica de generacion de la tabla de simbolos
# Generar txt de tabla de simbolos
# parser.out -> se genera solo

from lexer import tokens  # Se importan los tokens generado previamente en el lexer
import ply.yacc as yacc  # analizador sintactico
from pathlib import Path
# 'var':['tipo','long','valor']
simbol_table = {}

precedence = (
    ('right', 'ASIGNACION'),
    ('right', 'IGUALI'),
    ('left', 'MAYORQ', 'MENORQ', 'MAYORI', 'MENORI'),
    ('left', 'MAS', 'MENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'A_PARENTESIS', 'C_PARENTESIS'),
)


def p_programa(p):
    '''programa : programa sentencia
                | sentencia
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_sentencia(p):
    '''sentencia : asignacion PUNTO_Y_COMA
                 | iteracion
                 | seleccion
                 | bloque_declaracion
                 | read PUNTO_Y_COMA
                 | write PUNTO_Y_COMA
    '''
    p[0] = p[1]


def p_read(p):
    '''read : READ A_PARENTESIS elemento C_PARENTESIS'''
    print(p[3])


def p_write(p):
    '''write : WRITE A_PARENTESIS elemento C_PARENTESIS'''
    print(p[3])


def p_bloque_declaracion(p):
    '''bloque_declaracion : INIT A_LLAVE declaraciones  C_LLAVE
    '''
    # p[0] = p[3]


def p_declaraciones(p):
    '''declaraciones : declaraciones declaracion
                     | declaracion
    '''
    # p[0] = p[1]


def p_declaracion(p):
    '''declaracion : lista_variables DOS_PUNTOS tipo_dato PUNTO_Y_COMA'''
    # p[0] = p[1]


def p_lista_variables(p):
    '''lista_variables : VARIABLE
                       | lista_variables COMA VARIABLE
    '''


def p_tipo_dato(p):
    '''tipo_dato : FLOAT
                 | INT
                 | STR
    '''
    p[0] = p[1]


def p_seleccion(p):
    '''seleccion : IF A_PARENTESIS condicion C_PARENTESIS bloque
                 | IF A_PARENTESIS condicion C_PARENTESIS bloque ELSE bloque
    '''
    if p[3]:
        p[0] = p[5]
    else:
        if len(p) == 8:
            p[0] = p[7]


def p_iteracion(p):
    '''iteracion : WHILE A_PARENTESIS condicion C_PARENTESIS bloque'''
    if p[3]:
        p[0] = p[6]


def p_condicion(p):
    '''condicion : comparacion OR comparacion
                 | comparacion AND comparacion
                 | NOT comparacion
                 | comparacion
    '''
    match len(p):
        case 4: p[0] = p[1] or p[3] if p[2] == 'or' else p[1] and p[3]
        case 3: p[0] = not bool(p[2])
        case _: p[0] = bool(p[1])


def p_comparacion(p):
    '''comparacion : expresion comparador expresion
                   | elemento
    '''
    if len(p) == 4:
        match p[2]:
            case '<=': p[0] = p[1] <= p[3]
            case '>=': p[0] = p[1] >= p[3]
            case '==': p[0] = p[1] == p[3]
            case '>': p[0] = p[1] > p[3]
            case '<': p[0] = p[1] < p[3]
    if len(p) == 2:
        p[0] = bool(p[1])


def p_comparador(p):
    '''comparador : MENORI
                  | MENORQ
                  | MAYORQ
                  | MAYORI
                  | IGUALI
                  | DISTINTOQ
     '''
    p[0] = p[1]


def p_bloque(p):
    '''bloque : A_LLAVE programa C_LLAVE'''
    p[0] = p[2]


def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION lista PUNTO_Y_COMA
                  | VARIABLE ASIGNACION expresion PUNTO_Y_COMA
                  | VARIABLE ASIGNACION condicion PUNTO_Y_COMA
    '''
    p[0] = p[3]


def p_suma_los_ultimos(p):
    '''suma_los_ultimos : SUMA_LOS_ULTIMOS  A_PARENTESIS N_ENTERO PUNTO_Y_COMA  lista  C_PARENTESIS
    '''
    lista = p[5]
    n = len(lista)-p[3]
    ultimos = lista[n:]
    p[0] = 0
    for num in ultimos:
        p[0] += num


def p_contar_binarios(p):
    ''''contar_binarios : CONTAR_BINARIOS A_PARENTESIS lista C_PARENTESIS '''


def p_lista(p):
    '''lista : A_CORCHETE elementos C_CORCHETE
             | A_CORCHETE C_CORCHETE
    '''
    if len(p) == 4:
        p[0] = p[2]
    if len(p) == 3:
        p[0] = []


def p_expresion_mas(p):
    'expresion : expresion MAS termino'
    p[0] = p[1] + p[3]


def p_expresion_menos(p):
    'expresion : expresion MENOS termino'
    p[0] = p[1] - p[3]


def p_expresion_termino(p):
    'expresion : termino'
    p[0] = p[1]


def p_termino_multiplicacion(p):
    'termino : termino MULTIPLICACION elemento'
    p[0] = p[1] * p[3]


def p_termino_division(p):
    'termino : termino DIVISION elemento'
    if type(p[1]) == str or type(p[3]) == str:
        print("no se pueden dividir cadenas")
    else:
        p[0] = p[1] / p[3]


def p_termino_elemento(p):
    'termino : elemento'
    p[0] = p[1]


def p_elemento_expresion(p):
    'elemento : A_PARENTESIS expresion C_PARENTESIS'
    p[0] = p[2]


def p_elementos(p):
    '''elementos : elementos COMA elemento
                 | elemento'''
    if len(p) == 4:
        p[0] = p[1] + [p[3]]
    else:
        p[0] = [p[1]]


def p_elemento(p):
    '''elemento : N_ENTERO
                | N_DECIMAL
                | N_BINARIO
                | VARIABLE
                | CADENA
                | sumar_los_ultimos
                | condicion
                | contar_binarios
    '''
    p[0] = p[1]

# Error rule for syntax errors


def p_error(p):
    print(f"Syntax error in linea {p.lineno} at value {p.value}")


# Build the parser
parser = yacc.yacc()
path = Path("./TESTS/parser_test.txt")
code = path.read_text()
result = parser.parse(code)
print(result)
