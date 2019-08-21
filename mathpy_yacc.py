#--------------------------------------
# Programming Language: mathpy.py
# Orientation: numerical calculations
# Author: Sharif Nasser Kadamani
# ID: A00820367
# This is the parser with python yacc
#--------------------------------------
import ply.yacc as yacc

# Symbol Table
symbolTable = {}
procedureTable = {}
var_type = ""
memory = [x for x in range (0, 1001)]

# Intermediate Code Generation
operands = []
temporal = [x for x in range(1000, 499, -1)]

# Translation and Execution
execution = []
jump_list = []
pc = 0

quadruple_counter = 0

def executer(execution):
	executer_list = []
	global pc
	while True:
		instruction = execution[pc]
		if (instruction[0] == 'goto'):
			pc = int(instruction[1])
		elif (instruction[0] == 'gotoF'):
			if(memory[int(instruction[1])] == False):
				pc = int(instruction[2])
			else:
				pc = pc + 1
		elif (instruction[0] == 'gotoT'):
			if(memory[int(instruction[1])]):
				pc = int(instruction[2])
			else:
				pc = pc + 1
		elif (instruction[0] == 'gotoP'):
			executer_list.append(pc+1)
			pc = int(instruction[1])
		elif (instruction[0] == 'return'):
			pc = executer_list.pop()
		elif (instruction[0] == 'print'):
			op2 = str(instruction[1])
			if (',' in op2):
				in1 = op2[op2.find('(')+1: op2.find(',')]
				in2 = op2[op2.find(',')+1: op2.find(')')]
				if (in1 in symbolTable):
					in1 = memory[list(symbolTable.keys()).index(in1)]
				if (in2 in symbolTable):
					in2 = memory[list(symbolTable.keys()).index(in2)]
				n_op2 = op2[0:op2.find('(')] + '(' + str(in1) + ',' + str(in2) + ')'
				op2 = memory[list(symbolTable.keys()).index(n_op2)]
			elif (op2.endswith(')') or op2.endswith(')c')):
			 	ind = op2[op2.find('(')+1: op2.find(')')]
			 	if (ind in symbolTable):
			 		ind = memory[list(symbolTable.keys()).index(ind)]
			 	n_op2 = op2[0:op2.find('(')] + '(' + str(ind) + ')'
			 	op2 = memory[list(symbolTable.keys()).index(n_op2)]
			elif(op2.endswith('c')):
				op2 = int(op2[0: len(op2)-1])
			elif(str(op2).isdigit()):
				op2 = memory[int(op2)]
			elif(not str(op2).endswith('"')): 
				op2 = memory[int(op2)]
			print(op2)
			pc += 1
		elif (instruction[0] == 'read'):
			memory[int(instruction[1])] = int(input())
			pc += 1
		elif (len(instruction) == 4):
			opcode = instruction[0]
			op2 = instruction[1]
			op1 = instruction[2]
			dir = memory

			if (',' in op2):
				in1 = op2[op2.find('(')+1: op2.find(',')]
				in2 = op2[op2.find(',')+1: op2.find(')')]
				if (in1 in symbolTable):
					in1 = memory[list(symbolTable.keys()).index(in1)]
				if (in2 in symbolTable):
					in2 = memory[list(symbolTable.keys()).index(in2)]
				n_op2 = op2[0:op2.find('(')] + '(' + str(in1) + ',' + str(in2) + ')'
				op2 = memory[list(symbolTable.keys()).index(n_op2)]
			elif (op2.endswith(')') or op2.endswith(')c')):
			 	ind = op2[op2.find('(')+1: op2.find(')')]
			 	if (ind in symbolTable):
			 		ind = memory[list(symbolTable.keys()).index(ind)]
			 	n_op2 = op2[0:op2.find('(')] + '(' + str(ind) + ')'
			 	op2 = memory[list(symbolTable.keys()).index(n_op2)]
			elif(str(op2).endswith('c')):
				op2 = int(op2[0: len(op2)-1])
			else:
				op2 = memory[int(op2)]

			if(',' in op1):
				in1 = op1[op1.find('(')+1: op1.find(',')]
				in2 = op1[op1.find(',')+1: op1.find(')')]
				if (in1 in symbolTable):
					in1 = memory[list(symbolTable.keys()).index(in1)]
				if (in2 in symbolTable):
					in2 = memory[list(symbolTable.keys()).index(in2)]
				n_op1 = op1[0:op1.find('(')] + '(' + str(in1) + ',' + str(in2) + ')'
				op1 = memory[list(symbolTable.keys()).index(n_op1)]
			elif (op1.endswith(')' or op1.endswith(')c'))):
			 	ind = op1[op1.find('(')+1: op1.find(')')]
			 	if (ind in symbolTable):
			 		ind = memory[list(symbolTable.keys()).index(ind)]
			 	n_op1 = op1[0:op1.find('(')] + '(' + str(ind) + ')'
			 	op1 = memory[list(symbolTable.keys()).index(n_op1)]
			elif(str(op1).endswith('c')):
				op1 = int(op1[0: len(op1)-1])
			elif (opcode == '='):
				op1 = ''
			else:
				op1 = memory[int(op1)]

			if(',' in str(instruction[3])):
				in1 = instruction[3][instruction[3].find('(')+1: instruction[3].find(',')]
				in2 = instruction[3][instruction[3].find(',')+1: instruction[3].find(')')]
				if (in1 in symbolTable):
					in1 = memory[list(symbolTable.keys()).index(in1)]
				if (in2 in symbolTable):
					in2 = memory[list(symbolTable.keys()).index(in2)]
				n_op = instruction[3][0:instruction[3].find('(')] + '(' + str(in1) + ',' + str(in2) + ')'
				instruction[3] = list(symbolTable.keys()).index(n_op)
			elif (str(instruction[3]).endswith(')') or str(instruction[3]).endswith(')c')):
			 	ind = instruction[3][instruction[3].find('(')+1: instruction[3].find(')')]
			 	if (ind in symbolTable):
			 		ind = memory[list(symbolTable.keys()).index(ind)]
			 	n_op = instruction[3][0:instruction[3].find('(')] + '(' + str(ind) + ')'
			 	instruction[3] = list(symbolTable.keys()).index(n_op)

			


		

			if (opcode == '='):
				dir[int(instruction[3])] = op2
			elif (opcode == '+'):
				dir[int(instruction[3])] = op2 + op1
			elif (opcode == '-'):
				dir[int(instruction[3])] = op2 - op1
			elif (opcode == '*'):
				dir[int(instruction[3])] = op2 * op1
			elif (opcode == '/'):
				dir[int(instruction[3])] = op2 / op1
			elif (opcode == '=='):
				dir[int(instruction[3])] = (op2 == op1)
			elif (opcode == '<='):
				dir[int(instruction[3])] = (op2 <= op1)
			elif (opcode == '>='):
				dir[int(instruction[3])] = (op2 >= op1)
			elif (opcode == '<'):
				dir[int(instruction[3])] = (op2 < op1)
			elif (opcode == '>'):
				dir[int(instruction[3])] = (op2 > op1)
			elif (opcode == '/='):
				dir[int(instruction[3])] = (op2 != op1)
			elif (opcode == 'and'):
				dir[int(instruction[3])] = (op2 and op1)
			elif (opcode == 'or'):
				dir[int(instruction[3])] = (op2 or op1)
			pc += 1
		elif (instruction[0] == 'end'):
			break



