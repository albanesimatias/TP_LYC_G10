from pathlib import Path
from terceto import Terceto
from utils import *
import re
lista_prioridades = [[]]

diccionarioComparadoresAssembler = {
    "BLT":   "JB",
    "BLE":   "JBE",
    "BGT":   "JA",
    "BGE":   "JAE",
    "BEQ":   "JE",
    "BNE":   "JNE",
    "BI":   "JMP"
}


class AssemblerBuilder:
    def init(self, tercetos: list, assembler):
        self.tercetos = tercetos
        self.assembler = list()

    def traducirTercetosAAssembler(self):
        i = 0
        i_max = len(self.tercetos)
        while (i < i_max):
            self.traducir_terceto(self.tercetos[i])
            i += 1

    def traducir_terceto(self, terceto):
        aux = terceto.valor1()

        match aux:
            case '+':
                self.traducir_suma(terceto)
            case '-':
                self.traducir_resta(terceto)
            case '*':
                self.traducir_multiplicacion(terceto)
            case '/':
                self.traducir_division(terceto)
            case '=':
                self.traducir_asignacion(terceto)
            case 'write':
                self.traducir_write(terceto)
            case 'read':
                self.traducir_read(terceto)
            case 'salto':
                self.traducir_salto(terceto)

    def traducir_operacion_intermedia(self, terceto: Terceto):
        operacion = ''
        if not is_index(terceto.valor2):
            cmd = 'FILD' if tabla_de_simbolos[get_key(terceto.valor2)].tipo == 'int' else 'FLD'
            operacion += f'{cmd} {get_key(terceto.valor2)}\n'
        if not is_index(terceto.valor3) and not terceto.valor3 is None:
            cmd = 'FILD' if tabla_de_simbolos[get_key(terceto.valor3)].tipo == 'int' else 'FLD'
            operacion += f'{cmd} {get_key(terceto.valor3)}\n'
        if not is_index(terceto.valor2) and is_index(terceto.valor3):
            operacion += f'FXCH\n'
        if is_index(terceto.valor2) and is_index(terceto.valor3):
            if convertir_indice(terceto.valor2) > convertir_indice(terceto.valor3):
                operacion += f'FXCH\n'
        if terceto.valor3 is None:
            operacion += f'FCHS\n'
        return operacion

    def traducir_suma(self, terceto: Terceto):
        operacion = self.traducir_operacion_intermedia(terceto)
        operacion += f'FADD\n'
        self.assembler.append(operacion)

    def traducir_resta(self, terceto: Terceto):
        operacion = self.traducir_operacion_intermedia(terceto)
        operacion += f'FSUB\n'
        self.assembler.append(operacion)

    def traducir_multiplicacion(self, terceto: Terceto):
        operacion = self.traducir_operacion_intermedia(terceto)
        operacion += f'FMUL\n'
        self.assembler.append(operacion)

    def traducir_division(self, terceto: Terceto):
        operacion = self.traducir_operacion_intermedia(terceto)
        if terceto.valor3 == 0:
            raise Exception('No se puede dividir por 0')
        operacion += f'FDIV\n'
        self.assembler.append(operacion)

    def traducir_asignacion(self, terceto: Terceto):
        # = id cte_str
        # = id id
        # = id []
        operacion = ''
        if is_index(terceto.valor3):
            operacion += f'FSTP {terceto.valor2}'

    def traducir_write(terceto):
        pass

    def traducir_read(terceto):
        pass

    def traducir_salto(terceto):
        pass

    # def traducirTercetoAAssembler2(terceto):
    #    aux = terceto.getValor3()
    #    if (aux is None):
    #        traducirNoOperacion(terceto)
    #    else:
    #        traducirOperacion(terceto)
    # def traducirOperacion(terceto):
    #    pass
