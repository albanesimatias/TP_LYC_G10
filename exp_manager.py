import re


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


def get_key(elemento):
    if is_cad(elemento):
        elemento = str(elemento).replace('"', '')
        return '_'+str(elemento)
    if not is_id(str(elemento)):
        return '_'+str(elemento)
    return str(elemento)


def is_none(tipo, tipo2=False):
    return tipo is None or tipo2 is None


class ExpMagager:
    def __init__(self):
        self.exp_check = []

    def reiniciar(self):
        self.exp_check = []

    def validar_elemento(self, elemento, tabla_de_simbolos):
        if not is_index(elemento):
            key = get_key(elemento)
            tipo = tabla_de_simbolos[key]['tipo']
            if is_none(tipo):
                raise Exception(f'La variable {elemento} no esta declarado')
            if tipo != self.exp_check[0]:
                self.exp_check[1] = False

    def validar_tipo(self, tabla_de_simbolos, elemento, elemento2='[]'):
        if len(self.exp_check) != 0:
            if self.exp_check[1]:
                self.validar_elemento(elemento, tabla_de_simbolos)
                self.validar_elemento(elemento2, tabla_de_simbolos)
        else:
            tipo = tabla_de_simbolos[get_key(elemento)]['tipo']
            tipo2 = tabla_de_simbolos[get_key(elemento2)]['tipo']
            if is_none(tipo, tipo2):
                raise Exception(f'La variable {elemento} o {elemento2} no esta declarado')
            valid_exp = tipo == tipo2
            self.exp_check.append(tipo)
            self.exp_check.append(valid_exp)

    def is_ok(self):
        return self.exp_check[1]
