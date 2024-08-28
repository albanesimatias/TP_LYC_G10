# BNF y Logica de generacion de la tabla de simbolos
# Generar txt de tabla de simbolos
# parser.out -> se genera solo

from lexer import tokens  # Se importan los tokens generado previamente en el lexer
import ply.yacc as yacc  # analizador sintactico

SYMBOL_TABLE = {}


def p_programa(p):
    '''programa : sentencia programa
                | sentencia
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_sentencia(p):
    '''sentencia : asignacion
                 | iteracion
                 | seleccion
                 | bloque_declaracion
                 | suma_los_ultimos
    '''
    p[0] = p[1]


def p_bloque_declaracion(p):
    '''bloque_declaracion : INIT A_LLAVE declaraciones  C_LLAVE
    '''
    p[0] = p[3]


def p_declaraciones(p):
    '''declaraciones : declaraciones declaracion
                     | declaracion
    '''
    # reveer logica
    p[0] = p[1]


def p_declaracion(p):
    '''declaracion : lista_variables DOS_PUNTOS tipo_dato'''
    p[0] = p[1]


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
        if len(p) >= 6:
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
    '''comparacion : elemento comparador elemento
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
                  | DISTONTOQ
     '''
    p[0] = p[1]


def p_bloque(p):
    '''bloque : A_LLAVE programa C_LLAVE'''
    p[0] = p[2]


def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION VARIABLE
                  | VARIABLE ASIGNACION N_ENTERO
                  | VARIABLE ASIGNACION N_DECIMAL
                  | VARIABLE ASIGNACION CADENA
                  | VARIABLE ASIGNACION N_BINARIO
                  | VARIABLE ASIGNACION lista
    '''
    p[0] = p[3]


def p_sumaLosUltimos(p):
    '''suma_los_ultimos : SUMA_LOS_ULTIMOS  A_PARENTESIS N_ENTERO PUNTO_Y_COMA  lista  C_PARENTESIS
    '''
    lista = p[5]
    n = len(lista)-p[3]
    ultimos = lista[n:]
    p[0] = 0
    for num in ultimos:
        p[0] += num


def p_lista(p):
    '''lista : A_CORCHETE elementos C_CORCHETE'''
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
    '''
    p[0] = p[1]

# Error rule for syntax errors


def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

while True:
    try:
        s = input('yacc > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    print(result)