# Generate quadruple for arithmetical and boolean expression
def generate_quadruple(operator, operand1, operand2, result):
	if (operand1 in symbolTable):
		operand1 = list(symbolTable.keys()).index(operand1)
	elif ('c' not in str(operand1) and operand1 != ''):
		temporal.append(operand1)

	if (operand2 in symbolTable):
		operand2 = list(symbolTable.keys()).index(operand2)
	elif ('c' not in str(operand2) and operand2 != ''):
		temporal.append(operand2)

	if (result in symbolTable):
		result = list(symbolTable.keys()).index(result)

	quadruple = str(operator) + ' ' + str(operand1) + ' ' + str(operand2) + ' ' + str(result)
	execution.append(quadruple)
	#print(operands)
	#print(quadruple)

# Generate quadruple for gotoes
def generate_quadruple_goto(option, result):
	if (option == 'f'):
		quadruple = 'gotoF' + ' ' + str(result) + ' '
	elif (option == 't'):
		quadruple = 'gotoT' + ' ' + str(result) + ' '
	else:
		quadruple = 'goto' + ' '
	execution.append(quadruple)
	#print(operands)
	#print(quadruple)

def fill_jump(dir, jump_position):
	execution[dir] = execution[dir] + str(jump_position)

def fill_jump_main( jump_position):
	execution[0] = 'goto ' + str(jump_position)

