
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ASIGNACION CADENA COMO DEFINIR DIGITO DIVISION ENTERO ESCRIBIR FIN ID INICIO MODULO MULTIPLICACION PARENTESIS_DER PARENTESIS_IZQ PUNTO_Y_COMA REAL RESTA SUMAprograma : INICIO instrucciones FINinstrucciones : instruccion\n                     | instruccion instruccionesinstruccion : definicion\n                   | escritura\n                   | asignaciondefinicion : DEFINIR tdato COMO tipo_dato PUNTO_Y_COMAasignacion : tdato ASIGNACION expresion PUNTO_Y_COMAtdato : IDtipo_dato : ENTERO\n                 | REALescritura : ESCRIBIR expresion PUNTO_Y_COMAexpresion : ID\n                 | DIGITO \n                 | CADENA\n                 | expresion SUMA expresion \n                 | expresion RESTA expresion \n                 | expresion MULTIPLICACION expresion \n                 | expresion DIVISION expresion \n                 | expresion MODULO expresion \n                 | PARENTESIS_IZQ expresion PARENTESIS_DER\n                 | CADENA SUMA CADENA'
    
_lr_action_items = {'INICIO':([0,],[2,]),'$end':([1,12,],[0,-1,]),'DEFINIR':([2,4,5,6,7,23,34,42,],[8,8,-4,-5,-6,-12,-8,-7,]),'ESCRIBIR':([2,4,5,6,7,23,34,42,],[10,10,-4,-5,-6,-12,-8,-7,]),'ID':([2,4,5,6,7,8,10,15,20,23,24,25,26,27,28,34,42,],[11,11,-4,-5,-6,11,17,17,17,-12,17,17,17,17,17,-8,-7,]),'FIN':([3,4,5,6,7,13,23,34,42,],[12,-2,-4,-5,-6,-3,-12,-8,-7,]),'ASIGNACION':([9,11,],[15,-9,]),'DIGITO':([10,15,20,24,25,26,27,28,],[18,18,18,18,18,18,18,18,]),'CADENA':([10,15,20,24,25,26,27,28,29,],[19,19,19,19,19,19,19,19,40,]),'PARENTESIS_IZQ':([10,15,20,24,25,26,27,28,],[20,20,20,20,20,20,20,20,]),'COMO':([11,14,],[-9,21,]),'PUNTO_Y_COMA':([16,17,18,19,22,31,32,33,35,36,37,38,39,40,41,],[23,-13,-14,-15,34,42,-10,-11,-16,-17,-18,-19,-20,-22,-21,]),'SUMA':([16,17,18,19,22,30,35,36,37,38,39,40,41,],[24,-13,-14,29,24,24,24,24,24,24,24,-22,-21,]),'RESTA':([16,17,18,19,22,30,35,36,37,38,39,40,41,],[25,-13,-14,-15,25,25,25,25,25,25,25,-22,-21,]),'MULTIPLICACION':([16,17,18,19,22,30,35,36,37,38,39,40,41,],[26,-13,-14,-15,26,26,26,26,26,26,26,-22,-21,]),'DIVISION':([16,17,18,19,22,30,35,36,37,38,39,40,41,],[27,-13,-14,-15,27,27,27,27,27,27,27,-22,-21,]),'MODULO':([16,17,18,19,22,30,35,36,37,38,39,40,41,],[28,-13,-14,-15,28,28,28,28,28,28,28,-22,-21,]),'PARENTESIS_DER':([17,18,19,30,35,36,37,38,39,40,41,],[-13,-14,-15,41,-16,-17,-18,-19,-20,-22,-21,]),'ENTERO':([21,],[32,]),'REAL':([21,],[33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'instrucciones':([2,4,],[3,13,]),'instruccion':([2,4,],[4,4,]),'definicion':([2,4,],[5,5,]),'escritura':([2,4,],[6,6,]),'asignacion':([2,4,],[7,7,]),'tdato':([2,4,8,],[9,9,14,]),'expresion':([10,15,20,24,25,26,27,28,],[16,22,30,35,36,37,38,39,]),'tipo_dato':([21,],[31,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> INICIO instrucciones FIN','programa',3,'p_programa','parser.py',22),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones','parser.py',26),
  ('instrucciones -> instruccion instrucciones','instrucciones',2,'p_instrucciones','parser.py',27),
  ('instruccion -> definicion','instruccion',1,'p_instruccion','parser.py',34),
  ('instruccion -> escritura','instruccion',1,'p_instruccion','parser.py',35),
  ('instruccion -> asignacion','instruccion',1,'p_instruccion','parser.py',36),
  ('definicion -> DEFINIR tdato COMO tipo_dato PUNTO_Y_COMA','definicion',5,'p_definicion','parser.py',40),
  ('asignacion -> tdato ASIGNACION expresion PUNTO_Y_COMA','asignacion',4,'p_asignacion','parser.py',48),
  ('tdato -> ID','tdato',1,'p_tdato','parser.py',67),
  ('tipo_dato -> ENTERO','tipo_dato',1,'p_tipo_dato','parser.py',71),
  ('tipo_dato -> REAL','tipo_dato',1,'p_tipo_dato','parser.py',72),
  ('escritura -> ESCRIBIR expresion PUNTO_Y_COMA','escritura',3,'p_escritura','parser.py',76),
  ('expresion -> ID','expresion',1,'p_expresion','parser.py',93),
  ('expresion -> DIGITO','expresion',1,'p_expresion','parser.py',94),
  ('expresion -> CADENA','expresion',1,'p_expresion','parser.py',95),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion','parser.py',96),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion','parser.py',97),
  ('expresion -> expresion MULTIPLICACION expresion','expresion',3,'p_expresion','parser.py',98),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion','parser.py',99),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion','parser.py',100),
  ('expresion -> PARENTESIS_IZQ expresion PARENTESIS_DER','expresion',3,'p_expresion','parser.py',101),
  ('expresion -> CADENA SUMA CADENA','expresion',3,'p_expresion','parser.py',102),
]
