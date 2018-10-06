grammar Boltun;

options {
}

@parser::header {
import ast
import logging

from antlr4 import *

from .nodes import AliasNode, CallNode, ChoiceNode, CommentNode, ContentNode, \
    DataNode, Filter, IntentNode, RootNode, SlotNode
from ...util.collections import Stack

logger = logging.getLogger(__name__)
}

@parser::members {

@property
def node_stack(self):
    try:
        return self._node_stack
    except AttributeError:
        self._node_stack = Stack()
        self._node_stack.push(RootNode())
        return self._node_stack
}


@lexer::header{

import re
import importlib
import logging

from antlr4 import *

from Queue import Empty, LifoQueue
from collections import defaultdict

logger = logging.getLogger(__name__)
}

@lexer::members {

@property
def state(self):
    try:
        return self._state
    except AttributeError:
        self._state = defaultdict(bool)
        return self._state

@property
def bracket_queue(self):
    try:
        return self._bracket_queue
    except AttributeError:
        self._bracket_queue = LifoQueue()
        return self._bracket_queue

def open_bracket(self, current):
    self.bracket_queue.put(current)

def close_bracket(self, expected):
    if self.bracket_queue.get() == expected:
        return True
    return None


def reset(self):
    super(BoltunLexer, self).reset()
    self.state['tag'] = False
    self.state['choice'] = False
    self.state['comment'] = False
    while not self.bracket_queue.empty():
        try:
            self.bracket_queue.get(False)
        except Empty:
            continue
    self.bracket_queue.task_done()
}

document : (polyadic_tag | content)* EOF?;

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
self.node_stack.peek().add_child(content_node)

} :
    ( unary_tag
    | data
    )+
    ;

data: var_chars+=DATA+
{
data_str = ''.join([c.text for c in $var_chars])
self.node_stack.peek().add_child(DataNode(data_str))
} ;

polyadic_tag : choice_tag ;

unary_tag : entity_tag | call_tag | comment_tag ;

choice_tag
    locals []
@init
{

choice_node = ChoiceNode()
self.node_stack.push(choice_node)

}
@after
{

choice_node = self.node_stack.pop()
self.node_stack.peek().add_child(choice_node)

} :
    LL_BRACE
    var_content_choises+=content?
    (
        DOUBLE_PIPE
        var_content_choises+=content?
    )*?
    RR_BRACE
    ;

entity_tag
    locals []
    @init {}
    @after {}
    :
    LL_BRACK
    var_type=entity_type
    name=NAME
    (HASH var_ref_names+=NAME (HASH var_ref_names+=NAME)*)?
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

self.node_stack.peek().add_child(node)
} ;

entity_type : ENTITY_TYPE ;

call_tag
    locals []
    @init {}
    @after {}
    :
    LL_BRACK
    GREATER
    name=NAME
    var_optional=QUESTION?
    var_attr=attr
    var_optional=QUESTION?
    var_fltrs+=fltr*
    RR_BRACK
{
args = $ctx.var_attr.__data__.get('args', None)
kwargs = $ctx.var_attr.__data__.get('kwargs', None)

name=$name.text
optional=$var_optional is not None
node = CallNode(name, optional, args, kwargs)

for fltr in $var_fltrs:
    name = fltr.__data__.get('name')
    args = fltr.__data__.get('args')
    kwargs = fltr.__data__.get('kwargs')

    node.add_filter(Filter(name, args, kwargs))

self.node_stack.peek().add_child(node)
} ;

fltr
    locals []
    @init {}
    @after {}
    : PIPE var_name=NAME var_optional=QUESTION? var_attr=attr? var_optional=QUESTION?
{

$ctx.__data__ = {
    'name' : $ctx.var_name.text,
    'optional': $var_optional is not None,
    'args' : $ctx.var_attr.__data__.get('args') if $ctx.var_attr else [],
    'kwargs' : $ctx.var_attr.__data__.get('kwargs') if $ctx.var_attr else {}
}

} ;

attr
    locals [__data__=dict()]
    @init {}
    @after {}
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

attr_arg_def
    locals [__data__=dict()]
    : var_value=attr_value
{

$ctx.__data__ = {
    'value': $ctx.var_value.__data__.get('content')
}

} ;

attr_kw_arg_def
    locals [__data__=dict()]
    : var_name=NAME EQUAL var_value=attr_value
{

$ctx.__data__ = {
    'name': $ctx.var_name.text,
    'value': $ctx.var_value.__data__.get('content')
}

} ;

attr_value
    locals [__data__=dict()]
    : var_content=(BOOL | NUMBER | STRING)
{

$ctx.__data__ = {
    'content': ast.literal_eval($ctx.var_content.text)
}

} ;

