from pathlib import Path

tabla_de_simbolos = {}


def guardar_en_tabla_de_simbolos(token):
    t_value = str(token.value).replace('"', '')
    const_name = const_name = '_' + t_value
    include = ['VARIABLE', 'CADENA', 'N_BINARIO', 'N_DECIMAL', 'N_ENTERO']
    if const_name not in tabla_de_simbolos and token.value not in tabla_de_simbolos and token.type in include:
        if token.type == 'VARIABLE':
            const_name = token.value
        tabla_de_simbolos[const_name] = {
            'tipo': None, 'valor': t_value, 'longitud': None}
        if token.type == 'CADENA':
            tabla_de_simbolos[const_name] = {
                'tipo': None, 'valor': t_value, 'longitud': len(t_value)}


def persistir_tabla_de_simbolos():
    path = Path('./tabla_de_simbolos.txt')

    # Encabezado
    encabezado = f'{"NOMBRE":^20}|{"TIPODATO":^20}|{
        "VALOR":^20}|{"LONGITUD":^20}\n'
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
