from numpy import array,zeros, ix_
from beam_element_self_weight_FEM_2 import beam_element


xy = array([
	[ 0.0 , 0.0 ],

	[ 0.0 , 0.3 ],
	[ 0.0 , 0.6 ],
	[ 0.0 , 0.9 ],
	[ 0.0 , 1.2 ],
	[ 0.0 , 1.5 ],
	[ 0.0 , 1.8 ],
	[ 0.0 , 2.1 ],
	[ 0.0 , 2.4 ],
	[ 0.0 , 2.7 ],
	[ 0.0 , 3.0 ],

	[ 0.0 , 3.2 ],
	[ 0.0 , 3.4 ],
	[ 0.0 , 3.6 ],
	[ 0.0 , 3.8 ],
	[ 0.0 , 4.0 ],
	[ 0.0 , 4.2 ],
	[ 0.0 , 4.4 ],
	[ 0.0 , 4.6 ],
	[ 0.0 , 4.8 ],
	[ 0.0 , 5.0 ],

	[ 0.0 , 5.1 ],
	[ 0.0 , 5.2 ],
	[ 0.0 , 5.3 ],
	[ 0.0 , 5.4 ],
	[ 0.0 , 5.5 ],
	[ 0.0 , 5.6 ],
	[ 0.0 , 5.7 ],
	[ 0.0 , 5.8 ],
	[ 0.0 , 5.9 ],
	[ 0.0 , 6.0 ],#Column X=0


	[ 6.0 , 0.0 ],

	[ 6.0 , 0.3 ],
	[ 6.0 , 0.6 ],
	[ 6.0 , 0.9 ],
	[ 6.0 , 1.2 ],
	[ 6.0 , 1.5 ],
	[ 6.0 , 1.8 ],
	[ 6.0 , 2.1 ],
	[ 6.0 , 2.4 ],
	[ 6.0 , 2.7 ],
	[ 6.0 , 3.0 ],

	[ 6.0 , 3.2 ],
	[ 6.0 , 3.4 ],
	[ 6.0 , 3.6 ],
	[ 6.0 , 3.8 ],
	[ 6.0 , 4.0 ],
	[ 6.0 , 4.2 ],
	[ 6.0 , 4.4 ],
	[ 6.0 , 4.6 ],
	[ 6.0 , 4.8 ],
	[ 6.0 , 5.0 ],

	[ 6.0 , 5.15],
	[ 6.0 , 5.3 ],
	[ 6.0 , 5.45],
	[ 6.0 , 5.6 ],
	[ 6.0 , 5.75],
	[ 6.0 , 5.9 ],
	[ 6.0 , 6.05],
	[ 6.0 , 6.2 ],
	[ 6.0 , 6.35],
	[ 6.0 , 6.5 ],#Column X=6

	[ 0.6 , 3.0 ],
	[ 1.2 , 3.0 ],
	[ 1.8 , 3.0 ],
	[ 2.4 , 3.0 ],
	[ 3.0 , 3.0 ],
	[ 3.6 , 3.0 ],
	[ 4.2 , 3.0 ],
	[ 4.8 , 3.0 ],
	[ 5.4 , 3.0 ],# Beam Y=3

	[ 0.6 , 5.0 ],
	[ 1.2 , 5.0 ],
	[ 1.8 , 5.0 ],
	[ 2.4 , 5.0 ],
	[ 3.0 , 5.0 ],
	[ 3.6 , 5.0 ],
	[ 4.2 , 5.0 ],
	[ 4.8 , 5.0 ],
	[ 5.4 , 5.0 ],# Beam Y=5

	[ 0.6 , 6.05],
	[ 1.2 , 6.1 ],
	[ 1.8 , 6.15],
	[ 2.4 , 6.2 ],
	[ 3.0 , 6.25],
	[ 3.6 , 6.3 ],
	[ 4.2 , 6.35],
	[ 4.8 , 6.4 ],
	[ 5.4 , 6.45],# Beam roof
	])


'''
from matplotlib import pylab as plt

for nodo in xy:
	plt.plot(nodo[0],nodo[1],'sr')
'''



