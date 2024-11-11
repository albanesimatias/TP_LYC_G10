from pathlib import Path
import re


class Constantes:
    INT16_MIN = -32768
    INT16_MAX = 32767
    FLOAT32_MIN = -3.4e38
    FLOAT32_MAX = 3.4e38
    MAX_LEN_VAR = 20
    MAX_LEN_CAD = 40


conversion_tipos = {
    'N_BINARIO': 'bin',
    'N_ENTERO': 'int',
    'N_DECIMAL': 'float',
    'CADENA': 'str',
    'VARIABLE': None
}

tabla_de_simbolos = {}


def guardar_en_tabla_de_simbolos(token):
    t_value = str(token.value).replace('"', '')
    transform_key = {'VARIABLE': '', 'N_BINARIO': '_', 'N_DECIMAL': '_', 'N_ENTERO': '_', 'CADENA': '__'}
    include = ['VARIABLE', 'CADENA', 'N_BINARIO', 'N_DECIMAL', 'N_ENTERO']
    const_name = transform_key[token.type] + t_value

    if const_name not in tabla_de_simbolos and token.type in include:
        if token.type == 'VARIABLE':
            tabla_de_simbolos[const_name] = {'tipo': conversion_tipos[token.type], 'valor': None, 'longitud': None}
        if token.type == 'CADENA':
            const_name = const_name.replace(' ', '_')
            tabla_de_simbolos[const_name] = {
                'tipo': conversion_tipos[token.type], 'valor': t_value, 'longitud': len(t_value)}
        if token.type in ['N_DECIMAL', 'N_BINARIO', 'N_ENTERO']:
            tabla_de_simbolos[const_name] = {'tipo': conversion_tipos[token.type], 'valor': token.value, 'longitud': None}


def actualizar_en_tabla(id, tipo):
    if not tabla_de_simbolos[id]['tipo']:
        tabla_de_simbolos[id]['tipo'] = tipo
        return True
    return False


def persistir_tabla_de_simbolos():
    path = Path('./tabla_de_simbolos.txt')
    # Encabezado
    encabezado = f'{"NOMBRE":^20}|{"TIPODATO":^20}|{"VALOR":^20}|{"LONGITUD":^20}\n'
    separador = '-'*85 + '\n'

    # Inicializamos el texto con el encabezado y separador
    text = encabezado + separador

    for key in tabla_de_simbolos.keys():
        entrada = tabla_de_simbolos[key]
        nombre = key
        tipo = entrada['tipo'] or ''
        valor = entrada['valor'] or ''
        longitud = entrada['longitud'] or ''

        # Añadimos la entrada a la tabla con formato ajustado a 20 espacios por columna
        text += f'{nombre:^20}|{tipo:^20}|{valor:^20}|{longitud:^20}\n'
        text += separador

    path.write_text(text)


def is_index(elemento):
    cad = str(elemento)
    if '[' in cad:
        return True
    return False


def is_id(elemento):
    cad = str(elemento)
    regex = r'[a-zA-Z](\w|_)*'
    return re.match(regex, elemento)


def is_cad(elemento):
    cad = str(elemento)
    regex = r'"(\w|\s)*"'
    return re.match(regex, cad)


def is_bin(elemento):
    cad = str(elemento)
    regex = r'(0|1)+b'
    return re.match(regex, cad)


def get_key(elemento):
    if is_cad(elemento):
        elemento = str(elemento).replace('"', '')
        elemento = elemento.replace(' ', '_')
        return '__'+str(elemento)
    if is_bin(elemento):
        return '_'+str(elemento)
    if not is_id(str(elemento)):
        return '_'+str(elemento)
    return str(elemento)


def is_none(tipo):
    return tipo is None


def convertir_indice(indice):
    n = str(indice).replace('[', '')
    n = n.replace(']', '')
    return int(n)
