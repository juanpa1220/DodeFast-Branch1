
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AA AF ALEATORIO COMA CUANDO DAA DAB DCL DEC DEFAULT DESDE DFA DFB DIFERENTE DOSPUNTOS ENCASO ENTONS F FIN FINDESDE FINENCASO FINPROC HAGA HASTA HASTAENCONTRAR IAA IAB ID IFA IFB IGUAL INC INI INICIO INICIOPROC LLAMAR LLAVE_DER LLAVE_IZQ MAYOR MAYORIGUAL MENOR MENORIGUAL MOVER NUMERO PARENTESIS_DER PARENTESIS_IZQ PROC PUNTOCOMA REPITA SINO SUMA\n    Start : code\n    \n    code : INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento\n    \n    cuerpo : empty\n    \n    cuerpo : expresion cuerpo\n    \n        cuerpo : variable cuerpo\n\n        \n    variable : variable1\n            | variable2\n    \n    variable1 : DCL ID PUNTOCOMA\n    \n    variable2 : DCL ID DEFAULT NUMERO PUNTOCOMA\n    \n    expresion : empty\n        \n    expresion : condicion1 expresion\n            | condicion2 expresion\n            | repita expresion\n            | hacer expresion\n            | funcion expresion\n            | llamarProc expresion\n    \n        expresion : condicion1\n\n        \n        expresion : condicion2\n\n        \n    condicion1 : ENCASO cond1Aux1 FINENCASO PUNTOCOMA\n    \n    condicion2 : ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA\n    \n    cond2Aux1 : cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER\n                | empty empty empty empty empty\n    \n    cond1Aux1 : cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER\n            | empty empty empty empty empty\n    \n    cond1Aux2 : empty\n        \n    cond1Aux2 : CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2\n    \n        cond2Aux2 : CUANDO  condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2\n        \n    cond2Aux2 : empty\n        \n    condicion : IGUAL\n              | MAYOR\n              | MENOR\n              | DIFERENTE\n              | MAYORIGUAL\n              | MENORIGUAL\n    \n    sentencia : ID\n               | NUMERO\n    \n     repita : REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA\n    \n    hacer : DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA\n    \n    funcion : Aleatorio\n            | Mover\n            | funcionAlge\n    \n    Aleatorio : ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA\n    \n    Mover : MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA\n    \n    paramMover : AF\n                | F\n                | DFA\n                | IFA\n                | DFB\n                | IFB\n                | A\n                | DAA\n                | IAA\n                | DAB\n                | IAB\n                | AA\n    \n    funcionAlge : INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion\n             | DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion\n             | INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion\n    \n    funcionAlge : INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n             | INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA\n    \n        procedimiento : PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento\n                     | empty empty empty empty empty empty empty empty empty empty empty\n    \n    parametro : ID COMA parametro\n              | ID empty empty\n              | NUMERO COMA parametro\n              | NUMERO empty empty\n              | empty empty empty\n    \n    llamarProc : LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA\n    \n    empty :\n    '
    
