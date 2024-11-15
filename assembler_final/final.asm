include macros2.asm
include number.asm
.MODEL  LARGE
.386
.STACK 200h

;variables de la tabla de simbolos
.DATA

var             dd         ?
var2            dd         ?
var_str         dw         "?"
_1              dd         1    
_2              dd         2    
_3              dd         3    
_5              dd         5    
_6              dd         6    
_7              dd         7    
_46             dd         46   
__Hola_mundo    db         0Dh, "Hola mundo", "$", 10   dup (?)

.CODE

start:
mov ax,@data
mov ds,ax
FINIT;
FILD _3
FILD _3
FDIV
FFREE st(0)

FILD _2
FXCH
FMUL
FFREE st(0)

FILD _1
FXCH
FADD
FFREE st(0)

FILD _5
FADD
FFREE st(0)

FILD _5
FADD
FFREE st(0)

FILD _5
FSUB
FFREE st(0)

FISTP var

FILD _5
FILD _6
FMUL
FFREE st(0)

FILD _7
FMUL
FFREE st(0)

FILD _46
FILD _2
FDIV
FFREE st(0)

FADD
FFREE st(0)

FISTP var2

FILD var
FILD var2
FADD
FFREE st(0)

FISTP var

lea ax, __Hola_mundo
mov var_str, ax

CALL displayString var_str



mov ax, 4C00h
int 21h
END start