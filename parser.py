# BNF y Logica de generacion de la tabla de simbolos
# Generar txt de tabla de simbolos
# parser.out -> se genera solo

# Se importan los tokens generado previamente en el lexer
from lexer import tokens
import ply.yacc as yacc  # analizador sintactico
from pathlib import Path
from utils import tabla_de_simbolos
from utils import persistir_tabla_de_simbolos
from tercetos_manager import TercetosManager

tm = TercetosManager()

precedence = (
    ('right', 'ASIGNACION'),
    ('right', 'IGUALI'),
    ('left', 'MAYORQ', 'MENORQ', 'MAYORI', 'MENORI'),
    ('left', 'MAS', 'MENOS'),
    ('right', 'UMENOS'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'A_PARENTESIS', 'C_PARENTESIS'),
)


def p_start(p):
    '''start : programa'''
    print('FIN')


def p_programa(p):
    '''programa : programa sentencia
                | sentencia
    '''
    if len(p) == 3:
        print(f'programa sentencia -> programa')
    else:
        print(f'sentencia -> programa')


def p_sentencia(p):
    '''sentencia : asignacion PUNTO_Y_COMA
                 | iteracion
                 | seleccion
                 | bloque_declaracion
                 | read PUNTO_Y_COMA
                 | write PUNTO_Y_COMA
    '''
    print(f'{p.slice[1].type} -> sentencia')


def p_read(p):
    '''read : READ A_PARENTESIS elemento C_PARENTESIS'''
    print(f'READ ( elemento ) -> read')


def p_write(p):
    '''write : WRITE A_PARENTESIS elemento C_PARENTESIS'''
    print(f'WRITE ( elemento ) -> write')


def p_bloque_declaracion(p):
    '''bloque_declaracion : INIT A_LLAVE declaraciones C_LLAVE
    '''
    print('INIT { declaraciones } -> bloque_declaracion')


def p_declaraciones(p):
    '''declaraciones : declaraciones declaracion
                     | declaracion
    '''
    if len(p) == 3:
        print(f'declaraciones declaracion -> declaraciones')
    else:
        print(f' declaracion -> declaraciones')


def p_declaracion(p):
    '''declaracion : lista_variables DOS_PUNTOS tipo_dato PUNTO_Y_COMA'''
    print(f' lista_variables : tipo_dato ; -> declaracion')


def p_lista_variables(p):
    '''lista_variables : VARIABLE
                       | lista_variables COMA VARIABLE
    '''
    if len(p) == 4:
        print(f'lista_variables ; variable -> lista_variables')
    else:
        print('VARIABLE -> lista_variables')


def p_tipo_dato(p):
    '''tipo_dato : FLOAT
                 | INT
                 | STR
                 | BIN
    '''
    print(f'{p.slice[1].type} -> tipo_dato')


def p_seleccion(p):
    '''seleccion : IF A_PARENTESIS condicion C_PARENTESIS bloque
                 | IF A_PARENTESIS condicion C_PARENTESIS bloque ELSE bloque
    '''
    if len(p) == 8:
        print('IF ( condicion ) bloque ELSE bloque -> seleccion')

    else:
        print('IF ( condicion ) bloque -> seleccion')


def p_iteracion(p):
    '''iteracion : WHILE A_PARENTESIS condicion C_PARENTESIS bloque'''
    print(' WHILE ( condicion ) bloque -> iteracion')


def p_condicion(p):
    '''condicion : comparacion OR comparacion
                 | comparacion AND comparacion
                 | NOT comparacion
                 | comparacion
    '''
    if len(p) == 4:
        print(f'comparacion {p.slice[2].type} comparacion -> condicion')
    if len(p) == 3:
        print('NOT comparacion -> condicion')
    if len(p) == 2:
        print('comparacion -> condicion')
        p[0] = p[1]


def p_comparacion(p):  # < <= > >= ==
    '''comparacion : expresion comparador expresion
                   | expresion
    '''
    # diccionario = {'<=':'BGE'}
    # crear_terceto(CMP,exp1,exp1)
    # aux=crear_terceto(BGE,None,None)
    # apilar(aux)
    if len(p) == 4:
        print('expresion comparador expresion -> comparacion')
    else:
        print('expresion -> comparacion')
        p[0] = p[1]


