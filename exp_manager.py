from utils import is_index, get_key, is_none


class ExpMagager:
    def __init__(self):
        self.exp_check = []

    def reiniciar(self):
        self.exp_check = []

    def validar_elemento(self, elemento, tabla_de_simbolos, line_error):
        if not is_index(elemento):
            key = get_key(elemento)
            tipo = tabla_de_simbolos[key]['tipo']
            if is_none(tipo):
                raise Exception(f'En la linea {line_error} la variable {elemento} no esta declarada')
            if tipo != self.exp_check[0]:
                self.exp_check[1] = False
                raise Exception(f'En la linea {line_error} se intento realizar una operacion con el tipo de dato {self.exp_check[0]} y {tipo}')

    def validar_tipo(self, tabla_de_simbolos, elemento, line_error):
        if len(self.exp_check) != 0:
            if self.exp_check[1]:
                self.validar_elemento(elemento, tabla_de_simbolos, line_error)

        else:
            tipo = tabla_de_simbolos[get_key(elemento)]['tipo']
            if is_none(tipo):
                raise Exception(f'Error en la linea {line_error} la variable {elemento} no esta declarada')
            self.exp_check.append(tipo)
            self.exp_check.append(True)

    def is_ok(self):
        return self.exp_check[1]
