!--------------------------------------
! Programming Language: mathpy.py
! Orientation: numerical calculations
! Author: Sharif Nasser Kadamani
! ID: A00820367
! This a test code
!--------------------------------------

! This is a comment
! Below there is an example program written in mathpy
! It is supposed to read dimensions of two matrices y verify if it is possible to sum them up

program exampleMatrix: 
	integer :: a, b, c, d, e(a,b), f(c,d)
	real :: unusedvar ! For illustration

	! Unused subroutines for illustration only
	subroutine abc()
		a + b + c
	end subroutine abc

	subroutine cba()
		c + (b + a)
	end subroutine

	! The real example code starts here
	do
		print *, "Escriba la dimension uno de la matriz uno"
		read *, a
		print *, "Escriba la dimension dos de la matriz uno"
		read *, b
		print *, "Escriba la dimension uno de la matriz dos"
		read *, c
		print *, "Escriba la dimension dos de la matriz dos"
		read *, d

		a = 0
		b = 0
		c = 0
		d = 0
		if (a == c ) then
			if b == d then
				do a = 0, c
					do b = 0, d
						e(a,b) = e(a,b) + f(a,b)
						print *, e(a,b)
					end do
				end do
			end if
			exit
		end if

		if (b == d) then
			if a == c then
				do a = 0, c
					do b = 0, d
						e(a,b) = e(a,b) + f(a,b)
						print *, e(a,b)
					end do
				end do
			end if
		end if		
	end do
end program exampleMatrix


def p_variables(p):
	'''
	variables : variables COMMA ID matrix
			  | ID matrix
	'''
	if (len(p) > 3):
		symbolTable.update({p[3]: var_type[0]})
	else:
		symbolTable.update({p[1]: var_type[0]})

def p_matrix(p):
	'''
	matrix : LPAREN index RPAREN
		   | empty
	'''
	pass

def p_index(p):
	'''
	index : arithmetic COMMA arithmetic
		  | arithmetic
	'''
	pass