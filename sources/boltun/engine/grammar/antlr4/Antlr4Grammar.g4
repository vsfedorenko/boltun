grammar Antlr4Grammar;

options {
}

@parser::header {

import ast
import logging

from boltun.engine.grammar import RecognitionDisabledException
from boltun.util import Stack
from .Antlr4GrammarMode import Antlr4GrammarMode
from .node import NodeFilter
from .node.fork import ChoiceNode, ContentNode, RootNode
from .node.leaf import CallNode, CommentNode, DataNode

logger = logging.getLogger(__name__)

}

@parser::members {

@property
def recognition_mode(self):
    try:
        return self.__recognition_mode
    except AttributeError:
        self.__recognition_mode = Antlr4GrammarMode.CALL
        return self.__recognition_mode

@recognition_mode.setter
def recognition_mode(self, value):
    self.__recognition_mode = value

@property
def error_strategy(self):
    return self._errHandler

@error_strategy.setter
def error_strategy(self, value):
    self._errHandler = value

def _validate_recognition_mode(self, mode):
    if self.recognition_mode >= mode:
        return
    raise RecognitionDisabledException(mode=mode, recognizer=self)

@property
def node_stack(self):
    try:
        return self._node_stack
    except AttributeError:
        self._node_stack = Stack()
        return self._node_stack

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

root_node = RootNode()
self.node_stack.push(root_node)

}
@after
{

root_node = self.node_stack.peek()
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
self.node_stack.push(content_node)

}
@after
{

content_node = self.node_stack.pop()
content_node.start = self._get_start_pos($ctx)
content_node.stop = self._get_stop_pos($ctx)

self.node_stack.peek().add_child(content_node)

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

self._validate_recognition_mode(Antlr4GrammarMode.DATA)

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self.node_stack.peek().add_child(node)

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

unary_tag : data_filter_tag | call_tag | comment_tag ;

// ================================ CHOICE TAG ================================

choice_tag
locals []
@init
{

self._validate_recognition_mode(Antlr4GrammarMode.CALL)

choice_node = ChoiceNode()
self.node_stack.push(choice_node)

}
@after
{

choice_node = self.node_stack.pop()
choice_node.start = self._get_start_pos($ctx)
choice_node.stop = self._get_stop_pos($ctx)

self.node_stack.peek().add_child(choice_node)

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

self._validate_recognition_mode(Antlr4GrammarMode.CALL)

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

self.node_stack.peek().add_child(node)

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
// ============================= DATA FILTER TAG ==============================

data_filter_tag
locals []
@init
{

self._validate_recognition_mode(Antlr4GrammarMode.CALL)

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self.node_stack.peek().add_child(node)

}
    :
    LL_TEXT_BRACK
    var_optional=QUESTION?
    var_data=STRING
    var_optional=QUESTION?
    (PIPE var_fltr_chain=fltr_chain)?
    RR_TEXT_BRACK
{

data=ast.literal_eval($var_data.text)
optional=$var_optional is not None

node = DataNode(content=data, optional=optional)

if $ctx.var_fltr_chain:
    filters = $ctx.var_fltr_chain.__data__.get('filters', None)
    node.add_filters(filters)

} ;

// ================================= CALL TAG =================================

call_tag
locals []
@init
{

self._validate_recognition_mode(Antlr4GrammarMode.CALL)

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self.node_stack.peek().add_child(node)

}
    :
    LL_CALL_BRACK
    var_optional=QUESTION?
    var_name=NAME
    (DOT var_method_name=NAME)?
    var_optional=QUESTION?
    var_attr=attr
    var_optional=QUESTION?
    (PIPE var_fltr_chain=fltr_chain)?
    RR_CALL_BRACK
{

name=$var_name.text
optional=$var_optional is not None
method=$var_method_name.text
arg_params = $ctx.var_attr.__data__.get('arg_params', None)
kwarg_params = $ctx.var_attr.__data__.get('kwarg_params', None)

node = CallNode(name=name, optional=optional,
                method=method, arg_params=arg_params, kwarg_params=kwarg_params)

if $ctx.var_fltr_chain:
    filters = $ctx.var_fltr_chain.__data__.get('filters', None)
    node.add_filters(filters)

} ;

// ================================== FILTER ==================================

fltr
locals [__data__=dict()]
@init
{

}
@after
{

}
    :
    var_name=NAME
    (DOT var_method_name=NAME)?
    var_optional=QUESTION?
    var_attr=attr?
    var_optional=QUESTION?
{

$ctx.__data__ = {
    'name' : $var_name.text,
    'method': $var_method_name.text,
    'optional': $var_optional is not None,
    'arg_params' : $ctx.var_attr.__data__.get('arg_params') if $ctx.var_attr else [],
    'kwarg_params' : $ctx.var_attr.__data__.get('kwarg_params') if $ctx.var_attr else {}
}

} ;

// =============================== FILTER CHAIN ===============================

fltr_chain
locals [__data__=dict()]
@init
{

}
@after
{

}
    :
    var_fltrs+=fltr
    (PIPE var_fltrs+=fltr)*
{

filters = []

for fltr_def in $var_fltrs:
    name = fltr_def.__data__.get('name')
    optional = fltr_def.__data__.get('optional')
    method = fltr_def.__data__.get('method')
    arg_params = fltr_def.__data__.get('arg_params')
    kwarg_params = fltr_def.__data__.get('kwarg_params')

    filter_ = NodeFilter(name=name, method=method, optional=optional,
                         arg_params=arg_params, kwarg_params=kwarg_params)
    filters.append(filter_)

$ctx.__data__ = {
    'filters' : filters,
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
        var_attr_kw_arg_defs+=attr_kw_arg_def?
        (COMMA var_attr_kw_arg_defs+=attr_kw_arg_def)*
        |
        var_attr_arg_defs+=attr_arg_def?
        (COMMA var_attr_arg_defs+=attr_arg_def)*
        (COMMA var_attr_kw_arg_defs+=attr_kw_arg_def)*
    )
    R_PAREN
{

$ctx.__data__ = {
    'arg_params' : [
        v.__data__.get('value') for v in $ctx.var_attr_arg_defs
    ],
    'kwarg_params' : {
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
    (
        var_single_content=attr_single_value
        |
        var_list_content=attr_list_value
    )
{

content = None
if $ctx.var_single_content:
    content = $ctx.var_single_content.__data__.get('value')
elif $ctx.var_list_content:
    content = $ctx.var_list_content.__data__.get('values')

$ctx.__data__ = {
    'content': content
}

} ;


attr_single_value
locals [__data__=dict()]
@init
{

}
@after
{

}
    : var_value=(BOOL | NUMBER | STRING)
{

$ctx.__data__ = {
    'value': ast.literal_eval($var_value.text)
}

} ;

attr_list_value
locals [__data__=dict()]
@init
{

}
@after
{

}
    :
    L_BRACK
    var_values+=attr_single_value?
    (
        COMMA var_values+=attr_single_value
    )*
    R_BRACK
{

$ctx.__data__ = {
    'values': [v.__data__.get('value') for v in $var_values]
}

} ;

// =============================== COMMENT TAG ================================

comment_tag
locals [__data__=dict()]
@init
{

self._validate_recognition_mode(Antlr4GrammarMode.DATA)

}
@after
{

node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)
self.node_stack.peek().add_child(node)

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

LL_TEXT_BRACK : {not self._state['tag'] and not self._state['comment']}?
           '[['
{
self._open_bracket(current='[[')
self._state['tag'] = True
} ;

RR_TEXT_BRACK : {self._state['tag'] and not self._state['comment']}?
           ']]'
{
self._close_bracket(expected='[[')
self._state['tag'] = False
} ;

LL_CALL_BRACK : {not self._state['tag'] and not self._state['comment']}?
           '[%'
{
self._open_bracket(current='[[')
self._state['tag'] = True
} ;

RR_CALL_BRACK : {self._state['tag'] and not self._state['comment']}?
           '%]'
{
self._close_bracket(expected='[[')
self._state['tag'] = False
} ;

LL_COMMENT_BRACK : {not self._state['tag'] and not self._state['comment']}?
                   '[#'
{
self._open_bracket(current='[[')
self._state['tag'] = True
self._state['comment'] = True
} ;

RR_COMMENT_BRACK : {self._state['tag'] and self._state['comment']}?
                   '#]'
{
self._close_bracket(expected='[[')
self._state['tag'] = False
self._state['comment'] = False
} ;

L_PAREN  : '('
{
self._open_bracket(current='(')
self._state['attr'] = True
} ;

R_PAREN  : ')'
{
self._close_bracket(expected='(')
self._state['attr'] = False
} ;

L_BRACK : {self._state['attr']}?
          '['
{
self._open_bracket(current='[')
self._state['list'] = True
} ;

R_BRACK : {self._state['attr']}?
          ']'
{
self._close_bracket(expected='[')
self._state['list'] = False
} ;

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
             ) ;


fragment STRING_ESC_SEQ : '\\' .;


WS_SKIP	     : {self._state['tag'] and not self._state['comment']}?
               WS+ -> channel(HIDDEN) ;

fragment WS  : '\t' | ' ' | '\r' | '\n'| '\u000C' ;

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