from gaussy import *


def Solve( ext_steel , ext_autos):
	return GaussSolve([ [5395.0/25448.0 - 1.0, 2664.0/30346.0, -1.0 * ext_steel], [ 48.0/25448.0, 9030.0/30346.0 - 1.0, -1.0 * ext_autos ] ])


def Solve2( ext_steel , ext_autos):
	return GaussSolve([ [5395.0/25448.0 - 1.0, 0.05, -1.0 * ext_steel], [ 48.0/25448.0, 9030.0/30346.0 - 1.0, -1.0 * ext_autos ] ])


def Solve3( ext_steel , ext_autos):
	return GaussSolve([ [6.90/18.69 - 1.0, 1.28/14.27, -1.0 * ext_steel], [ 0.0/18.69, 4.40/14.27 - 1.0, -1.0 * ext_autos ] ])


# The book seems to use 17389+200+200, is that a mistake?
print '\n>>> sanity)'
PrintV(Solve(17389+200, 21268-25))

print '\n>>> 1.a)'
PrintV(Solve(17389+200, 21268))
PrintV(Solve(17389+400, 21243))

print '\n>>> 1.b)'
PrintV(Solve(17389+100, 21268+200))

print '\n>>> 1.c)'
PrintV(Solve(17389+200, 21268+200))


print '\n>>> 2.a)'
PrintV(Solve2(17389+200, 21268-25))


print '\n>>> 2.b)'
PrintV(Solve2(17389+200, 21500))

print '\n>>> 3.a)'
PrintV(Solve3(18.69*1.1, 14.27*1.15))

print '\n>>> 3.b)'
pred_3b = v2_muls( Solve3(17389.0 / (1000.0 * 1.3), 21268.0 / (1000.0 * 1.3)), 1000.0*1.3) 
PrintV( pred_3b )
print 'off by'
PrintV( v2_sub(pred_3b, [25448, 30346]) )

print '\nSkipped 4. and 5. (more of the same, but read the questions)'
