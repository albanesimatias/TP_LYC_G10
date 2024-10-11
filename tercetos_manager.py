from terceto import Terceto


class TercetosManager:
    def __init__(self):
        self.lista = list()
        self.indice = int(0)

    def obtener_indice(self):
        return self.indice

    def crear_terceto(self, valor1, valor2, valor3):
        terceto_nuevo = Terceto(valor1, valor2, valor3)
        self.lista.append(terceto_nuevo)
        self.indice = self.indice + 1
        return self.indice - 1

    def insertar_terceto(self, terceto):
        self.lista.append(terceto)
        self.indice = self.indice + 1
        return self.indice - 1

    def actualizar_terceto(self, indice, valor):
        self.lista[indice].actualizar_terceto(valor)

    def print_tercetos(self):
        i = 0
        for terceto in self.lista:
            print(f'[{i}] {terceto}')
            i += 1
