class Terceto:
    def __init__(self, valor1, valor2, valor3):
        self.valor1 = valor1
        self.valor2 = valor2
        self.valor3 = valor3

    def actualizar_terceto(self, valor):
        if self.valor1 is None:
            self.valor1 = valor
        elif self.valor2 is None:
            self.valor2 = valor
        elif self.valor3 is None:
            self.valor3 = valor
        else:
            print("Terceto lleno\n")

    def modificar_terceto(self, indice, valor):
        match indice:
            case 1:
                self.valor1 = valor
            case 2:
                self.valor2 = valor
            case 3:
                self.valor3 = valor
            case _:
                print("Indice invalido\n")

    def __str__(self):
        return f'({self.valor1}, {self.valor2}, {self.valor3})'
