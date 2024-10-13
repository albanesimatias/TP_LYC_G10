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


def get_key(elemento):
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

    def validar_tipo(self, tabla_de_simbolos, elemento, elemento2='[]'):
        if len(self.exp_check) != 0:
            if not self.exp_check[1]:
                return
            if is_index(elemento):
                if is_index(elemento2):
                    return
                else:
                    key = get_key(elemento2)
                    tipo = tabla_de_simbolos[key]['tipo']
                    if is_none(tipo):
                        raise Exception(f'La variable {elemento2} no esta declarado')
                    if tipo != self.exp_check[0]:
                        self.exp_check[1] = False
            elif is_index(elemento2):
                if is_index(elemento):
                    return
                else:
                    key = get_key(elemento)
                    tipo = tabla_de_simbolos[key]['tipo']
                    if is_none(tipo):
                        raise Exception(f'La variable {elemento} no esta declarado')
                    if tipo != self.exp_check[0]:
                        self.exp_check[1] = False
            else:
                key1 = get_key(elemento)
                key2 = get_key(elemento2)
                tipo = tabla_de_simbolos[key1]['tipo']
                tipo2 = tabla_de_simbolos[key2]['tipo']
                if is_none(tipo, tipo2):
                    raise Exception(f'La variable {elemento} o {elemento2} no esta declarado')
                valid_exp = tipo == self.exp_check[0] and tipo2 == self.exp_check[0]
                if not valid_exp:
                    self.exp_check[1] = False
        else:
            key1 = get_key(elemento)
            key2 = get_key(elemento2)
            tipo = tabla_de_simbolos[key1]['tipo']
            tipo2 = tabla_de_simbolos[key2]['tipo']
            if is_none(tipo, tipo2):
                raise Exception(f'La variable {elemento} o {elemento2} no esta declarado')
            valid_exp = tipo == tipo2
            self.exp_check.append(tipo)
            self.exp_check.append(valid_exp)

    def is_ok(self):
        return self.exp_check[1]