conec = array([
	[ 0, 1,.1],
	[ 1, 2,.2],
	[ 2, 3,.3],
	[ 3, 4,.4],
	[ 4, 5,.5],
	[ 5, 6,.6],
	[ 6, 7,.7],
	[ 7, 8,.8],
	[ 8, 9,.9],
	[ 9,10,1.],#0

	[10,11,.1],
	[11,12,.2],
	[12,13,.3],
	[13,14,.4],
	[14,15,.5],
	[15,16,.6],
	[16,17,.7],
	[17,18,.8],
	[18,19,.9],
	[19,20,1.],#1

	[20,21,.1],
	[21,22,.2],
	[22,23,.3],
	[23,24,.4],
	[24,25,.5],
	[25,26,.6],
	[26,27,.7],
	[27,28,.8],
	[28,29,.9],
	[29,30,1.],#2

	[31,32,.1],
	[32,33,.2],
	[33,34,.3],
	[34,35,.4],
	[35,36,.5],
	[36,37,.6],
	[37,38,.7],
	[38,39,.8],
	[39,40,.9],#3
	[40,41,1.],

	[41,42,.1],
	[42,43,.2],
	[43,44,.3],
	[44,45,.4],
	[45,46,.5],
	[46,47,.6],
	[47,48,.7],
	[48,49,.8],
	[49,50,.9],
	[50,51,1.],#4

	[51,52,.1],
	[52,53,.2],
	[53,54,.3],
	[54,55,.4],
	[55,56,.5],
	[56,57,.6],
	[57,58,.7],
	[58,59,.8],
	[59,60,.9],
	[60,61,1.],#5

	[10,62,.1],
	[62,63,.2],
	[63,64,.3],
	[64,65,.4],
	[65,66,.5],
	[66,67,.6],
	[67,68,.7],
	[68,69,.8],
	[69,70,.9],
	[70,41,1.],#6 Beam

	[20,71,.1],
	[71,72,.2],
	[72,73,.3],
	[73,74,.4],
	[74,75,.5],
	[75,76,.6],
	[76,77,.7],
	[77,78,.8],
	[78,79,.9],
	[79,51,1.],#7 Beam

	[30,80,.1],
	[80,81,.2],
	[81,82,.3],
	[82,83,.4],
	[83,84,.5],
	[84,85,.6],
	[85,86,.7],
	[86,87,.8],
	[87,88,.9],
	[88,61,1.],#8 Roof beam
	])

'''
for i,e in enumerate(conec):
	ni = e[0]
	nj = e[1]

	# Initial form in blue
	plt.plot([xy[ni][0],xy[nj][0]],[xy[ni][1],xy[nj][1]],'b')

plt.show()
exit(-1)
'''


properties_column = {}
properties_column['E'] = 250./0.003 #kgf/cm2
properties_column['ρ'] = 2500e-6 #kgf/cm3
properties_column['A'] = 30*30. #cm2
properties_column['I'] = 30 * 30**3 /12. #cm4

properties_beam = {}
properties_beam['E'] = 250./0.003 #kgf/cm2
properties_beam['ρ'] = 2500e-6 #kgf/cm3
properties_beam['A'] = 20*40. #cm2
properties_beam['I'] = 20 * 40**3 /12. #cm4

properties_roof_beam = {}
properties_roof_beam['E'] = 250./0.003 #kgf/cm2
properties_roof_beam['ρ'] = 2500e-6 #kgf/cm3
properties_roof_beam['A'] = 20*20. #cm2
properties_roof_beam['I'] = 20 * 20**3 /12. #cm4

Nnodes = xy.shape[0]
Nelems = conec.shape[0]

NDOFs_per_node=3
NDOFs = NDOFs_per_node*Nnodes

K = zeros((NDOFs,NDOFs))
f = zeros((NDOFs,1))

for e in range(Nelems):
	ni = int(conec[e,0])
	nj = int(conec[e,1])

	xy_e = xy[[ni,nj],:] #Se obtiene una matriz 2 filas con las columnas correspondientes a los nodos ni y nj

	if e in [6,7]:
		ke, fe = beam_element(xy_e,properties_beam,conec[e,2])
	elif e==8:
		ke, fe = beam_element(xy_e,properties_roof_beam,conec[e,2])
	else:
		ke, fe = beam_element(xy_e,properties_column,conec[e,2])


	#Node k---> [3*k,3*k+1,3*k+2]
	d = [3*ni,3*ni+1,3*ni+2,3*nj,3*nj+1,3*nj+2]

	for i in range(2*NDOFs_per_node):
		p = d[i]
		for j in range(2*NDOFs_per_node):
			q = d[j]
			K[p,q] += ke[i,j]
		f[p] += fe[i]

'''
from matplotlib import pylab as plt


plt.matshow(K)
plt.show()
'''



# System partitioning and solution


#print(K.shape)
constrained_DOFs=[0,1,2,31*3,31*3 + 1,31*3 + 2]
free_DOFs = list(range(0,267))
for rest in constrained_DOFs:
	free_DOFs.remove(rest)



Kff = K[ix_(free_DOFs,free_DOFs)]
Kfc = K[ix_(free_DOFs,constrained_DOFs)]
Kcf = K[ix_(constrained_DOFs,free_DOFs)]
Kcc = K[ix_(constrained_DOFs,constrained_DOFs)]

ff = f[free_DOFs]
fc = f[constrained_DOFs]

# Solve
from scipy.linalg import solve

u = zeros((NDOFs,1))


u[free_DOFs] = solve(Kff,ff)


# Get reaction forces
R = Kcf@u[free_DOFs]

#print(u)

from matplotlib import pylab as plt


#print(u)
for i,e in enumerate(conec):
	ni = int(e[0])
	nj = int(e[1])

	# Initial form in blue
	plt.plot([xy[ni][0],xy[nj][0]],[xy[ni][1],xy[nj][1]],'b')

	# Deformated form in green
	augment = 5e2
	plt.plot([xy[ni][0]+u[ni*3]*augment,xy[nj][0]+u[nj*3]*augment],[xy[ni][1]+u[ni*3 +1]*augment,xy[nj][1]+u[nj*3 +1]*augment],'g--')
plt.show()