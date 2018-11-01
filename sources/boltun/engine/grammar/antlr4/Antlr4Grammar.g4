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

def _in(self, state):
    self._state[state] += 1

def _out(self, state):
    self._state[state] -= 1

def _is(self, state):
    return self._state[state] > 0

def _not(self, state):
    return self._state[state] == 0

def _reset_all_states(self):
    del self.__state

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
    super(Antlr4GrammarLexer, self).reset()

    self._reset_all_states()
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
        polyadic_tag
        |
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
    var_data=STRING?
    var_optional=QUESTION?
    (PIPE var_fltr_chain=fltr_chain)?
    RR_TEXT_BRACK
{

data=ast.literal_eval($var_data.text) if $var_data else None
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
    (DOT var_ref_names+=NAME)*
    var_optional=QUESTION?
    var_attr=attr
    var_optional=QUESTION?
    (PIPE var_fltr_chain=fltr_chain)?
    RR_CALL_BRACK
{

name=$var_name.text
ref_names=[v.text for v in $var_ref_names]
optional=$var_optional is not None
arg_params = $ctx.var_attr.__data__.get('arg_params', None)
kwarg_params = $ctx.var_attr.__data__.get('kwarg_params', None)

node = CallNode(name=name, ref_names=ref_names, optional=optional,
                arg_params=arg_params, kwarg_params=kwarg_params)

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
    (DOT var_ref_names+=NAME)*
    var_optional=QUESTION?
    var_attr=attr?
    var_optional=QUESTION?
{

$ctx.__data__ = {
    'name' : $var_name.text,
    'ref_names': [v.text for v in $var_ref_names],
    'optional': $var_optional is not None,

    'arg_params' : $ctx.var_attr.__data__.get('arg_params') \
                   if $ctx.var_attr else [],

    'kwarg_params' : $ctx.var_attr.__data__.get('kwarg_params') \
                     if $ctx.var_attr else {}
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
    ref_names = fltr_def.__data__.get('ref_names')
    arg_params = fltr_def.__data__.get('arg_params')
    kwarg_params = fltr_def.__data__.get('kwarg_params')

    filter_ = NodeFilter(name=name, ref_names=ref_names, optional=optional,
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
    'value': $ctx.var_value.__data__.get('value')
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
    'value': $ctx.var_value.__data__.get('value')
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
    'value': content
}

} ;

// ======================= ATTRIBUTES ARG SINGLE VALUE ========================

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

// ======================== ATTRIBUTES ARG LIST VALUE =========================

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
    var_values+=attr_value?
    (
        COMMA var_values+=attr_value
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

content = ''.join([c.text for c in $var_chars]) \
                        if $var_chars else None

$ctx.__data__ = {
    'content' : content
}

node = CommentNode(content=content)
node.start = self._get_start_pos($ctx)
node.stop = self._get_stop_pos($ctx)

} ;

// ================================ LEXER RULES ===============================


LLL_BRACE : '{{{'
{
self._open_bracket(current='{{{')
self._in(state='choice_short')
} ;
RRR_BRACE : '}}}'
{
self._close_bracket(expected='{{{')
self._out(state='choice_short')
} ;

LL_BRACE : '{{'
{
self._open_bracket(current='{{')
self._in(state='choice')
} ;

RR_BRACE : '}}'
{
self._close_bracket(expected='{{')
self._out(state='choice')
} ;

LL_TEXT_BRACK : { self._not(state='tag') \
                  and self._not(state='attr') \
                  and self._not(state='list') \
                  and self._not(state='comment') }?
                '[['
{
self._open_bracket(current='[[')
self._in(state='tag')
} ;

RR_TEXT_BRACK : { self._is(state='tag') \
                  and self._not(state='comment') \
                  and self._not(state='attr') \
                  and self._not(state='list') }?
                ']]'
{
self._close_bracket(expected='[[')
self._out(state='tag')
} ;

LL_CALL_BRACK : { self._not(state='tag') \
                  and self._not(state='comment') }?
                '[%'
{
self._open_bracket(current='[[')
self._in(state='tag')
} ;

RR_CALL_BRACK : { self._is(state='tag') \
                  and self._not(state='comment') }?
                '%]'
{
self._close_bracket(expected='[[')
self._out(state='tag')
} ;

LL_COMMENT_BRACK : { self._not(state='tag') \
                     and self._not(state='comment') }?
                   '[#'
{
self._open_bracket(current='[[')
self._in(state='tag')
self._in(state='comment')
} ;

RR_COMMENT_BRACK : { self._is(state='tag') \
                     and self._is(state='comment') }?
                   '#]'
{
self._close_bracket(expected='[[')
self._out(state='tag')
self._out(state='comment')
} ;

L_PAREN  : { self._not(state='comment') }?
           '('
{
self._open_bracket(current='(')
self._in(state='attr')
} ;

R_PAREN  : { self._not(state='comment') }?
           ')'
{
self._close_bracket(expected='(')
self._out(state='attr')
} ;

L_BRACK : { self._is(state='attr') \
            and self._not(state='comment') }?
          '['
{
self._open_bracket(current='[')
self._in(state='list')
} ;

R_BRACK : { self._is(state='attr') \
            and self._not(state='comment') }?
          ']'
{
self._close_bracket(expected='[')
self._out(state='list')
} ;

BOOL         : {self._is(state='tag') and self._not(state='comment')}?
               'True' | 'False' ;

NUMBER       : {self._is(state='tag') and self._not(state='comment')}?
               INT_NUMBER | FLOAT_NUMBER ;

INT_NUMBER   : {self._is(state='tag') and self._not(state='comment')}?
               ('0'..'9')+ ;

FLOAT_NUMBER : {self._is(state='tag') and self._not(state='comment')}?
               INT_NUMBER+ DOT INT_NUMBER* ;

STRING       : {self._is(state='tag') and self._not(state='comment')}?
             (
                '\'' ( STRING_ESC_SEQ | ~[\\\r\n\f'] )* '\''
                |
                '"' ( STRING_ESC_SEQ | ~[\\\r\n\f"] )* '"'
             ) ;


fragment STRING_ESC_SEQ : '\\' . ;


WS_SKIP	     : {self._is(state='tag') and self._not(state='comment')}?
               WS+ -> channel(HIDDEN) ;

fragment WS  : '\t' | ' ' | '\r' | '\n'| '\u000C' ;

NAME         : {self._is(state='tag') and self._not(state='comment')}?
               NAME_LETTERS+
               (
                    NAME_LETTERS
                    |
                    NAME_NUMBERS
               )*
               ;
fragment NAME_LETTERS : 'a'..'z' | 'A'..'Z' | '_' | '-';
fragment NAME_NUMBERS : '0'..'9';


COMMENT_DATA : {self._is(state='tag') and self._is(state='comment')}? . ;
DATA         : {self._not(state='tag')}? . ;

DOUBLE_PIPE  : {self._is(state='choice') and self._not(state='tag')}? '||' ;
PIPE         : {self._is(state='tag')}? '|' ;
SLASH        : {self._is(state='tag')}? '/' ;
AMP	         : {self._is(state='tag')}? '&' ;
HASH	     : {self._is(state='tag')}? '#' ;
GREATER      : {self._is(state='tag')}? '>' ;
HAT	         : {self._is(state='tag')}? '^' ;
EQUAL        : {self._is(state='tag')}? '=' ;
BANG         : {self._is(state='tag')}? '!' ;
DOT          : {self._is(state='tag')}? '.' ;
COMMA        : {self._is(state='tag')}? ',' ;
PERCENT      : {self._is(state='tag')}? '%' ;
TILDA        : {self._is(state='tag')}? '~' ;
COMMAT       : {self._is(state='tag')}? '@' ;
QUESTION     : {self._is(state='tag')}? '?' ;

UNKNOWN      : . ;