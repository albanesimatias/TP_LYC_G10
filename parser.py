# BNF y Logica de generacion de la tabla de simbolos
# Generar txt de tabla de simbolos
# parser.out -> se genera solo

# Se importan los tokens generado previamente en el lexer
from lexer import tokens
import ply.yacc as yacc  # analizador sintactico
from pathlib import Path
from utils import tabla_de_simbolos, actualizar_en_tabla, persistir_tabla_de_simbolos, guardar_en_tabla_de_simbolos
from exp_manager import ExpMagager, get_key
from tercetos_manager import TercetosManager
from queue import LifoQueue
from i_token import Itoken

tm = TercetosManager()
auxCantElementos = 0
auxComparador = 0


diccionarioComparadores = {
    ">=":   "BLT",
    ">":   "BLE",
    "<=":   "BGT",
    "<":   "BGE",
    "<>":   "BEQ",
    "==":   "BNE"
}

diccionarioComparadoresNot = {
    ">=":   "BGE",
    ">":   "BGT",
    "<=":   "BLE",
    "<":   "BLT",
    "<>":   "BNE",
    "==":   "BEQ"
}

pilaComparadores = LifoQueue(0)
pilaCantComparadores = LifoQueue(0)
pilaVariables = LifoQueue(0)
banderaNot = False
exp_manager = ExpMagager()


def obtenerIndiceInt(variableString):
    aux = variableString[1]
    indice = 2
    while (indice < len(variableString)-1):
        aux = aux+variableString[indice]
        indice = indice+1
    return int(aux)


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
    '''read : READ A_PARENTESIS VARIABLE C_PARENTESIS'''
    print(f'READ ( VARIABLE ) -> read')
    exp_manager.reiniciar()
    p[0] = tm.crear_terceto('read', p[3], None)


def p_write(p):
    '''write : WRITE A_PARENTESIS elemento C_PARENTESIS'''
    print(f'WRITE ( elemento ) -> write')
    exp_manager.reiniciar()
    p[0] = tm.crear_terceto('write', p[3], None)


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
        print(f'declaracion -> declaraciones')


def p_declaracion(p):
    '''declaracion : lista_variables DOS_PUNTOS tipo_dato PUNTO_Y_COMA'''
    print(f'lista_variables : tipo_dato ; -> declaracion')
    lista_ids = p[1]
    tipo_dato = p[3]
    for id in lista_ids:
        if not actualizar_en_tabla(id, tipo_dato):
            raise Exception(f'Se intento declarar la variable "{id}" que ya estaba declarada')


def p_lista_variables(p):
    '''lista_variables : VARIABLE
                       | lista_variables COMA VARIABLE
    '''
    if len(p) == 4:
        print(f'lista_variables ; variable -> lista_variables')
        p[0] = p[1] + [p[3]]
    else:
        print('VARIABLE -> lista_variables')
        p[0] = [p[1]]


def p_tipo_dato(p):
    '''tipo_dato : FLOAT
                 | INT
                 | STR
                 | BIN
    '''
    print(f'{p.slice[1].type} -> tipo_dato')
    p[0] = p[1]


def p_seleccion(p):
    '''seleccion : IF A_PARENTESIS condicion C_PARENTESIS bloque
                 | IF A_PARENTESIS condicion C_PARENTESIS bloque bandera_else ELSE bloque
    '''
    if len(p) == 9:
        print('IF ( condicion ) bloque ELSE bloque -> seleccion')
        auxIndice = obtenerIndiceInt(p[6])
        tm.actualizar_terceto(int(auxIndice), f'[{tm.indice}]')
        p[0] = p[3]

    else:
        print('IF ( condicion ) bloque -> seleccion')
        auxCant = pilaCantComparadores.get()
        while (auxCant > 0):
            auxIndice = pilaComparadores.get()
            tm.actualizar_terceto(auxIndice, f'[{tm.indice}]')
            auxCant = auxCant-1
        p[0] = p[3]


def p_bandera_else(p):
    'bandera_else : '
    auxCant = pilaCantComparadores.get()
    p[0] = tm.crear_terceto("BI", None, None)
    auxIndice = 0
    while (auxCant > 0):
        auxIndice = pilaComparadores.get()
        tm.actualizar_terceto(auxIndice, f'[{tm.indice}]')
        auxCant = auxCant-1
    p[0] = f'[{p[0]}]'


def p_iteracion(p):
    '''iteracion : WHILE A_PARENTESIS condicion C_PARENTESIS bloque'''
    print(' WHILE ( condicion ) bloque -> iteracion')
    auxCant = pilaCantComparadores.get()
    p[0] = tm.crear_terceto("BI", None, None)
    auxIndice = 0
    if (auxCant == 2):
        auxIndice = pilaComparadores.get()
        tm.actualizar_terceto(auxIndice, f'[{tm.indice}]')
    auxIndice = pilaComparadores.get()
    tm.actualizar_terceto(auxIndice, f'[{tm.indice}]')
    tm.actualizar_terceto(p[0], auxIndice-1)
    p[0] = f'[{p[0]}]'


