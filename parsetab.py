
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightASIGNACIONrightIGUALIleftMAYORQMENORQMAYORIMENORIleftMASMENOSrightUMENOSleftMULTIPLICACIONDIVISIONleftA_PARENTESISC_PARENTESISAND ASIGNACION A_CORCHETE A_LLAVE A_PARENTESIS CADENA COMA CONTAR_BINARIOS C_CORCHETE C_LLAVE C_PARENTESIS DISTINTOQ DIVISION DOS_PUNTOS ELSE FLOAT IF IGUALI INIT INT MAS MAYORI MAYORQ MENORI MENORQ MENOS MULTIPLICACION NOT N_BINARIO N_DECIMAL N_ENTERO OR PUNTO_Y_COMA READ STR SUMAR_LOS_ULTIMOS VARIABLE WHILE WRITEstart : programaprograma : programa sentencia\n                | sentencia\n    sentencia : asignacion PUNTO_Y_COMA\n                 | iteracion\n                 | seleccion\n                 | bloque_declaracion\n                 | read PUNTO_Y_COMA\n                 | write PUNTO_Y_COMA\n    read : READ A_PARENTESIS elemento C_PARENTESISwrite : WRITE A_PARENTESIS elemento C_PARENTESISbloque_declaracion : INIT A_LLAVE declaraciones C_LLAVE\n    declaraciones : declaraciones declaracion\n                     | declaracion\n    declaracion : lista_variables DOS_PUNTOS tipo_dato PUNTO_Y_COMAlista_variables : VARIABLE\n                       | lista_variables COMA VARIABLE\n    tipo_dato : FLOAT\n                 | INT\n                 | STR\n    seleccion : IF A_PARENTESIS condicion C_PARENTESIS bloque\n                 | IF A_PARENTESIS condicion C_PARENTESIS bloque ELSE bloque\n    iteracion : WHILE A_PARENTESIS condicion C_PARENTESIS bloquecondicion : comparacion OR comparacion\n                 | comparacion AND comparacion\n                 | NOT comparacion\n                 | comparacion\n    comparacion : expresion comparador expresion\n                   | expresion\n    comparador : MENORI\n                  | MENORQ\n                  | MAYORQ\n                  | MAYORI\n                  | IGUALI\n                  | DISTINTOQ\n     bloque : A_LLAVE programa C_LLAVEasignacion : VARIABLE ASIGNACION lista\n                  | VARIABLE ASIGNACION expresion\n                  | VARIABLE ASIGNACION condicion\n    sumar_los_ultimos : SUMAR_LOS_ULTIMOS A_PARENTESIS N_ENTERO PUNTO_Y_COMA lista C_PARENTESIS\n    contar_binarios : CONTAR_BINARIOS A_PARENTESIS lista C_PARENTESISlista : A_CORCHETE elementos C_CORCHETE\n             | A_CORCHETE C_CORCHETE\n    expresion : expresion MAS terminoexpresion : MENOS expresion %prec UMENOSexpresion : expresion MENOS terminoexpresion : terminotermino : termino MULTIPLICACION elementotermino : termino DIVISION elementotermino : elementoelemento : A_PARENTESIS expresion C_PARENTESISelementos : elementos COMA elemento\n                 | elementoelemento : N_ENTERO\n                | N_DECIMAL\n                | N_BINARIO\n                | VARIABLE\n                | CADENA\n                | sumar_los_ultimos\n                | contar_binarios\n    '
    