# Get the token map from the lexer
from mathpy_lex import tokens

def p_language(p):
	'language : mathpy'
	pass

def p_mathpy(p):
	'''
	mathpy : PROGRAM ID COLON declarations subroutines blocks END
		   | PROGRAM ID COLON declarations subroutines blocks END PROGRAM
		   | PROGRAM ID COLON declarations subroutines blocks END PROGRAM ID
	'''
	pass

def p_declarations(p):
	'''
	declarations : type COLON COLON variables declarations
				 | empty
	'''
	pass

def p_type(p):
	'''
	type : INTEGER
		 | REAL
	'''
	global var_type
	var_type = p[1:]

def p_variables(p):
	'''
	variables : variables COMMA ID
			  | variables COMMA ID LPAREN INT RPAREN
			  | variables COMMA ID LPAREN INT COMMA INT RPAREN
			  | ID
			  | ID LPAREN INT RPAREN
			  | ID LPAREN INT COMMA INT RPAREN
	'''
	if (len(p) == 2):
		symbolTable.update({p[1]: var_type[0]})
	elif (len(p) == 4):
		symbolTable.update({p[3]: var_type[0]})
	elif (len(p) == 5):
		for x in range (0, p[3]):
			symbolTable.update({str(p[1])+p[2]+str(x)+p[4]: var_type[0]})
	elif (len(p) == 7 and p[2] == ','):
		for x in range (0, p[5]):
			symbolTable.update({str(p[3])+p[4]+str(x)+p[6]: var_type[0]})
	elif (len(p) == 7):
		for x in range (0, p[3]):
			for y in range (0, p[5]):
				symbolTable.update({str(p[1])+p[2]+str(x)+p[4]+str(y)+p[6]: var_type[0]})
	elif (len(p) == 9):
		for x in range (0, p[5]):
			for y in range (0, p[7]):
				symbolTable.update({str(p[3])+p[4]+str(x)+p[6]+str(y)+p[8]: var_type[0]})

def p_matrix(p):
	'''
	matrix : ID
		   | ID LPAREN INT RPAREN
		   | ID LPAREN INT COMMA INT RPAREN
		   | ID LPAREN ID RPAREN
		   | ID LPAREN ID COMMA ID RPAREN
	'''
	if (len(p) == 2):
		p[0] = ''.join(p[1])
	elif (len(p) == 5):
		p[3] = str(p[3])
		p[0] = ''.join(p[1:5])
	elif (len(p) == 7):
		p[3] = str(p[3])
		p[5] = str(p[5])
		p[0] = ''.join(p[1:7])

def p_index(p):
	'''
	index : arithmetic COMMA arithmetic
		  | arithmetic
	'''
	pass

def p_subroutines(p):
	'''
	subroutines : subroutines SUBROUTINE id_subroutine LPAREN RPAREN blocks END
				| subroutines SUBROUTINE id_subroutine LPAREN RPAREN blocks END SUBROUTINE
				| subroutines SUBROUTINE id_subroutine LPAREN RPAREN blocks END SUBROUTINE ID
				| empty
	'''
	if(len(p) > 2):
		execution.append('return')
	
	fill_jump_main(len(execution))

def p_id_subroutine(p):
	'''
	id_subroutine : ID
	'''
	procedureTable.update({p[1]: len(execution)})


