from lexer import lexer
from parser import parser, persistir_tabla_de_simbolos, Path


def ejecutar_lexter():
    path_lexter = Path('./TESTS/lexer_test.txt')
    data = path_lexter.read_text()
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)


def ejecutar_parser():
    path_parser = Path("./TESTS/parser_test.txt")
    code = path_parser.read_text()
    parser.parse(code)
    persistir_tabla_de_simbolos()


# ejecutar_lexter()
ejecutar_parser()
