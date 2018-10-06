grammar Boltun;

options {
}

@parser::header {

import ast
import logging

from antlr4 import *

from .node import AliasNode, CallNode, ChoiceNode, CommentNode, ContentNode, \
    DataNode, Filter, IntentNode, RootNode, SlotNode
from ...util.collections import Stack

logger = logging.getLogger(__name__)

}

@parser::members {

def parse(self):
    self.reset()
    self.document()

    root_node = self._node_stack.pop()
    return root_node

@property
def _node_stack(self):
    try:
        return self.__node_stack
    except AttributeError:
        self.__node_stack = Stack()
        self.__node_stack.push(RootNode())
        return self.__node_stack

def _get_start_pos(self, ctx):
    if not ctx:
        return None
    return ctx.start.start if ctx.start else None

def _get_stop_pos(self, ctx):
    if not ctx:
        return None
    return ctx.stop.stop if ctx.stop else None

}


@lexer::header {

import logging

from Queue import Empty, LifoQueue
from collections import defaultdict

logger = logging.getLogger(__name__)

}

@lexer::members {

@property
def _state(self):
    try:
        return self.__state
    except AttributeError:
        self.__state = defaultdict(bool)
        return self.__state

@property
def _bracket_queue(self):
    try:
        return self.__bracket_queue
    except AttributeError:
        self.__bracket_queue = LifoQueue()
        return self.__bracket_queue

def _open_bracket(self, current):
    self._bracket_queue.put(current)

def _close_bracket(self, expected):
    if self._bracket_queue.get() == expected:
        return True
    return None

def reset(self):
    super(BoltunLexer, self).reset()
    self._state['tag'] = False
    self._state['choice'] = False
    self._state['comment'] = False
    while not self._bracket_queue.empty():
        try:
            self._bracket_queue.get(False)
        except Empty:
            continue
    self._bracket_queue.task_done()

}

// =============================== DOCUMENT ROOT ==============================

document
locals []
@init
{

content_node = ContentNode()
self._node_stack.push(content_node)

}
@after
{

root_node = self._node_stack.peek()
root_node.start = self._get_start_pos($ctx)
root_node.stop = self._get_stop_pos($ctx)

}
    :
    (
        polyadic_tag
        |
        content
    )*
    EOF?
    ;


// ================================== CONTENT =================================

content
locals []
@init
{

content_node = ContentNode()
self._node_stack.push(content_node)

}
@after
{

content_node = self._node_stack.pop()
content_node.start = self._get_start_pos($ctx)
content_node.stop = self._get_stop_pos($ctx)

self._node_stack.peek().add_child(content_node)

}
    :
    (
        unary_tag
        |
        data
    )+
    ;

// =================================== DATA ===================================

data
locals []
@init
{

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self._node_stack.peek().add_child(node)

}
    :
    var_chars+=DATA+
{

data_str = ''.join([c.text for c in $var_chars])

node = DataNode(data_str)

} ;

// =============================== POLYADIC TAG ===============================

polyadic_tag : choice_tag | choice_short_tag;

// ================================= UNARY TAG ================================

unary_tag : entity_tag | call_tag | comment_tag ;

// ================================ CHOICE TAG ================================

choice_tag
locals []
@init
{

choice_node = ChoiceNode()
self._node_stack.push(choice_node)

}
@after
{

choice_node = self._node_stack.pop()
choice_node.start = self._get_start_pos($ctx)
choice_node.stop = self._get_stop_pos($ctx)

self._node_stack.peek().add_child(choice_node)

}
    :
    LL_BRACE
    var_content_choises+=content?
    (
        DOUBLE_PIPE
        var_content_choises+=content?
    )*?
    RR_BRACE
{

} ;

// ============================= CHOICE SHORT TAG =============================

choice_short_tag
locals []
@init
{

node = ChoiceNode()

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)

for child_node in node.children:
    if not isinstance(child_node, (DataNode,)):
        continue
    child_node.start = node.start
    child_node.stop = node.stop

self._node_stack.peek().add_child(node)

}
    :
    LLL_BRACE
    var_chars+=DATA+
    RRR_BRACE
{

for c in $var_chars:
    node.add_child(DataNode(c.text))

}
;
// ================================ ENTITY TAG ================================