def p_blocks(p):
	'''
	blocks : blocks assignment
		   | blocks if comparison then_if blocks conditionals END IF
		   | blocks do blocks IF comparison then_if blocks exit END IF blocks END DO
		   | blocks do assignment_do COMMA arithmetic colon blocks END DO
		   | blocks do assignment_do COMMA arithmetic colon IF comparison then_if blocks exit END IF blocks END DO
		   | blocks ID LPAREN RPAREN
		   | blocks READ TIMES COMMA matrix
		   | blocks PRINT TIMES COMMA matrix
		   | blocks PRINT TIMES COMMA STRING
		   | empty
	'''
	if(len(p) > 12):
		if(p[13] == 'do'):
			generate_quadruple_goto('','')
			dir = jump_list.pop()
			fill_jump(dir, len(execution))
			dir = jump_list.pop()
			fill_jump(len(execution)-1, dir)
		elif(p[16] == 'do'):
			op = operands.pop()
			generate_quadruple('+', op, '1c', op)
			generate_quadruple_goto('','')
			dir = jump_list.pop()
			fill_jump(dir, len(execution))
			dir = jump_list.pop()
			fill_jump(len(execution)-1, dir-1)
			fill_jump(dir, len(execution))
			jump_list.pop()
	elif(len(p) > 7):
		if(p[8] == 'if'):
			while (jump_list[len(jump_list)-1] != 'm'):
 				dir = jump_list.pop()
 				fill_jump(dir, len(execution))
			jump_list.pop()
		elif(p[9] == 'do'):
			op = operands.pop()
			generate_quadruple('+', op, '1c', op)
			generate_quadruple_goto('','')
			dir = jump_list.pop()
			fill_jump(dir, len(execution))
			dir = jump_list.pop()
			fill_jump(len(execution)-1, dir+1)
	elif(len(p) > 3):
		if(p[2] == 'read'):
			if (p[5] in symbolTable):
				dir = list(symbolTable.keys()).index(p[5])
				execution.append('read ' + str(dir))
		elif(p[2] == 'print'):
			if (p[5] in symbolTable):
				dir = list(symbolTable.keys()).index(p[5])
				execution.append('print ' + str(dir))
			elif("\"" in p[5]):
				execution.append('print ' + ''.join(p[5:]))
			elif(str(p[5]).endswith(')')):
				execution.append('print ' + ''.join(p[5:]))
			else:
				print('The variable' , p[5], 'was not declared')
		elif(p[4] == ')'):
			if (p[2] in procedureTable):
				dir = procedureTable[p[2]]
				execution.append('gotoP ' + str(dir))
	else:
		pass

def p_do(p):
	'''
	do : DO
	'''
	jump_list.append(len(execution))

def p_colon(p):
	'''
	colon : COLON
	'''
	op2 = operands.pop()
	op1 = operands.pop()
	r = temporal.pop()
	generate_quadruple('<=', op1, op2, r)
	operands.append(op1)
	operands.append(r)
	expression = operands.pop()
	generate_quadruple_goto('f', expression)
	jump_list.append(len(execution)-1)

def p_assignment_do(p):
	'''
	assignment_do : ID ASSIGN arithmetic
	'''
	operands.append(p[1])
	op1 = operands.pop()
	op2 = operands.pop()
	generate_quadruple('=', op2, '', op1)
	operands.append(op1)


def p_exit(p):
	'''
	exit : EXIT
	'''
	dir = jump_list.pop()
	generate_quadruple_goto('','')
	fill_jump(dir, len(execution))
	jump_list.append(len(execution)-1)


def p_if(p):
	'''
	if : IF
	'''
	jump_list.append('m')
			
def p_then_if(p):
	'''
	then_if : THEN
	'''
	expression = operands.pop()
	generate_quadruple_goto('f', expression)
	jump_list.append(len(execution)-1)

def p_conditionals(p):
	'''
	conditionals : else blocks
				 | else IF comparison then_if blocks conditionals
				 | else
	'''