def p_comparador(p):
    '''comparador : MENORI
                  | MENORQ
                  | MAYORQ
                  | MAYORI
                  | IGUALI
                  | DISTINTOQ
     '''
    print(f'{p.slice[1].type} -> comparador')


def p_bloque(p):
    '''bloque : A_LLAVE programa C_LLAVE'''
    print('{ programa } -> bloque')


def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION lista
                  | VARIABLE ASIGNACION condicion
    '''
    print(f'VARIABLE ASIGNACION {p.slice[3].type} -> asignacion')
    p[0] = f'[{tm.crear_terceto('=', p[1], p[3])}]'


def p_sumar_los_ultimos(p):
    '''sumar_los_ultimos : SUMAR_LOS_ULTIMOS A_PARENTESIS N_ENTERO PUNTO_Y_COMA lista C_PARENTESIS
    '''
    print('SUMAR_LOS_ULTIMOS (N_ENTERO ; lista ) -> sumar_los_ultimos')
    lista = p[5]
    # cant = len(lista)
    # n_ultimos = p[3]
    # if (n_ultimos > cant and n_ultimos < 1):
    #    p[0] = f'[{tm.crear_terceto(0, None, None)}]'

    # ultimos = lista[n_ultimos-1::]
    # for elem in ultimos:


def p_contar_binarios(p):
    '''contar_binarios : CONTAR_BINARIOS A_PARENTESIS lista C_PARENTESIS'''
    print('CONTAR_BINARIOS ( lista ) -> contar_binarios')


def p_lista(p):
    '''lista : A_CORCHETE elementos C_CORCHETE
             | A_CORCHETE C_CORCHETE
    '''
    if len(p) == 4:
        print('[elementos] -> lista')
        p[0] = p[2]
    else:
        print('[] -> lista')
        p[0] = []


def p_expresion_mas(p):
    'expresion : expresion MAS termino'
    print('expresion + termino -> expresion')
    p[0] = f'[{tm.crear_terceto('+', p[1], p[3])}]'


def p_expresion_menos_unario(p):
    'expresion : MENOS expresion %prec UMENOS'
    print('MENOS expresion %prec UMENOS -> expresion')
    p[0] = f'[{tm.crear_terceto('-', p[2], None)}]'


def p_expresion_menos(p):
    'expresion : expresion MENOS termino'
    print('expresion - termino -> expresion')
    p[0] = f'[{tm.crear_terceto('-', p[1], p[3])}]'


def p_expresion_termino(p):
    'expresion : termino'
    print('termino -> expresion')
    p[0] = p[1]


def p_termino_multiplicacion(p):
    'termino : termino MULTIPLICACION elemento'
    print('termino * elemento -> termino')
    p[0] = f'[{tm.crear_terceto('*', p[1], p[3])}]'


def p_termino_division(p):
    'termino : termino DIVISION elemento'
    print('termino / elemento -> termino')
    p[0] = f'[{tm.crear_terceto('/', p[1], p[3])}]'


def p_termino_elemento(p):
    'termino : elemento'
    print('elemento -> termino')
    p[0] = p[1]


def p_elemento_expresion(p):
    'elemento : A_PARENTESIS expresion C_PARENTESIS'
    print('( expresion ) -> elemento')
    p[0] = p[2]


def p_elementos(p):
    '''elementos : elementos COMA elemento
                 | elemento'''

    if len(p) == 4:
        print('elementos , elemento -> elementos')
        if band_ultimos:
            p[0] = p[1] + [p[3]]
    else:
        print('elemento -> elementos')
        # p[0] = p[1]
        p[0] = [p[1]]


def p_elemento(p):
    '''elemento : N_ENTERO
                | N_DECIMAL
                | N_BINARIO
                | VARIABLE
                | CADENA
                | sumar_los_ultimos
                | contar_binarios
    '''
    print(f'{p.slice[1].type} -> elemento')
    p[0] = p[1]

# Error rule for syntax errors


def p_error(p):
    print(f"Error en la linea {p.lineno or ''} at {p.value or ''}")


# Build the parser
parser = yacc.yacc()
path_parser = Path("./TESTS/parser_test2.txt")
code = path_parser.read_text()
parser.parse(code)
tm.print_tercetos()
