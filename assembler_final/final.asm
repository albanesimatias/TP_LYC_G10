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
i               dd         ?
_1              dd         1    
_2              dd         2    
_3              dd         3    
_5              dd         5    
__Hola_mundo    db         0Dh, "Hola mundo", "$", 10   dup (?)
__hola          db         0Dh, "hola", "$", 4    dup (?)
_0              dd         ?
_4              dd         4    
__iterando      db         0Dh, "iterando", "$", 8    dup (?)
_2.5            dd         2.5  
_1111b          db         0Dh, "1111b" 39  
_101b           db         0Dh, "101b" 39  
_3.5            dd         3.5  

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

CALL displayString var_str

FILD _1
FILD _1
FCOM
FSTSW ax
SAHF

JNE ETIQ_13

CALL displayString __hola

JMP ETIQ_14

ETIQ_13:
CALL displayString var_str

ETIQ_14:
FILD _0
FISTP i

ETIQ_15:
FILD _4
FILD i
FCOM
FSTSW ax
SAHF

JAE ETIQ_21

CALL displayString __iterando

FILD i
FILD _1
FADD
FFREE st(0)

FISTP i

JMP ETIQ_15

ETIQ_21:
FILD _1
FISTP var

FILD _2
FISTP cont



mov ax, 4C00h
int 21h
END start