def p_else(p):
	'''
	else : ELSE
		 | empty
	'''
	generate_quadruple_goto('', '')
	dir = jump_list.pop()
	fill_jump(dir, len(execution))
	jump_list.append(len(execution)-1)	

def p_assignment(p):
	'''
	assignment : matrix ASSIGN arithmetic
	'''
	operands.append(p[1])
	op1 = operands.pop()
	op2 = operands.pop()
	generate_quadruple('=', op2, '', op1)

def p_arithmetic(p):
	'''
	arithmetic : arithmetic PLUS term
			   | arithmetic MINUS term
			   | term
	'''
	if (len(p) == 4):
		op2 = operands.pop()
		op1 = operands.pop()
		r = temporal.pop()
		generate_quadruple(p[2], op1, op2, r)
		operands.append(r)
		p[0] = p[3]
	else:
		p[0] = p[1]

def p_term(p):
	'''
	term : term TIMES factor
		 | term DIVIDE factor
		 | factor
	'''
	if (len(p) == 4):
		op2 = operands.pop()
		op1 = operands.pop()
		r = temporal.pop()
		generate_quadruple(p[2], op1, op2, r)
		operands.append(r)
		p[0] = p[3]
	else:
		p[0] = p[1]

def p_factor(p):
	'''
	factor : INT
		   | FLOAT
		   | matrix
		   | LPAREN arithmetic RPAREN
	'''
	p[0] = p[1:]
	if (len(p) == 2):
		if(p[1] in symbolTable.keys()):
			operands.append(p[1])
		else:
			operands.append(str(p[1]) + 'c')

def p_comparison(p):
	'''
	comparison : comparison OR comparisontwo
			   | comparisontwo
	'''
	if (len(p) == 4):
		op2 = operands.pop()
		op1 = operands.pop()
		r = temporal.pop()
		generate_quadruple(p[2], op1, op2, r)
		operands.append(r)

def p_comparisontwo(p):
	'''
	comparisontwo : comparisontwo AND comparisonthree
				  | comparisonthree
	'''
	if (len(p) == 4):
		op2 = operands.pop()
		op1 = operands.pop()
		r = temporal.pop()
		generate_quadruple(p[2], op1, op2, r)
		operands.append(r)

def p_comparisonthree(p):
	'''
	comparisonthree : comparisonthree EQ comparisonfour
					| comparisonthree NEQ comparisonfour
					| comparisonthree LT comparisonfour
					| comparisonthree GT comparisonfour
					| comparisonthree LTE comparisonfour
			   		| comparisonthree GTE comparisonfour
			   		| comparisonfour
	'''
	if (len(p) == 4):
		op2 = operands.pop()
		op1 = operands.pop()
		r = temporal.pop()
		generate_quadruple(p[2], op1, op2, r)
		operands.append(r)

def p_comparisonfour(p):
	'''
	comparisonfour : INT
		   | FLOAT
		   | matrix
		   | LPAREN arithmetic RPAREN
		   | LPAREN comparison RPAREN
	'''
	if (len(p) == 2):
		if(p[1] in symbolTable.keys()):
			operands.append(p[1])
		else:
			operands.append(str(p[1]) + 'c')

# Define empty production
def p_empty(p):
	'empty :'
	pass

# Error rule for syntax erros
#def p_error(p):
#	print("Syntax error!")

# Build the parser
parser = yacc.yacc()

# Test the parser
from sys import *

data = open(argv[1], "r").read()
#data = open("test.mathpy", "r").read()

generate_quadruple_goto('', '')
parser.parse(data)
execution.append('end of program')
#fill_jump(0, jump_list.pop())

count = 0
print("\nSYMBOL TABLE")
for key, value in symbolTable.items():
	print(count, key, value)
	count = count + 1

print("\nPROCEDURE TABLE")
for key, value in procedureTable.items():
	print(key, value)
print('\n','Operands')
print(operands)
print('\n','Jumps')
print(jump_list, '\n')

count = 0
new_execution = []
for data in execution:
	data = data.split(' ')
	new_execution.append(data)
	print(count, '\t', data, '\n')
	count = count + 1

execution = new_execution

executer(execution)