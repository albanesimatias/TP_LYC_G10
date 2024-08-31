from pathlib import Path

tabla_de_simbolos = {}


def guardar_en_tabla_de_simbolos(token):
    const_name = const_name = '_'+str(token.value)
    include = ['VARIABLE', 'CADENA', 'N_BINARIO', 'N_DECIMAL', 'N_ENTERO']
    if const_name not in tabla_de_simbolos and token.value not in tabla_de_simbolos and token.type in include:
        if token.type == 'VARIABLE':
            const_name = token.value
        tabla_de_simbolos[const_name] = {
            'tipo': None, 'valor': token.value, 'longitud': None}
        if token.type == 'CADENA':
            tabla_de_simbolos[const_name] = {
                'tipo': None, 'valor': token.value, 'longitud': len(token.value)}


def persistir_tabla_de_simbolos():
    path = Path('./tabla_de_simbolos.txt')
    text = f'NOMBRE {' '*14}TIPODATO {' '*12}VALOR{' '*15}LONGITUD \n'
    for key in tabla_de_simbolos.keys():
        entrada = tabla_de_simbolos[key]
        valor = entrada['valor'] or ''
        tipo = entrada['tipo'] or ''
        longitud = entrada['longitud'] or ''

        text += f'{key} {' '*(20-len(key))}{tipo or ''}{' '*(20-len(str(tipo)))} {
            valor}{' '*(20-len(str(valor)))}{longitud} \n'

    path.write_text(text)