_lr_action_items = {'VARIABLE':([0,2,3,5,6,7,16,17,18,19,20,21,22,23,24,25,30,32,34,36,48,49,54,55,56,57,58,59,60,61,62,66,67,69,70,77,78,80,87,95,96,97,106,108,110,111,],[10,10,-3,-5,-6,-7,-2,-4,-8,-9,26,26,26,51,26,26,26,26,26,26,51,-14,26,26,26,-30,-31,-32,-33,-34,-35,26,26,26,26,-12,-13,102,26,-23,10,-21,10,-15,-36,-22,]),'WHILE':([0,2,3,5,6,7,16,17,18,19,77,95,96,97,106,110,111,],[11,11,-3,-5,-6,-7,-2,-4,-8,-9,-12,-23,11,-21,11,-36,-22,]),'IF':([0,2,3,5,6,7,16,17,18,19,77,95,96,97,106,110,111,],[12,12,-3,-5,-6,-7,-2,-4,-8,-9,-12,-23,12,-21,12,-36,-22,]),'INIT':([0,2,3,5,6,7,16,17,18,19,77,95,96,97,106,110,111,],[13,13,-3,-5,-6,-7,-2,-4,-8,-9,-12,-23,13,-21,13,-36,-22,]),'READ':([0,2,3,5,6,7,16,17,18,19,77,95,96,97,106,110,111,],[14,14,-3,-5,-6,-7,-2,-4,-8,-9,-12,-23,14,-21,14,-36,-22,]),'WRITE':([0,2,3,5,6,7,16,17,18,19,77,95,96,97,106,110,111,],[15,15,-3,-5,-6,-7,-2,-4,-8,-9,-12,-23,15,-21,15,-36,-22,]),'$end':([1,2,3,5,6,7,16,17,18,19,77,95,97,110,111,],[0,-1,-3,-5,-6,-7,-2,-4,-8,-9,-12,-23,-21,-36,-22,]),'C_LLAVE':([3,5,6,7,16,17,18,19,48,49,77,78,95,97,106,108,110,111,],[-3,-5,-6,-7,-2,-4,-8,-9,77,-14,-12,-13,-23,-21,110,-15,-36,-22,]),'PUNTO_Y_COMA':([4,8,9,26,27,28,29,31,33,35,37,38,39,40,41,42,46,64,68,71,81,82,83,84,85,86,88,89,90,91,92,93,98,99,100,101,105,112,],[17,18,19,-57,-37,-29,-39,-47,-27,-50,-54,-55,-56,-58,-59,-60,-29,-43,-45,-26,-10,-11,-44,-46,-28,-42,-48,-49,-24,-25,-51,104,108,-18,-19,-20,-41,-40,]),'ASIGNACION':([10,],[20,]),'A_PARENTESIS':([11,12,14,15,20,21,22,24,25,30,32,34,36,43,44,54,55,56,57,58,59,60,61,62,66,67,69,70,87,],[21,22,24,25,36,36,36,36,36,36,36,36,36,73,74,36,36,36,-30,-31,-32,-33,-34,-35,36,36,36,36,36,]),'A_LLAVE':([13,75,76,107,],[23,96,96,96,]),'A_CORCHETE':([20,74,104,],[30,30,30,]),'MENOS':([20,21,22,26,28,31,32,34,35,36,37,38,39,40,41,42,46,56,57,58,59,60,61,62,68,69,70,72,83,84,85,88,89,92,105,112,],[32,32,32,-57,55,-47,32,32,-50,32,-54,-55,-56,-58,-59,-60,55,32,-30,-31,-32,-33,-34,-35,-45,32,32,55,-44,-46,55,-48,-49,-51,-41,-40,]),'NOT':([20,21,22,],[34,34,34,]),'N_ENTERO':([20,21,22,24,25,30,32,34,36,54,55,56,57,58,59,60,61,62,66,67,69,70,73,87,],[37,37,37,37,37,37,37,37,37,37,37,37,-30,-31,-32,-33,-34,-35,37,37,37,37,93,37,]),'N_DECIMAL':([20,21,22,24,25,30,32,34,36,54,55,56,57,58,59,60,61,62,66,67,69,70,87,],[38,38,38,38,38,38,38,38,38,38,38,38,-30,-31,-32,-33,-34,-35,38,38,38,38,38,]),'N_BINARIO':([20,21,22,24,25,30,32,34,36,54,55,56,57,58,59,60,61,62,66,67,69,70,87,],[39,39,39,39,39,39,39,39,39,39,39,39,-30,-31,-32,-33,-34,-35,39,39,39,39,39,]),'CADENA':([20,21,22,24,25,30,32,34,36,54,55,56,57,58,59,60,61,62,66,67,69,70,87,],[40,40,40,40,40,40,40,40,40,40,40,40,-30,-31,-32,-33,-34,-35,40,40,40,40,40,]),'SUMAR_LOS_ULTIMOS':([20,21,22,24,25,30,32,34,36,54,55,56,57,58,59,60,61,62,66,67,69,70,87,],[43,43,43,43,43,43,43,43,43,43,43,43,-30,-31,-32,-33,-34,-35,43,43,43,43,43,]),'CONTAR_BINARIOS':([20,21,22,24,25,30,32,34,36,54,55,56,57,58,59,60,61,62,66,67,69,70,87,],[44,44,44,44,44,44,44,44,44,44,44,44,-30,-31,-32,-33,-34,-35,44,44,44,44,44,]),'MULTIPLICACION':([26,31,35,37,38,39,40,41,42,83,84,88,89,92,105,112,],[-57,66,-50,-54,-55,-56,-58,-59,-60,66,66,-48,-49,-51,-41,-40,]),'DIVISION':([26,31,35,37,38,39,40,41,42,83,84,88,89,92,105,112,],[-57,67,-50,-54,-55,-56,-58,-59,-60,67,67,-48,-49,-51,-41,-40,]),'MAS':([26,28,31,35,37,38,39,40,41,42,46,68,72,83,84,85,88,89,92,105,112,],[-57,54,-47,-50,-54,-55,-56,-58,-59,-60,54,-45,54,-44,-46,54,-48,-49,-51,-41,-40,]),'MENORI':([26,28,31,35,37,38,39,40,41,42,46,68,83,84,88,89,92,105,112,],[-57,57,-47,-50,-54,-55,-56,-58,-59,-60,57,-45,-44,-46,-48,-49,-51,-41,-40,]),'MENORQ':([26,28,31,35,37,38,39,40,41,42,46,68,83,84,88,89,92,105,112,],[-57,58,-47,-50,-54,-55,-56,-58,-59,-60,58,-45,-44,-46,-48,-49,-51,-41,-40,]),'MAYORQ':([26,28,31,35,37,38,39,40,41,42,46,68,83,84,88,89,92,105,112,],[-57,59,-47,-50,-54,-55,-56,-58,-59,-60,59,-45,-44,-46,-48,-49,-51,-41,-40,]),'MAYORI':([26,28,31,35,37,38,39,40,41,42,46,68,83,84,88,89,92,105,112,],[-57,60,-47,-50,-54,-55,-56,-58,-59,-60,60,-45,-44,-46,-48,-49,-51,-41,-40,]),'IGUALI':([26,28,31,35,37,38,39,40,41,42,46,68,83,84,88,89,92,105,112,],[-57,61,-47,-50,-54,-55,-56,-58,-59,-60,61,-45,-44,-46,-48,-49,-51,-41,-40,]),'DISTINTOQ':([26,28,31,35,37,38,39,40,41,42,46,68,83,84,88,89,92,105,112,],[-57,62,-47,-50,-54,-55,-56,-58,-59,-60,62,-45,-44,-46,-48,-49,-51,-41,-40,]),'OR':([26,28,31,33,35,37,38,39,40,41,42,46,68,83,84,85,88,89,92,105,112,],[-57,-29,-47,69,-50,-54,-55,-56,-58,-59,-60,-29,-45,-44,-46,-28,-48,-49,-51,-41,-40,]),'AND':([26,28,31,33,35,37,38,39,40,41,42,46,68,83,84,85,88,89,92,105,112,],[-57,-29,-47,70,-50,-54,-55,-56,-58,-59,-60,-29,-45,-44,-46,-28,-48,-49,-51,-41,-40,]),'C_PARENTESIS':([26,31,33,35,37,38,39,40,41,42,45,46,47,52,53,64,68,71,72,83,84,85,86,88,89,90,91,92,94,105,109,112,],[-57,-47,-27,-50,-54,-55,-56,-58,-59,-60,75,-29,76,81,82,-43,-45,-26,92,-44,-46,-28,-42,-48,-49,-24,-25,-51,105,-41,112,-40,]),'C_CORCHETE':([26,30,37,38,39,40,41,42,63,65,92,103,105,112,],[-57,64,-54,-55,-56,-58,-59,-60,86,-53,-51,-52,-41,-40,]),'COMA':([26,37,38,39,40,41,42,50,51,63,65,92,102,103,105,112,],[-57,-54,-55,-56,-58,-59,-60,80,-16,87,-53,-51,-17,-52,-41,-40,]),'DOS_PUNTOS':([50,51,102,],[79,-16,-17,]),'FLOAT':([79,],[99,]),'INT':([79,],[100,]),'STR':([79,],[101,]),'ELSE':([97,110,],[107,-36,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'programa':([0,96,],[2,106,]),'sentencia':([0,2,96,106,],[3,16,3,16,]),'asignacion':([0,2,96,106,],[4,4,4,4,]),'iteracion':([0,2,96,106,],[5,5,5,5,]),'seleccion':([0,2,96,106,],[6,6,6,6,]),'bloque_declaracion':([0,2,96,106,],[7,7,7,7,]),'read':([0,2,96,106,],[8,8,8,8,]),'write':([0,2,96,106,],[9,9,9,9,]),'lista':([20,74,104,],[27,94,109,]),'expresion':([20,21,22,32,34,36,56,69,70,],[28,46,46,68,46,72,85,46,46,]),'condicion':([20,21,22,],[29,45,47,]),'termino':([20,21,22,32,34,36,54,55,56,69,70,],[31,31,31,31,31,31,83,84,31,31,31,]),'comparacion':([20,21,22,34,69,70,],[33,33,33,71,90,91,]),'elemento':([20,21,22,24,25,30,32,34,36,54,55,56,66,67,69,70,87,],[35,35,35,52,53,65,35,35,35,35,35,35,88,89,35,35,103,]),'sumar_los_ultimos':([20,21,22,24,25,30,32,34,36,54,55,56,66,67,69,70,87,],[41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,]),'contar_binarios':([20,21,22,24,25,30,32,34,36,54,55,56,66,67,69,70,87,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'declaraciones':([23,],[48,]),'declaracion':([23,48,],[49,78,]),'lista_variables':([23,48,],[50,50,]),'comparador':([28,46,],[56,56,]),'elementos':([30,],[63,]),'bloque':([75,76,107,],[95,97,111,]),'tipo_dato':([79,],[98,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> programa','start',1,'p_start','parser.py',24),
  ('programa -> programa sentencia','programa',2,'p_programa','parser.py',29),
  ('programa -> sentencia','programa',1,'p_programa','parser.py',30),
  ('sentencia -> asignacion PUNTO_Y_COMA','sentencia',2,'p_sentencia','parser.py',39),
  ('sentencia -> iteracion','sentencia',1,'p_sentencia','parser.py',40),
  ('sentencia -> seleccion','sentencia',1,'p_sentencia','parser.py',41),
  ('sentencia -> bloque_declaracion','sentencia',1,'p_sentencia','parser.py',42),
  ('sentencia -> read PUNTO_Y_COMA','sentencia',2,'p_sentencia','parser.py',43),
  ('sentencia -> write PUNTO_Y_COMA','sentencia',2,'p_sentencia','parser.py',44),
  ('read -> READ A_PARENTESIS elemento C_PARENTESIS','read',4,'p_read','parser.py',50),
  ('write -> WRITE A_PARENTESIS elemento C_PARENTESIS','write',4,'p_write','parser.py',55),
  ('bloque_declaracion -> INIT A_LLAVE declaraciones C_LLAVE','bloque_declaracion',4,'p_bloque_declaracion','parser.py',60),
  ('declaraciones -> declaraciones declaracion','declaraciones',2,'p_declaraciones','parser.py',66),
  ('declaraciones -> declaracion','declaraciones',1,'p_declaraciones','parser.py',67),
  ('declaracion -> lista_variables DOS_PUNTOS tipo_dato PUNTO_Y_COMA','declaracion',4,'p_declaracion','parser.py',76),
  ('lista_variables -> VARIABLE','lista_variables',1,'p_lista_variables','parser.py',81),
  ('lista_variables -> lista_variables COMA VARIABLE','lista_variables',3,'p_lista_variables','parser.py',82),
  ('tipo_dato -> FLOAT','tipo_dato',1,'p_tipo_dato','parser.py',91),
  ('tipo_dato -> INT','tipo_dato',1,'p_tipo_dato','parser.py',92),
  ('tipo_dato -> STR','tipo_dato',1,'p_tipo_dato','parser.py',93),
  ('seleccion -> IF A_PARENTESIS condicion C_PARENTESIS bloque','seleccion',5,'p_seleccion','parser.py',99),
  ('seleccion -> IF A_PARENTESIS condicion C_PARENTESIS bloque ELSE bloque','seleccion',7,'p_seleccion','parser.py',100),
  ('iteracion -> WHILE A_PARENTESIS condicion C_PARENTESIS bloque','iteracion',5,'p_iteracion','parser.py',114),
  ('condicion -> comparacion OR comparacion','condicion',3,'p_condicion','parser.py',119),
  ('condicion -> comparacion AND comparacion','condicion',3,'p_condicion','parser.py',120),
  ('condicion -> NOT comparacion','condicion',2,'p_condicion','parser.py',121),
  ('condicion -> comparacion','condicion',1,'p_condicion','parser.py',122),
  ('comparacion -> expresion comparador expresion','comparacion',3,'p_comparacion','parser.py',138),
  ('comparacion -> expresion','comparacion',1,'p_comparacion','parser.py',139),
  ('comparador -> MENORI','comparador',1,'p_comparador','parser.py',157),
  ('comparador -> MENORQ','comparador',1,'p_comparador','parser.py',158),
  ('comparador -> MAYORQ','comparador',1,'p_comparador','parser.py',159),
  ('comparador -> MAYORI','comparador',1,'p_comparador','parser.py',160),
  ('comparador -> IGUALI','comparador',1,'p_comparador','parser.py',161),
  ('comparador -> DISTINTOQ','comparador',1,'p_comparador','parser.py',162),
  ('bloque -> A_LLAVE programa C_LLAVE','bloque',3,'p_bloque','parser.py',169),
  ('asignacion -> VARIABLE ASIGNACION lista','asignacion',3,'p_asignacion','parser.py',175),
  ('asignacion -> VARIABLE ASIGNACION expresion','asignacion',3,'p_asignacion','parser.py',176),
  ('asignacion -> VARIABLE ASIGNACION condicion','asignacion',3,'p_asignacion','parser.py',177),
  ('sumar_los_ultimos -> SUMAR_LOS_ULTIMOS A_PARENTESIS N_ENTERO PUNTO_Y_COMA lista C_PARENTESIS','sumar_los_ultimos',6,'p_sumar_los_ultimos','parser.py',184),
  ('contar_binarios -> CONTAR_BINARIOS A_PARENTESIS lista C_PARENTESIS','contar_binarios',4,'p_contar_binarios','parser.py',196),
  ('lista -> A_CORCHETE elementos C_CORCHETE','lista',3,'p_lista','parser.py',201),
  ('lista -> A_CORCHETE C_CORCHETE','lista',2,'p_lista','parser.py',202),
  ('expresion -> expresion MAS termino','expresion',3,'p_expresion_mas','parser.py',215),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_menos_unario','parser.py',221),
  ('expresion -> expresion MENOS termino','expresion',3,'p_expresion_menos','parser.py',227),
  ('expresion -> termino','expresion',1,'p_expresion_termino','parser.py',233),
  ('termino -> termino MULTIPLICACION elemento','termino',3,'p_termino_multiplicacion','parser.py',239),
  ('termino -> termino DIVISION elemento','termino',3,'p_termino_division','parser.py',245),
  ('termino -> elemento','termino',1,'p_termino_elemento','parser.py',254),
  ('elemento -> A_PARENTESIS expresion C_PARENTESIS','elemento',3,'p_elemento_expresion','parser.py',260),
  ('elementos -> elementos COMA elemento','elementos',3,'p_elementos','parser.py',266),
  ('elementos -> elemento','elementos',1,'p_elementos','parser.py',267),
  ('elemento -> N_ENTERO','elemento',1,'p_elemento','parser.py',279),
  ('elemento -> N_DECIMAL','elemento',1,'p_elemento','parser.py',280),
  ('elemento -> N_BINARIO','elemento',1,'p_elemento','parser.py',281),
  ('elemento -> VARIABLE','elemento',1,'p_elemento','parser.py',282),
  ('elemento -> CADENA','elemento',1,'p_elemento','parser.py',283),
  ('elemento -> sumar_los_ultimos','elemento',1,'p_elemento','parser.py',284),
  ('elemento -> contar_binarios','elemento',1,'p_elemento','parser.py',285),
]
