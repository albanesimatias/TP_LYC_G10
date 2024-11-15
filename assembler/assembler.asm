include macros2.asm
include number.asm
.MODEL  LARGE
.386
.STACK 200h

;variables de la tabla de simbolos
.DATA

var             dd         ?
var2            dd         ?
_1              dd         1    
_2              dd         2    
_3              dd         3    
_5              dd         5    
_6              dd         6    
_7              dd         7    
_46             dd         46   

.CODE

start:
mov ax,@data
mov ds,ax
FINIT;
FILD _3
FILD _3
FDIV

FILD _2
FXCH
FMUL

FILD _1
FXCH
FADD

FILD _5
FADD

FILD _5
FADD

FILD _5
FSUB

FISTP var

FILD _5
FILD _6
FMUL

FILD _7
FMUL

FILD _46
FILD _2
FDIV

FADD

FISTP var2

FILD var
FILD var2
FADD

FISTP var



mov ax, 4C00h
int 21h
END start