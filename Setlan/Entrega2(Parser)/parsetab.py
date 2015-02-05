
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '$\xd8\x82P\x94}\x83&Y\x93\xd1\x9c3r\x01\xd2'
    
_lr_action_items = {'ASTERISK':([2,3,4,10,11,12,13,14,],[-7,5,5,5,5,5,5,5,]),'INTDIVISION':([2,3,4,10,11,12,13,14,],[-7,6,6,6,6,6,6,6,]),'DASH':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,],[1,1,-7,7,7,1,1,1,1,1,7,7,7,7,7,]),'PLUS':([2,3,4,10,11,12,13,14,],[-7,8,8,8,8,8,8,8,]),'INTEGER':([0,1,5,6,7,8,9,],[2,2,2,2,2,2,2,]),'$end':([2,3,4,10,11,12,13,14,],[-7,0,-6,-5,-3,-2,-1,-4,]),'RESTDIVISION':([2,3,4,10,11,12,13,14,],[-7,9,9,9,9,9,9,9,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,1,5,6,7,8,9,],[3,4,10,11,12,13,14,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binary','C:\\Users\\manuggz\\Setlan\\Setlan\\Entrega2(Parser)\\parser.py',15),
  ('expression -> expression DASH expression','expression',3,'p_expression_binary','C:\\Users\\manuggz\\Setlan\\Setlan\\Entrega2(Parser)\\parser.py',16),
  ('expression -> expression INTDIVISION expression','expression',3,'p_expression_binary','C:\\Users\\manuggz\\Setlan\\Setlan\\Entrega2(Parser)\\parser.py',17),
  ('expression -> expression RESTDIVISION expression','expression',3,'p_expression_binary','C:\\Users\\manuggz\\Setlan\\Setlan\\Entrega2(Parser)\\parser.py',18),
  ('expression -> expression ASTERISK expression','expression',3,'p_expression_binary','C:\\Users\\manuggz\\Setlan\\Setlan\\Entrega2(Parser)\\parser.py',19),
  ('expression -> DASH expression','expression',2,'p_expression_unary','C:\\Users\\manuggz\\Setlan\\Setlan\\Entrega2(Parser)\\parser.py',23),
  ('expression -> INTEGER','expression',1,'p_integer','C:\\Users\\manuggz\\Setlan\\Setlan\\Entrega2(Parser)\\parser.py',27),
]