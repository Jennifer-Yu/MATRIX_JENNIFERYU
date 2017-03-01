from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()


print("TESTING PRINT MATRIX...")
print_matrix(matrix)

print("TESTING IDENTITY MATRIX...")
ident(matrix)
print_matrix(matrix)

print("TESTING SCALAR MULTIPLICATION...")
scalar_mult(matrix, 3)
print_matrix(matrix)

print("TESTING MATRIX MULTIPLICATION...")
print("m1...")
scalar_mult(matrix, 3)
print_matrix(matrix)
print("m2...")
matrix2 = new_matrix2()
scalar_mult(matrix2, 2)
print_matrix(matrix2)
print("THE NEW AND IMPROVED M2!")
matrix_mult(matrix, matrix2)
print_matrix(matrix2)

print("TESTING ADD EDGE...")
add_edge(matrix, 0, 0, 0, 255, 255, 0)
print_matrix(matrix)

draw_lines( matrix, screen, color )
display(screen)

bubble = new_matrix()
tea = new_matrix()
yum = new_matrix()
yas = new_matrix()

ctr = 500

while ctr > 0:
    temp1 = random.randint(100,500)
    temp2 = random.randint(100,500)
    temp3 = random.randint(70,500)
    temp4 = random.randint(70,500)
    add_edge(bubble, 0, 0, 0, temp1, temp2, 0)
    add_edge(tea, temp1, temp2, 0, temp3, temp4, 0)
    ctr = ctr - 1

add_edge(yum, 0, 0, 0, 255, 255, 0)

while ctr < 150:
    temp5 = random.randint(50,400)
    temp6 = random.randint(50,400)
    temp7 = random.randint(0,450)
    temp8 = random.randint(0,450)
    add_edge(yum, 0, 0, 0, temp5, temp6, 0)
    add_edge(yas, temp5, temp6, 0, temp7, temp8, 0)
    ctr = ctr + 1

'''
	(138,43,226) blue violet
	(72,61,139) dark slate blue
'''
color = [ 138, 43, 226 ]
draw_lines( bubble, screen, color )
color = [ 72, 61, 139 ]
draw_lines( tea, screen, color )
color = [ 0, 255, 0 ]
draw_lines( yum, screen, color )
color = [ 0, 100, 0 ]
draw_lines( yas, screen, color )

display(screen)
