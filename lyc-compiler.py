from lexer import lexer
from parser import parser, persistir_tabla_de_simbolos
from pathlib import Path


def ejecutar_lexter():
    path_lexter = Path('_internal\TESTS\lexer_test.txt')
    data = path_lexter.read_text()
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(f'TOKEN: {token.type} LEXEMA: {token.value}')


def ejecutar_parser():
    path_parser = Path("_internal\TESTS\parser_test.txt")
    code = path_parser.read_text()
    parser.parse(code)
    persistir_tabla_de_simbolos()


try:
    print(f'{'-'*10}COMIENZO TEST LEXER{'-'*10}')
    ejecutar_lexter()
    print(f'{'-'*10}FIN TEST LEXER{'-'*10}')
    print(f'\n\n{'-'*10}INICIO TEST PARSER{'-'*10}')
    ejecutar_parser()
    print(f'{'-'*10}FIN TEST PARSER{'-'*10}\n\n')
except Exception as e:
    print(f"Se ha producido un error: {e}")
finally:
    input("Presiona Enter para salir...")