entity_tag
locals []
@init
{

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self._node_stack.peek().add_child(node)

}
    :
    LL_BRACK
    var_type=entity_type
    var_optional=QUESTION?
    name=NAME
    (
        HASH var_ref_names+=NAME
        (
            HASH var_ref_names+=NAME
        )*
    )?
    var_optional=QUESTION?
    var_fltrs+=fltr*?
    RR_BRACK
{

node_class = None

entity_type = $var_type.text
if entity_type == '%':
    node_class = IntentNode
elif entity_type == '~':
    node_class = AliasNode
elif entity_type == '@':
    node_class = SlotNode

name=$name.text
optional=$var_optional is not None
ref_names=[v.text for v in $ctx.var_ref_names]

node = node_class(name, ref_names, optional)


for fltr in $var_fltrs:
    name = fltr.__data__.get('name')
    optional = fltr.__data__.get('optional')
    args = fltr.__data__.get('args')
    kwargs = fltr.__data__.get('kwargs')
    node.add_filter(Filter(name, optional, args, kwargs))

} ;

// ================================ ENTITY TYPE ===============================

entity_type : ENTITY_TYPE ;

// ================================= CALL TAG =================================

call_tag
locals []
@init
{

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self._node_stack.peek().add_child(node)

}
    :
    LL_BRACK
    GREATER
    var_optional=QUESTION?
    name=NAME
    var_optional=QUESTION?
    var_attr=attr
    var_optional=QUESTION?
    var_fltrs+=fltr*
    RR_BRACK
{

name=$name.text
optional=$var_optional is not None
args = $ctx.var_attr.__data__.get('args', None)
kwargs = $ctx.var_attr.__data__.get('kwargs', None)

node = CallNode(name, optional, args, kwargs)

for fltr in $var_fltrs:
    name = fltr.__data__.get('name')
    args = fltr.__data__.get('args')
    kwargs = fltr.__data__.get('kwargs')

    node.add_filter(Filter(name, args, kwargs))

} ;

// ================================== FILTER ==================================

fltr
locals []
@init
{

}
@after
{

}
    :
    PIPE
    var_name=NAME
    var_optional=QUESTION?
    var_attr=attr?
    var_optional=QUESTION?
{

$ctx.__data__ = {
    'name' : $ctx.var_name.text,
    'optional': $var_optional is not None,
    'args' : $ctx.var_attr.__data__.get('args') if $ctx.var_attr else [],
    'kwargs' : $ctx.var_attr.__data__.get('kwargs') if $ctx.var_attr else {}
}

} ;

// ================================ ATTRIBUTES ================================

attr
locals [__data__=dict()]
@init
{

}
@after
{

}
    :
    L_PAREN
    (
        var_attr_kw_arg_defs+=attr_kw_arg_def
        (COMMA var_attr_kw_arg_defs+=attr_kw_arg_def)*
        |
        var_attr_arg_defs+=attr_arg_def
        (COMMA var_attr_arg_defs+=attr_arg_def)*
        (COMMA var_attr_kw_arg_defs+=attr_kw_arg_def)*
    )
    R_PAREN
{

$ctx.__data__ = {
    'args' : [
        v.__data__.get('value') for v in $ctx.var_attr_arg_defs
    ],
    'kwargs' : {
        v.__data__.get('name'): v.__data__.get('value')
        for v in $ctx.var_attr_kw_arg_defs
    }
}

} ;

// ========================= ATTRIBUTES ARG DEFINITION ========================

attr_arg_def
locals [__data__=dict()]
@init
{

}
@after
{

}
    :
    var_value=attr_value
{

$ctx.__data__ = {
    'value': $ctx.var_value.__data__.get('content')
}

} ;

// ======================= ATTRIBUTES KW_ARG DEFINITION =======================

attr_kw_arg_def
locals [__data__=dict()]
@init
{

}
@after
{

}
    :
    var_name=NAME
    EQUAL
    var_value=attr_value
{

$ctx.__data__ = {
    'name': $ctx.var_name.text,
    'value': $ctx.var_value.__data__.get('content')
}

} ;

// =========================== ATTRIBUTES ARG VALUE ===========================

attr_value
locals [__data__=dict()]
@init
{

}
@after
{

}
    :
    var_content=(BOOL | NUMBER | STRING)
{

$ctx.__data__ = {
    'content': ast.literal_eval($ctx.var_content.text)
}

} ;

// =============================== COMMENT TAG ================================

comment_tag
locals [__data__=dict()]
@init
{

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self._node_stack.peek().add_child(node)

}
    :
    LL_COMMENT_BRACK
    var_chars+=COMMENT_DATA*?
    RR_COMMENT_BRACK
{

content = data_str = ''.join([c.text for c in $var_chars])
$ctx.__data__ = {
    'content' : content
}

node = CommentNode(content)
node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)

} ;