def p_condicion(p):
    '''condicion : comparacion bandera_or OR  comparacion
                 | comparacion AND comparacion
                 | NOT bandera_not comparacion
                 | comparacion
    '''
    if len(p) == 5:
        print(f'comparacion {p.slice[2].type} comparacion -> condicion')
        aux = int(p[2])
        tm.actualizar_terceto(aux, f'[{tm.indice}]')
        pilaCantComparadores.put(1)
        p[0] = p[1]

    if len(p) == 4:
        if (p[1] == 'not'):
            print('NOT comparacion -> condicion')
            pilaCantComparadores.put(1)
            p[0] = p[3]
            globals()['banderaNot'] = False
        else:
            print(f'comparacion {p.slice[2].type} comparacion -> condicion')
            pilaCantComparadores.put(2)
            p[0] = p[1]

    if len(p) == 2:
        print('comparacion -> condicion')
        pilaCantComparadores.put(1)
        p[0] = p[1]


def p_bandera_or(p):
    'bandera_or : '
    p[0] = tm.crear_terceto("BI", None, None)
    tm.actualizar_terceto(pilaComparadores.get(), f'[{tm.indice}]')


def p_bandera_not(p):
    'bandera_not : '
    globals()['banderaNot'] = True


def p_comparacion(p):  # < <= > >= ==
    '''comparacion : expresion  comparador expresion
    '''
    print('expresion comparador expresion -> comparacion')
    exp_manager.validar_tipo(tabla_de_simbolos, p[1], p[2])
    exp_manager.validar_tipo(tabla_de_simbolos, p[3], p[2])
    p[0] = f'[{tm.crear_terceto('CMP', p[1], p[3])}]'
    global auxComparador
    pilaComparadores.put(tm.crear_terceto(auxComparador, None, None))
    exp_manager.reiniciar()


def p_comparador(p):
    '''comparador : MENORI
                  | MENORQ
                  | MAYORQ
                  | MAYORI
                  | IGUALI
                  | DISTINTOQ
     '''
    print(f'{p.slice[1].type} -> comparador')

    global banderaNot
    if (banderaNot):
        globals()['auxComparador'] = diccionarioComparadoresNot.get(p[1])
    else:
        globals()['auxComparador'] = diccionarioComparadores.get(p[1])
    p[0] = p.lineno(1)


def p_bloque(p):
    '''bloque : A_LLAVE programa C_LLAVE'''
    print('{ programa } -> bloque')
    p[0] = p[1]


def p_asignacion(p):
    '''asignacion : VARIABLE ASIGNACION expresion
    '''
    print(f'VARIABLE ASIGNACION {p.slice[3].type} -> asignacion')
    exp_manager.validar_tipo(tabla_de_simbolos, p[3], p.lineno(2))
    if exp_manager.exp_check[0] != tabla_de_simbolos[p[1]]['tipo']:
        raise Exception(f'En la linea {p.lineno(2)} se intento asignar a {p[1]} el tipo de dato {exp_manager.exp_check[0]} y {p[1]} es de tipo {tabla_de_simbolos[p[1]]['tipo']}')
    exp_manager.reiniciar()
    p[0] = f'[{tm.crear_terceto('=', p[1], p[3])}]'


def p_sumar_los_ultimos(p):
    '''sumar_los_ultimos : SUMAR_LOS_ULTIMOS A_PARENTESIS N_ENTERO PUNTO_Y_COMA lista_ctes C_PARENTESIS
                         | SUMAR_LOS_ULTIMOS A_PARENTESIS MENOS N_ENTERO PUNTO_Y_COMA lista_ctes C_PARENTESIS
    '''
    print('SUMAR_LOS_ULTIMOS (N_ENTERO ; lista ) -> sumar_los_ultimos')
    suma = 0
    if len(p) == 7:
        lista = p[5]
        n_ultimos = int(p[3])
        if n_ultimos >= 1:
            ultimos = lista[n_ultimos-1:]
            for elem in ultimos:
                suma += elem
    tipo = 'N_DECIMAL' if isinstance(suma, float) else 'N_ENTERO'
    guardar_en_tabla_de_simbolos(Itoken(suma, tipo))
    p[0] = suma


