#--------------------------------------
# Programming Language: mathpy.py
# Orientation: numerical calculations
# Author: Sharif Nasser Kadamani
# ID: A00820367
# This is the lexer with python lex
#--------------------------------------
import ply.lex as lex

# List of tokens
tokens = [
	'ID', 'STRING', 'FLOAT', 'INT',
	'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
	'ASSIGN', 'LPAREN', 'RPAREN',
	'EQ', 'NEQ', 'LT', 'LTE', 'GT', 'GTE',
	'DOT', 'COMMA', 'COLON', 'SEMICOLON', 'COMMENT'
]

reserved = {
	'program' : 'PROGRAM',
	'end' : 'END',
	'integer' : 'INTEGER',
	'real' : 'REAL',
	'subroutine' : 'SUBROUTINE',
	'if' : 'IF',
	'then' : 'THEN',
	'else' : 'ELSE',
	'do' : 'DO',
	'exit' : 'EXIT',
	'read' : 'READ',
	'print' : 'PRINT',
	'or' : 'OR',
	'and' : 'AND'
}

tokens = tokens + list(reserved.values())

# Regular expressions for simple tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ASSIGN = r'='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EQ = r'=='
t_NEQ = r'/='
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_DOT = r'\.'
t_COMMA = r','
t_COLON = r':'
t_SEMICOLON = r';'

# Ignored characters (spaces and tabs)
t_ignore = ' \t'

# Regular expression rules definition
def t_COMMENT(t):
	r'\!.*'
	pass
	# No return value. Token discarded

def t_ID(t):
	r'[a-zA-Z][a-zA-Z0-9_]*'
	t.type = reserved.get(t.value, 'ID') # Check for reserved
	return t

def t_STRING(t):
	r'".*"'
	#r'[\"][a-zA-Z_]*[a-zA-Z0-9_ ]*[\"]'
	return t

def t_FLOAT(t):
	r'\d+\.\d+'
	t.value = float(t.value)
	return t

def t_INT(t):
	r'\d+'
	t.value = int(t.value)
	return t

# Compute column whit the input text string and a token instance
def find_column(input, token):
	line_start = input.rfind('\n', 0, token.lexpos) + 1
	return(token.lexpos - line_start) + 1

# Rule to track line numbers
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
	print("Illegal character '%s'" % t.value[0])
	t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

"""
# Test the lexer
while True:
	# Give lexer some input
	lexer.input(input(''))
	# Tokenize
	while True:
		tok = lexer.token()
		if not tok:
			break	# No more input
		print(tok)
"""