// ================================ LEXER RULES ===============================

LL_BRACK : {not self._state['tag'] and not self._state['comment']}?
           '[['
{
self._open_bracket(current='[[')
self._state['tag'] = True
} ;

RR_BRACK : {self._state['tag'] and not self._state['comment']}?
           ']]'
{
self._close_bracket(expected='[[')
self._state['tag'] = False
} ;

LL_COMMENT_BRACK : {not self._state['tag'] and not self._state['comment']}?
                   '[[#'
{
self._open_bracket(current='[[')
self._state['tag'] = True
self._state['comment'] = True
} ;

RR_COMMENT_BRACK : {self._state['tag'] and self._state['comment']}?
                   ']]'
{
self._close_bracket(expected='[[')
self._state['tag'] = False
self._state['comment'] = False
} ;

L_BRACK  : '['
{
self._open_bracket(current='[')
} ;

R_BRACK  : ']'
{
self._close_bracket(expected='[')
} ;

LL_PAREN : '(('
{
self._open_bracket(current='((')
} ;

RR_PAREN : '))'
{
self._close_bracket(expected='((')
} ;

L_PAREN  : '('
{
self._open_bracket(current='(')
} ;

R_PAREN  : ')'
{
self._close_bracket(expected='(')
} ;

LLL_BRACE : '{{{'
{
self._open_bracket(current='{{{')
self._state['choice_short'] = True
} ;
RRR_BRACE : '}}}'
{
self._close_bracket(expected='{{{')
self._state['choice_short'] = False
} ;

LL_BRACE : '{{'
{
self._open_bracket(current='{{')
self._state['choice'] = True
} ;

RR_BRACE : '}}'
{
self._close_bracket(expected='{{')
self._state['choice'] = False
} ;

L_BRACE : '{'
{
self._open_bracket(current='{')
} ;

R_BRACE : '}'
{
self._close_bracket(expected='{')
} ;

ENTITY_TYPE  : {self._state['tag'] and not self._state['comment']}?
               (PERCENT | TILDA | COMMAT);

BOOL         : {self._state['tag'] and not self._state['comment']}?
               'True' | 'False' ;

NUMBER       : {self._state['tag'] and not self._state['comment']}?
               INT_NUMBER | FLOAT_NUMBER ;

INT_NUMBER   : {self._state['tag'] and not self._state['comment']}?
               ('0'..'9')+ ;

FLOAT_NUMBER : {self._state['tag'] and not self._state['comment']}?
               INT_NUMBER+ DOT INT_NUMBER* ;

STRING       : {self._state['tag'] and not self._state['comment']}?
             (
                '\'' ( STRING_ESC_SEQ | ~[\\\r\n\f'] )* '\''
                |
                '"' ( STRING_ESC_SEQ | ~[\\\r\n\f"] )* '"'
             )
       ;
fragment STRING_ESC_SEQ : '\\' .;


WS	         : {self._state['tag'] and not self._state['comment']}?
               ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+
               -> channel(HIDDEN) ;

NAME         : {self._state['tag'] and not self._state['comment']}?
               NAME_LETTERS+
               (
                    NAME_LETTERS
                    |
                    NAME_NUMBERS
               )*
               ;
fragment NAME_LETTERS : 'a'..'z' | 'A'..'Z' | '_' | '-';
fragment NAME_NUMBERS : '0'..'9';


COMMENT_DATA : {self._state['tag'] and self._state['comment']}? . ;
DATA         : {not self._state['tag']}? . ;

DOUBLE_PIPE  : {self._state['choice'] and not self._state['tag']}? '||' ;
PIPE         : {self._state['tag']}? '|' ;
SLASH        : {self._state['tag']}? '/' ;
AMP	         : {self._state['tag']}? '&' ;
HASH	     : {self._state['tag']}? '#' ;
GREATER      : {self._state['tag']}? '>' ;
HAT	         : {self._state['tag']}? '^' ;
EQUAL        : {self._state['tag']}? '=' ;
BANG         : {self._state['tag']}? '!' ;
DOT          : {self._state['tag']}? '.' ;
COMMA        : {self._state['tag']}? ',' ;
PERCENT      : {self._state['tag']}? '%' ;
TILDA        : {self._state['tag']}? '~' ;
COMMAT       : {self._state['tag']}? '@' ;
QUESTION     : {self._state['tag']}? '?' ;

UNKNOWN      : . ;