def p_contar_binarios(p):
    '''contar_binarios : CONTAR_BINARIOS A_PARENTESIS lista C_PARENTESIS'''
    print('CONTAR_BINARIOS ( lista ) -> contar_binarios')
    cont = 0
    lista = p[3]
    for elemento in lista:
        key = get_key(elemento)
        if not tabla_de_simbolos[key]['tipo']:
            raise Exception(f'"{elemento}" no esta declarado en el bloque init')
        if tabla_de_simbolos[key]['tipo'] == 'bin':
            cont += 1
    guardar_en_tabla_de_simbolos(Itoken(cont, 'N_ENTERO'))
    p[0] = cont


def p_expresion_mas(p):
    'expresion : expresion MAS termino'
    print('expresion + termino -> expresion')
    exp_manager.validar_tipo(tabla_de_simbolos, p[1], p.lineno(2))
    exp_manager.validar_tipo(tabla_de_simbolos, p[3], p.lineno(2))
    p[0] = f'[{tm.crear_terceto('+', p[1], p[3])}]'


def p_expresion_menos_unario(p):
    'expresion : MENOS expresion %prec UMENOS'
    print('MENOS expresion %prec UMENOS -> expresion')
    exp_manager.validar_tipo(tabla_de_simbolos, p[2], p.lineno(1))
    p[0] = f'[{tm.crear_terceto('-', p[2], None)}]'


def p_expresion_menos(p):
    'expresion : expresion MENOS termino'
    print('expresion - termino -> expresion')
    exp_manager.validar_tipo(tabla_de_simbolos, p[1], p.lineno(2))
    exp_manager.validar_tipo(tabla_de_simbolos, p[3], p.lineno(2))
    p[0] = f'[{tm.crear_terceto('-', p[1], p[3])}]'


def p_expresion_termino(p):
    'expresion : termino'
    print('termino -> expresion')
    p[0] = p[1]


def p_termino_multiplicacion(p):
    'termino : termino MULTIPLICACION elemento'
    print('termino * elemento -> termino')
    exp_manager.validar_tipo(tabla_de_simbolos, p[1], p.lineno(2))
    exp_manager.validar_tipo(tabla_de_simbolos, p[3], p.lineno(2))
    p[0] = f'[{tm.crear_terceto('*', p[1], p[3])}]'


def p_termino_division(p):
    'termino : termino DIVISION elemento'
    print('termino / elemento -> termino')
    exp_manager.validar_tipo(tabla_de_simbolos, p[1], p.lineno(2))
    exp_manager.validar_tipo(tabla_de_simbolos, p[3], p.lineno(2))
    p[0] = f'[{tm.crear_terceto('/', p[1], p[3])}]'


def p_termino_elemento(p):
    'termino : elemento'
    print('elemento -> termino')
    p[0] = p[1]


def p_elemento_expresion(p):
    'elemento : A_PARENTESIS expresion C_PARENTESIS'
    print('( expresion ) -> elemento')
    p[0] = p[2]


def p_lista(p):
    '''lista : A_CORCHETE elementos C_CORCHETE
    '''
    print('[elementos] -> lista')
    p[0] = p[2]


def p_lista_ctes(p):
    '''lista_ctes : A_CORCHETE elementos_ctes C_CORCHETE
    '''
    print('[elementos_ctes] -> lista_ctes')
    p[0] = p[2]


def p_elementos_ctes(p):
    '''elementos_ctes : elementos_ctes COMA elemento_cte
                 | elemento_cte'''

    if len(p) == 4:
        print('elementos_ctes , elemento_cte -> elementos_ctes')
        p[0] = p[1] + [p[3]]
    else:
        print('elemento_cte -> elementos_ctes')
        p[0] = [p[1]]


def p_elementos(p):
    '''elementos : elementos COMA elemento
                 | elemento'''

    if len(p) == 4:
        print('elementos , elemento -> elementos')
        p[0] = p[1] + [p[3]]
    else:
        print('elemento -> elementos')
        p[0] = [p[1]]


def p_elemento(p):
    '''elemento : N_ENTERO
                | N_DECIMAL
                | N_BINARIO
                | VARIABLE
    '''
    print(f'{p.slice[1].type} -> elemento')
    p[0] = p[1]


def p_elemento_cadena(p):
    '''elemento : CADENA
    '''
    print(f'{p.slice[1].type} -> elemento')
    p[0] = p[1]


def p_elemento_funcion(p):
    '''elemento : sumar_los_ultimos
                | contar_binarios
    '''
    print(f'{p.slice[1].type} -> elemento')
    p[0] = p[1]


def p_elemento_cte(p):
    '''elemento_cte : N_ENTERO
                    | N_DECIMAL
    '''
    p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    raise Exception(f"Error en la linea {p.lineno or ''} at {p.value or ''}")


def ejecutar_parser():
    # Build the parser
    parser = yacc.yacc()
    path_parser = Path("./TESTS/parser_test.txt")
    code = path_parser.read_text()
    parser.parse(code)
    tm.print_tercetos()
    tm.guardar_tercetos_txt()
    persistir_tabla_de_simbolos()
