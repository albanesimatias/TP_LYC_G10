include macros2.asm
include number.asm
.MODEL  LARGE
.386
.STACK 200h

;variables de la tabla de simbolos
.DATA

var             dd         ?
cont            dd         ?
var_str         dw         "?"
var_float       dd         ?
i               dd         ?
_1              dd         1    
_2              dd         2    
_3              dd         3    
_5              dd         5    
__Hola_mundo    db         0Dh, "Hola mundo", "$", 10   dup (?)
_3_5            dd         3.5  
_0              dd         ?
_4              dd         4    
_2_5            dd         2.5  
_1111b          db         0Dh, "1111b", "$", 31   dup (?)
_101b           db         0Dh, "101b", "$", 31   dup (?)

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

lea ax, __Hola_mundo
mov var_str, ax

FLD _3_5
FSTP var_float

FILD _1
FILD _1
FCOM
FSTSW ax
SAHF

JNE ETIQ_13

FILD var
FISTP var

JMP ETIQ_14

ETIQ_13:
FILD var
FISTP var

ETIQ_14:
FILD _0
FISTP i

ETIQ_15:
FILD _4
FILD i
FCOM
FSTSW ax
SAHF

JAE ETIQ_20

FILD i
FILD _1
FADD
FFREE st(0)

FISTP i

JMP ETIQ_15

ETIQ_20:
FILD _1
FISTP var

FILD _2
FISTP cont



mov ax, 4C00h
int 21h
END start