_lr_action_items = {'INICIO':([0,],[3,]),'$end':([1,2,54,85,87,117,139,158,169,178,184,191,194,196,197,198,199,],[0,-1,-70,-2,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-70,-62,-63,]),'DOSPUNTOS':([3,177,],[4,183,]),'FIN':([4,5,6,7,8,9,10,11,12,13,14,15,16,20,21,22,31,32,33,34,35,36,37,38,39,66,88,111,118,133,134,150,165,166,167,174,175,176,181,195,],[-70,30,-3,-70,-70,-17,-18,-70,-70,-70,-70,-6,-7,-39,-40,-41,-4,-5,-11,-10,-12,-13,-14,-15,-16,-8,-19,-42,-20,-9,-43,-69,-59,-60,-61,-56,-57,-58,-37,-38,]),'ENCASO':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[17,-10,17,17,17,17,17,17,17,17,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,17,-8,-19,17,-42,-20,17,-9,-43,-69,17,17,17,17,17,17,-56,-57,-58,-37,17,-38,]),'REPITA':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[18,-10,18,18,18,18,18,18,18,18,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,18,-8,-19,18,-42,-20,18,-9,-43,-69,18,18,18,18,18,18,-56,-57,-58,-37,18,-38,]),'DESDE':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[19,-10,19,19,19,19,19,19,19,19,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,19,-8,-19,19,-42,-20,19,-9,-43,-69,19,19,19,19,19,19,-56,-57,-58,-37,19,-38,]),'LLAMAR':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[23,-10,23,23,23,23,23,23,23,23,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,23,-8,-19,23,-42,-20,23,-9,-43,-69,23,23,23,23,23,23,-56,-57,-58,-37,23,-38,]),'DCL':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,66,88,111,118,133,134,150,165,166,167,174,175,176,181,195,],[24,-10,24,24,-17,-18,-70,-70,-70,-70,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,-8,-19,-42,-20,-9,-43,-69,-59,-60,-61,-56,-57,-58,-37,-38,]),'ALEATORIO':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[25,-10,25,25,25,25,25,25,25,25,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,25,-8,-19,25,-42,-20,25,-9,-43,-69,25,25,25,25,25,25,-56,-57,-58,-37,25,-38,]),'MOVER':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[26,-10,26,26,26,26,26,26,26,26,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,26,-8,-19,26,-42,-20,26,-9,-43,-69,26,26,26,26,26,26,-56,-57,-58,-37,26,-38,]),'INC':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[27,-10,27,27,27,27,27,27,27,27,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,27,-8,-19,27,-42,-20,27,-9,-43,-69,27,27,27,27,27,27,-56,-57,-58,-37,27,-38,]),'DEC':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[28,-10,28,28,28,28,28,28,28,28,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,28,-8,-19,28,-42,-20,28,-9,-43,-69,28,28,28,28,28,28,-56,-57,-58,-37,28,-38,]),'INI':([4,6,7,8,9,10,11,12,13,14,15,16,20,21,22,33,34,35,36,37,38,39,45,66,88,99,111,118,119,133,134,150,161,162,165,166,167,173,174,175,176,181,183,195,],[29,-10,29,29,29,29,29,29,29,29,-6,-7,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,29,-8,-19,29,-42,-20,29,-9,-43,-69,29,29,29,29,29,29,-56,-57,-58,-37,29,-38,]),'LLAVE_DER':([9,10,11,12,13,14,20,21,22,33,34,35,36,37,38,39,45,63,88,99,111,118,119,122,134,140,150,161,162,165,166,167,170,171,173,174,175,176,181,182,195,],[-17,-18,-70,-70,-70,-70,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,-70,102,-19,-70,-42,-20,-70,143,-43,159,-69,-70,-70,-59,-60,-61,179,180,-70,-56,-57,-58,-37,189,-38,]),'FINPROC':([9,10,11,12,13,14,20,21,22,33,34,35,36,37,38,39,88,111,118,134,150,165,166,167,174,175,176,181,183,190,195,],[-17,-18,-70,-70,-70,-70,-39,-40,-41,-11,-10,-12,-13,-14,-15,-16,-19,-42,-20,-43,-69,-59,-60,-61,-56,-57,-58,-37,-70,193,-38,]),'ID':([17,19,23,24,44,51,52,53,64,65,86,92,93,94,95,96,97,98,101,113,114,115,125,126,127,131,138,163,],[41,46,47,48,62,82,83,84,103,106,116,103,-29,-30,-31,-32,-33,-34,103,103,103,103,146,103,106,106,106,103,]),'CUANDO':([17,41,179,180,],[44,59,59,44,]),'FINENCASO':([17,40,41,43,56,58,61,91,100,120,123,141,143,144,159,160,],[-70,55,-70,-70,89,-70,-70,-70,-70,-70,-70,-70,-23,-24,-21,-22,]),'SINO':([17,41,42,43,57,58,179,180,185,186,187,188,],[-70,-70,60,-25,90,-28,-70,-70,-27,-28,-26,-25,]),'LLAVE_IZQ':([18,60,90,142,145,164,],[45,99,119,161,162,173,]),'PARENTESIS_IZQ':([25,26,27,28,29,47,116,],[49,50,51,52,53,65,138,]),'PUNTOCOMA':([30,48,55,68,89,103,105,110,112,129,154,155,156,172,192,193,],[54,66,88,111,118,-35,-36,133,134,150,165,166,167,181,195,196,]),'IGUAL':([46,59,62,146,],[64,93,93,93,]),'DEFAULT':([48,],[67,]),'PARENTESIS_DER':([49,65,69,70,71,72,73,74,75,76,77,78,79,80,81,103,105,106,107,108,109,127,128,130,131,132,135,136,137,138,148,149,151,152,153,157,],[68,-70,112,-44,-45,-46,-47,-48,-49,-50,-51,-52,-53,-54,-55,-35,-36,-70,129,-70,-70,-70,-70,-70,-70,-70,154,155,156,-70,-64,-65,-68,-66,-67,168,]),'AF':([50,],[70,]),'F':([50,],[71,]),'DFA':([50,],[72,]),'IFA':([50,],[73,]),'DFB':([50,],[74,]),'IFB':([50,],[75,]),'A':([50,],[76,]),'DAA':([50,],[77,]),'IAA':([50,],[78,]),'DAB':([50,],[79,]),'IAB':([50,],[80,]),'AA':([50,],[81,]),'PROC':([54,196,],[86,86,]),'MAYOR':([59,62,146,],[94,94,94,]),'MENOR':([59,62,146,],[95,95,95,]),'DIFERENTE':([59,62,146,],[96,96,96,]),'MAYORIGUAL':([59,62,146,],[97,97,97,]),'MENORIGUAL':([59,62,146,],[98,98,98,]),'NUMERO':([64,65,67,92,93,94,95,96,97,98,101,113,114,115,126,127,131,138,163,],[105,109,110,105,-29,-30,-31,-32,-33,-34,105,105,105,105,105,109,109,109,105,]),'COMA':([82,83,84,106,109,],[113,114,115,127,131,]),'HASTAENCONTRAR':([102,],[125,]),'HASTA':([103,104,105,],[-35,126,-36,]),'ENTONS':([103,105,121,124,],[-35,-36,142,145,]),'HAGA':([103,105,147,],[-35,-36,164,]),'INICIOPROC':([168,],[177,]),'FINDESDE':([189,],[192,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Start':([0,],[1,]),'code':([0,],[2,]),'cuerpo':([4,7,8,],[5,31,32,]),'empty':([4,7,8,9,10,11,12,13,14,17,41,43,45,54,58,61,65,87,91,99,100,106,108,109,117,119,120,123,127,128,130,131,132,138,139,141,158,161,162,165,166,167,169,173,178,179,180,183,184,191,194,196,197,],[6,6,6,34,34,34,34,34,34,43,58,61,34,87,91,100,108,117,120,34,123,128,130,132,139,34,141,144,108,149,151,108,153,108,158,160,169,34,34,34,34,34,178,34,184,186,188,34,191,194,197,87,199,]),'expresion':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[7,7,7,33,35,36,37,38,39,63,122,140,170,171,174,175,176,182,190,]),'variable':([4,7,8,],[8,8,8,]),'condicion1':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'condicion2':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'repita':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'hacer':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'funcion':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'llamarProc':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'variable1':([4,7,8,],[15,15,15,]),'variable2':([4,7,8,],[16,16,16,]),'Aleatorio':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'Mover':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'funcionAlge':([4,7,8,9,10,11,12,13,14,45,99,119,161,162,165,166,167,173,183,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'cond1Aux1':([17,],[40,]),'cond1Aux2':([17,180,],[42,187,]),'cond2Aux1':([41,],[56,]),'cond2Aux2':([41,179,],[57,185,]),'paramMover':([50,],[69,]),'procedimiento':([54,196,],[85,198,]),'condicion':([59,62,146,],[92,101,163,]),'sentencia':([64,92,101,113,114,115,126,163,],[104,121,124,135,136,137,147,172,]),'parametro':([65,127,131,138,],[107,148,152,157,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> code','Start',1,'p_Start','SintacticAnalizer.py',15),
  ('code -> INICIO DOSPUNTOS cuerpo FIN PUNTOCOMA procedimiento','code',6,'p_Code','SintacticAnalizer.py',23),
  ('cuerpo -> empty','cuerpo',1,'p_cuerpo_empty','SintacticAnalizer.py',29),
  ('cuerpo -> expresion cuerpo','cuerpo',2,'p_cuerpo_expresion','SintacticAnalizer.py',36),
  ('cuerpo -> variable cuerpo','cuerpo',2,'p_cuerpo_variable','SintacticAnalizer.py',47),
  ('variable -> variable1','variable',1,'p_Variable','SintacticAnalizer.py',58),
  ('variable -> variable2','variable',1,'p_Variable','SintacticAnalizer.py',59),
  ('variable1 -> DCL ID PUNTOCOMA','variable1',3,'p_Variable1','SintacticAnalizer.py',67),
  ('variable2 -> DCL ID DEFAULT NUMERO PUNTOCOMA','variable2',5,'p_Variable2','SintacticAnalizer.py',76),
  ('expresion -> empty','expresion',1,'p_expresion_empty','SintacticAnalizer.py',85),
  ('expresion -> condicion1 expresion','expresion',2,'p_expresion','SintacticAnalizer.py',91),
  ('expresion -> condicion2 expresion','expresion',2,'p_expresion','SintacticAnalizer.py',92),
  ('expresion -> repita expresion','expresion',2,'p_expresion','SintacticAnalizer.py',93),
  ('expresion -> hacer expresion','expresion',2,'p_expresion','SintacticAnalizer.py',94),
  ('expresion -> funcion expresion','expresion',2,'p_expresion','SintacticAnalizer.py',95),
  ('expresion -> llamarProc expresion','expresion',2,'p_expresion','SintacticAnalizer.py',96),
  ('expresion -> condicion1','expresion',1,'p_expresion_condicion1','SintacticAnalizer.py',105),
  ('expresion -> condicion2','expresion',1,'p_expresion_condicion2','SintacticAnalizer.py',113),
  ('condicion1 -> ENCASO cond1Aux1 FINENCASO PUNTOCOMA','condicion1',4,'p_condicion1','SintacticAnalizer.py',121),
  ('condicion2 -> ENCASO ID cond2Aux1 FINENCASO PUNTOCOMA','condicion2',5,'p_condicion2','SintacticAnalizer.py',127),
  ('cond2Aux1 -> cond2Aux2 SINO LLAVE_IZQ expresion LLAVE_DER','cond2Aux1',5,'p_cond2Aux1','SintacticAnalizer.py',135),
  ('cond2Aux1 -> empty empty empty empty empty','cond2Aux1',5,'p_cond2Aux1','SintacticAnalizer.py',136),
  ('cond1Aux1 -> cond1Aux2 SINO LLAVE_IZQ expresion LLAVE_DER','cond1Aux1',5,'p_cond1Aux1','SintacticAnalizer.py',145),
  ('cond1Aux1 -> empty empty empty empty empty','cond1Aux1',5,'p_cond1Aux1','SintacticAnalizer.py',146),
  ('cond1Aux2 -> empty','cond1Aux2',1,'p_cond1Aux2_empty','SintacticAnalizer.py',157),
  ('cond1Aux2 -> CUANDO ID condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond1Aux2','cond1Aux2',9,'p_cond1Aux2','SintacticAnalizer.py',163),
  ('cond2Aux2 -> CUANDO condicion sentencia ENTONS LLAVE_IZQ expresion LLAVE_DER cond2Aux2','cond2Aux2',8,'p_cond2Aux2','SintacticAnalizer.py',175),
  ('cond2Aux2 -> empty','cond2Aux2',1,'p_cond2Aux2_empty','SintacticAnalizer.py',186),
  ('condicion -> IGUAL','condicion',1,'p_condicion','SintacticAnalizer.py',196),
  ('condicion -> MAYOR','condicion',1,'p_condicion','SintacticAnalizer.py',197),
  ('condicion -> MENOR','condicion',1,'p_condicion','SintacticAnalizer.py',198),
  ('condicion -> DIFERENTE','condicion',1,'p_condicion','SintacticAnalizer.py',199),
  ('condicion -> MAYORIGUAL','condicion',1,'p_condicion','SintacticAnalizer.py',200),
  ('condicion -> MENORIGUAL','condicion',1,'p_condicion','SintacticAnalizer.py',201),
  ('sentencia -> ID','sentencia',1,'p_sentencia','SintacticAnalizer.py',209),
  ('sentencia -> NUMERO','sentencia',1,'p_sentencia','SintacticAnalizer.py',210),
  ('repita -> REPITA LLAVE_IZQ expresion LLAVE_DER HASTAENCONTRAR ID condicion sentencia PUNTOCOMA','repita',9,'p_repita','SintacticAnalizer.py',217),
  ('hacer -> DESDE ID IGUAL sentencia HASTA sentencia HAGA LLAVE_IZQ expresion LLAVE_DER FINDESDE PUNTOCOMA','hacer',12,'p_hacer','SintacticAnalizer.py',226),
  ('funcion -> Aleatorio','funcion',1,'p_funcion','SintacticAnalizer.py',235),
  ('funcion -> Mover','funcion',1,'p_funcion','SintacticAnalizer.py',236),
  ('funcion -> funcionAlge','funcion',1,'p_funcion','SintacticAnalizer.py',237),
  ('Aleatorio -> ALEATORIO PARENTESIS_IZQ PARENTESIS_DER PUNTOCOMA','Aleatorio',4,'p_aleatorio','SintacticAnalizer.py',244),
  ('Mover -> MOVER PARENTESIS_IZQ paramMover PARENTESIS_DER PUNTOCOMA','Mover',5,'p_mover','SintacticAnalizer.py',253),
  ('paramMover -> AF','paramMover',1,'p_ParamMover','SintacticAnalizer.py',262),
  ('paramMover -> F','paramMover',1,'p_ParamMover','SintacticAnalizer.py',263),
  ('paramMover -> DFA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',264),
  ('paramMover -> IFA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',265),
  ('paramMover -> DFB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',266),
  ('paramMover -> IFB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',267),
  ('paramMover -> A','paramMover',1,'p_ParamMover','SintacticAnalizer.py',268),
  ('paramMover -> DAA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',269),
  ('paramMover -> IAA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',270),
  ('paramMover -> DAB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',271),
  ('paramMover -> IAB','paramMover',1,'p_ParamMover','SintacticAnalizer.py',272),
  ('paramMover -> AA','paramMover',1,'p_ParamMover','SintacticAnalizer.py',273),
  ('funcionAlge -> INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion','funcionAlge',8,'p_funcion_Alge','SintacticAnalizer.py',280),
  ('funcionAlge -> DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion','funcionAlge',8,'p_funcion_Alge','SintacticAnalizer.py',281),
  ('funcionAlge -> INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA expresion','funcionAlge',8,'p_funcion_Alge','SintacticAnalizer.py',282),
  ('funcionAlge -> INC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge2','SintacticAnalizer.py',290),
  ('funcionAlge -> DEC PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge2','SintacticAnalizer.py',291),
  ('funcionAlge -> INI PARENTESIS_IZQ ID COMA sentencia PARENTESIS_DER PUNTOCOMA','funcionAlge',7,'p_funcion_Alge2','SintacticAnalizer.py',292),
  ('procedimiento -> PROC ID PARENTESIS_IZQ parametro PARENTESIS_DER INICIOPROC DOSPUNTOS expresion FINPROC PUNTOCOMA procedimiento','procedimiento',11,'p_procedimiento','SintacticAnalizer.py',301),
  ('procedimiento -> empty empty empty empty empty empty empty empty empty empty empty','procedimiento',11,'p_procedimiento','SintacticAnalizer.py',302),
  ('parametro -> ID COMA parametro','parametro',3,'p_parametro','SintacticAnalizer.py',314),
  ('parametro -> ID empty empty','parametro',3,'p_parametro','SintacticAnalizer.py',315),
  ('parametro -> NUMERO COMA parametro','parametro',3,'p_parametro','SintacticAnalizer.py',316),
  ('parametro -> NUMERO empty empty','parametro',3,'p_parametro','SintacticAnalizer.py',317),
  ('parametro -> empty empty empty','parametro',3,'p_parametro','SintacticAnalizer.py',318),
  ('llamarProc -> LLAMAR ID PARENTESIS_IZQ parametro PARENTESIS_DER PUNTOCOMA','llamarProc',6,'p_llamarProc','SintacticAnalizer.py',328),
  ('empty -> <empty>','empty',0,'p_empty','SintacticAnalizer.py',335),
]
