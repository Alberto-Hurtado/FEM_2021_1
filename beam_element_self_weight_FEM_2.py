from numpy import array, arctan2, zeros, ix_
from scipy.linalg import norm

def beam_element(xy,properties,percent):

	E = properties['E']
	I = properties['I']
	A = properties['A']
	ρ = properties['ρ']


	xi = xy[0,:]
	xj = xy[1,:]

	L = norm(xi - xj)
	#Θ = arctan2( xj[1] - xi[1], xj[0] - xi[0])
	cosΘ = ( xj[0] - xi[0])/L
	sinΘ = ( xj[1] - xi[1])/L


	ke = zeros((6,6))
	ke_tilde = zeros((6,6))

	fe = zeros((6,1))


	l = L

	n0 = percent -.1
	n1 = percent


	ke_tilde[0,0] =  (-n0 + n1)*A*E / l
	ke_tilde[3,3] =  (-n0 + n1)*A*E / l
	ke_tilde[0,3] = -(-n0 + n1)*A*E / l
	ke_tilde[3,0] = -(-n0 + n1)*A*E / l

	#bending_dofs = ix_([6*n+1,6*n+2,6*n+4,6*n+5],[6*n+1,6*n+2,6*n+4,6*n+5])
	bending_dofs = ix_([2,3,4,5],[2,3,4,5])
	

	Δ = 2

	n = percent*10
	e0=-1+Δ*n
	e1=-1+Δ*(n+1)
	
	T = zeros((6,6))
	T[0:2,0:2] = array([[cosΘ, -sinΘ],[sinΘ,cosΘ]])
	T[3:5,3:5] = array([[cosΘ, -sinΘ],[sinΘ,cosΘ]])
	T[2,2]= 1.
	T[5,5]= 1.

	ke_tilde[bending_dofs]=(E*I/(2* l**3))*array([
		[-12*e0**3 + 12*e1**3,-6*l*e0**3 + 3*l*e0**2 + 6*l*e1**3 - 3*l*e1**2,12*e0**3 - 12*e1**3,-6*l*e0**3 - 3*l*e0**2 + 6*l*e1**3 + 3*l*e1**2],
		[-6*l*e0**3 + 3*l*e0**2 + 6*l*e1**3 - 3*l*e1**2,-3*l**2*e0**3 + 3*l**2*e0**2 - l**2*e0 + 3*l**2*e1**3 - 3*l**2*e1**2 + l**2*e1,6*l*e0**3 - 3*l*e0**2 - 6*l*e1**3 + 3*l*e1**2,-3*l**2*e0**3 + l**2*e0 + 3*l**2*e1**3 - l**2*e1],
		[12*e0**3 - 12*e1**3,6*l*e0**3 - 3*l*e0**2 - 6*l*e1**3 + 3*l*e1**2,-12*e0**3 + 12*e1**3,6*l*e0**3 + 3*l*e0**2 - 6*l*e1**3 - 3*l*e1**2],
		[-6*l*e0**3 - 3*l*e0**2 + 6*l*e1**3 + 3*l*e1**2,-3*l**2*e0**3 + l**2*e0 + 3*l**2*e1**3 - l**2*e1,6*l*e0**3 + 3*l*e0**2 - 6*l*e1**3 - 3*l*e1**2,-3*l**2*e0**3 - 3*l**2*e0**2 - l**2*e0 + 3*l**2*e1**3 + 3*l**2*e1**2 + l**2*e1],
	])

	element_dofs = ix_([0,1,2,3,4,5],[0,1,2,3,4,5])
	ke[element_dofs] = T@ke_tilde[element_dofs]@T.T


	#ke=T@ke_tilde@T.T

	q = ρ*A
	fe[0]-= sinΘ*q *         (n0**2*l/2 - n0*l - n1**2*l/2 + n1*l)
	fe[1]-= cosΘ*q *l * .5 * (-0.0625*e0**4 + 0.375*e0**2 - 0.5*e0 + 0.0625*e1**4 - 0.375*e1**2 + 0.5*e1)
	fe[2]+= cosΘ*q *l * .5 * (-0.03125*e0**4*l + 0.0416666666666667*e0**3*l + 0.0625*e0**2*l - 0.125*e0*l + 0.03125*e1**4*l - 0.0416666666666667*e1**3*l - 0.0625*e1**2*l + 0.125*e1*l)
	fe[3]-= sinΘ*q *         (-l*n0**2/2 + l*n1**2/2)
	fe[4]-= cosΘ*q *l * .5 * (-0.0625*e0**4 + 0.375*e0**2 - 0.5*e0 + 0.0625*e1**4 - 0.375*e1**2 + 0.5*e1)
	fe[5]+= cosΘ*q *l * .5 *-(-0.03125*e0**4*l + 0.0416666666666667*e0**3*l + 0.0625*e0**2*l - 0.125*e0*l + 0.03125*e1**4*l - 0.0416666666666667*e1**3*l - 0.0625*e1**2*l + 0.125*e1*l)


	#print(ke)

	return ke , fe

'''
xy = array([[0,0],
			[10,0]])

properties={}
properties['E']=100
properties['A']=1
properties['I']=1
properties['ρ']=1


ke,fe = beam_element(xy,properties,1)

print(ke)
print(fe)
'''