comment_tag
    locals [__data__=dict()]
    @init {}
    @after {}
    :
    LL_COMMENT_BRACK
    var_chars+=COMMENT_DATA*?
    RR_COMMENT_BRACK
{

content = data_str = ''.join([c.text for c in $var_chars])
$ctx.__data__ = {
    'content' : content
}

self.node_stack.peek().add_child(CommentNode(content))

} ;

LL_BRACK : 
    {not self.state['tag'] and not self.state['comment']}? 
    '[['
{
self.open_bracket(current='[[')
self.state['tag'] = True
} ;

RR_BRACK : 
    {self.state['tag'] and not self.state['comment']}? 
    ']]'
{
self.close_bracket(expected='[[')
self.state['tag'] = False
} ;

LL_COMMENT_BRACK : 
    {not self.state['tag'] and not self.state['comment']}? 
    '[[#'
{
self.open_bracket(current='[[')
self.state['tag'] = True
self.state['comment'] = True
} ;

RR_COMMENT_BRACK : 
    {self.state['tag'] and self.state['comment']}? 
    ']]'
{
self.close_bracket(expected='[[')
self.state['tag'] = False
self.state['comment'] = False
} ;

L_BRACK  : '['
{
self.open_bracket(current='[')
} ;

R_BRACK  : ']'
{
self.close_bracket(expected='[')
} ;

LL_PAREN : '(('
{
self.open_bracket(current='((')
} ;

RR_PAREN : '))'
{
self.close_bracket(expected='((')
} ;

L_PAREN  : '('
{
self.open_bracket(current='(')
} ;

R_PAREN  : ')'
{
self.close_bracket(expected='(')
} ;

LL_BRACE : '{{'
{
self.open_bracket(current='{{')
self.state['choice'] = True
} ;

RR_BRACE : '}}'
{
self.close_bracket(expected='{{')
self.state['choice'] = False
} ;

L_BRACE : '{'
{
self.open_bracket(current='{')
} ;

R_BRACE : '}'
{
self.close_bracket(expected='{')
} ;

ENTITY_TYPE : {self.state['tag'] and not self.state['comment']}? (PERCENT | TILDA | COMMAT);
COMMENT_DATA : {self.state['tag'] and self.state['comment']}? . ;

BOOL         : {self.state['tag'] and not self.state['comment']}? 'True' | 'False' ;
NUMBER       : {self.state['tag'] and not self.state['comment']}? INT_NUMBER | FLOAT_NUMBER ;
INT_NUMBER   : {self.state['tag'] and not self.state['comment']}? ('0'..'9')+ ;
FLOAT_NUMBER : {self.state['tag'] and not self.state['comment']}? INT_NUMBER+ DOT INT_NUMBER* ;

STRING :
        {self.state['tag'] and not self.state['comment']}?
        ( '\'' ( STRING_ESC_SEQ | ~[\\\r\n\f'] )* '\''
        | '"' ( STRING_ESC_SEQ | ~[\\\r\n\f"] )* '"'
        )
       ;
fragment STRING_ESC_SEQ : '\\' .;

DOUBLE_PIPE : {self.state['choice'] and not self.state['tag']}? '||' ;
PIPE        : {self.state['tag']}? '|' ;

WS	         : {self.state['tag'] and not self.state['comment']}?
               ( '\t' | ' ' | '\r' | '\n'| '\u000C' )+
               -> channel(HIDDEN) ;
NAME         :
    {self.state['tag'] and not self.state['comment']}?
    NAME_LETTERS+
    ( NAME_LETTERS
    | NAME_NUMBERS
    )*
    ;
fragment NAME_LETTERS : 'a'..'z' | 'A'..'Z' | '_' | '-';
fragment NAME_NUMBERS : '0'..'9';

DATA         : {not self.state['tag']}? . ;

SLASH    : {self.state['tag']}? '/' ;
AMP	     : {self.state['tag']}? '&' ;
HASH	 : {self.state['tag']}? '#' ;
GREATER  : {self.state['tag']}? '>' ;
HAT	     : {self.state['tag']}? '^' ;
EQUAL    : {self.state['tag']}? '=' ;
BANG     : {self.state['tag']}? '!' ;
DOT      : {self.state['tag']}? '.' ;
COMMA    : {self.state['tag']}? ',' ;
PERCENT  : {self.state['tag']}? '%' ;
TILDA    : {self.state['tag']}? '~' ;
COMMAT   : {self.state['tag']}? '@' ;
QUESTION : {self.state['tag']}? '?' ;

UNKNOWN : . ;