from pathlib import Path
from terceto import Terceto
from utils import *
import re

etiquetas = set()

diccionario_comparadores = {
    "BLT":   "JB",
    "BLE":   "JBE",
    "BGT":   "JA",
    "BGE":   "JAE",
    "BEQ":   "JE",
    "BNE":   "JNE",
    "BI":   "JMP"
}


class AssemblerBuilder:
    def __init__(self, tercetos: list):
        self.tercetos = tercetos
        self.assembler = list()

    def traducir_tercetos(self):
        i = 0
        i_max = len(self.tercetos)
        while (i < i_max):
            self.traducir_terceto(self.tercetos[i])
            i += 1
        for etiqueta in etiquetas:
            operacion = f'ETIQ_{etiqueta}:\n'
            self.assembler[etiqueta] = operacion + self.assembler[etiqueta]
        self.crear_data()
        self.crear_end()

    def traducir_terceto(self, terceto: Terceto):
        aux = terceto.valor1

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
            case 'CMP':
                self.traducir_CMP(terceto)
            case 'FIN':
                self.assembler.append('')
            case _:
                self.traducir_salto(terceto)

    def traducir_operacion_intermedia(self, terceto: Terceto):
        operacion = ''
        if not is_index(terceto.valor2):
            cmd = 'FILD' if tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'int' else 'FLD'
            operacion += f'{cmd} {get_key(terceto.valor2)}\n'
        if not is_index(terceto.valor3) and not terceto.valor3 is None:
            cmd = 'FILD' if tabla_de_simbolos[get_key(terceto.valor3)]['tipo'] == 'int' else 'FLD'
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
        operacion = ''
        cmd = ''
        if tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'int':
            if not is_index(terceto.valor3):
                cmd = f'FILD {get_key(terceto.valor3)}\n'
            cmd += 'FISTP'
            operacion += f'{cmd} {get_key(terceto.valor2)}\n'
            self.assembler.append(operacion)
        elif tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'float':
            if not is_index(terceto.valor3):
                cmd = f'FLD {get_key(terceto.valor3)}\n'
            cmd += 'FSTP'
            operacion += f'{cmd} {get_key(terceto.valor2)}\n'
            self.assembler.append(operacion)
        else:
            operacion = f'lea ax, {get_key(terceto.valor3)}\n'
            operacion += f'mov {terceto.valor2}, ax\n'
            self.assembler.append(operacion)

    def traducir_write(self, terceto: Terceto):
        operacion = ''
        operacion += 'CALL '
        if not is_index(terceto.valor2) and not terceto.valor2 is None:
            if tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'int':
                cmd = 'DisplayInteger'
            elif tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'float':
                cmd = 'DisplayFloat'
            else:
                cmd = 'displayString'
        operacion += f'{cmd} {get_key(terceto.valor2)}\n'
        self.assembler.append(operacion)

    def traducir_read(self, terceto: Terceto):
        operacion = ''
        operacion += 'CALL '
        if not is_index(terceto.valor2) and not terceto.valor2 is None:
            if tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'int':
                cmd = 'GetInteger'
            elif tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'float':
                cmd = 'GetFloat'
            else:
                cmd = 'getString'
            operacion += f'{cmd} {get_key(terceto.valor2)}\n'
        self.assembler.append(operacion)

    def traducir_CMP(self, terceto: Terceto):
        operacion = ''
        if not is_index(terceto.valor3):
            cmd = 'FILD' if tabla_de_simbolos[get_key(terceto.valor3)]['tipo'] == 'int' else 'FLD'
            operacion += f'{cmd} {get_key(terceto.valor3)}\n'
        if not is_index(terceto.valor2):
            cmd = 'FILD' if tabla_de_simbolos[get_key(terceto.valor2)]['tipo'] == 'int' else 'FLD'
            operacion += f'{cmd} {get_key(terceto.valor2)}\n'
        if not is_index(terceto.valor3) and is_index(terceto.valor2):
            operacion += f'FXCH\n'
        if is_index(terceto.valor2) and is_index(terceto.valor3):
            operacion += f'FXCH\n'
        operacion += 'FCOM\nFSTSW ax\nSAHF\n'
        self.assembler.append(operacion)

    def traducir_salto(self, terceto: Terceto):
        operacion = ''
        salto = diccionario_comparadores[terceto.valor1]
        indice = int(convertir_indice(terceto.valor2))
        operacion += f'{salto} ETIQ_{indice}\n'
        self.assembler.append(operacion)
        etiquetas.add(indice)

    def crear_data(self):
        operacion = 'include macros2.asm\ninclude number.asm\n.MODEL  LARGE\n.386\n.STACK 200h\n\n;variables de la tabla de simbolos\n'
        operacion += '.DATA\n\n'

        for id, values in tabla_de_simbolos.items():
            nombre = id
            tipo = values['tipo']
            valor = values['valor']
            longitud = values['longitud']

            if tipo == "int" or tipo == "float":
                valor_numerico = valor if valor else '?'
                operacion += f"{nombre:<15} {'dd':<10} {valor_numerico:<5}\n" if valor else f"{nombre:<15} {'dd':<10} ?\n"
            if tipo == "str":
                valor_str = f'{'db':<10} {'0Dh, "'+valor+'"':<5}, "$", {longitud:<4} dup (?)\n' if valor else f'{'dw':<10} "?"\n'
                operacion += f"{nombre:<15} {valor_str}"
            if tipo == "bin":
                valor_str = f'{'0Dh, "'+valor+'"':<5}' if valor else f'{'"", ?,':<4}'
                operacion += f"{nombre:<15} {'db':<10} {valor_str} {'39':<4}\n"

        operacion += "\n.CODE\n\nstart:\nmov ax,@data\nmov ds,ax\nFINIT;"
        self.assembler.insert(0, operacion)

    def crear_end(self):
        operacion = '\nmov ax, 4C00h\nint 21h\nEND start'
        self.assembler.append(operacion)
