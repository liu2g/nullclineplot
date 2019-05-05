# By Zuguang Liu 4/27/2019
# Plot aged-based predation model
# Diff eq used in this model:
# dv/dt=Bu-v-Dv(u+v)-Pv, du/dt=v-u(u+v)-Qu


# Import the required modules
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# External parameters
B=1
D=1
P=2
Q=0
# display window of x and y axes
limlst=[0,1]

# u-nullcline function
def unulc(v):
	return (D*v+P+1)*v/(B-D*v)

# v-nullcline function
def vnulc(u):
	return (u+Q)*u/(1-u)

# Function that makes sure the graph knows where the asymptote is 
def getasymp(numl):
	new_numl=[]
	utol = 50
	ltol = -50
	# for i in numl:
	# 	new_numl.append(i)
	for i in numl:
		if i<ltol:
			new_numl.append(-np.inf)
		elif i>utol:
			new_numl.append(np.inf)
		else:
			new_numl.append(i)
	return new_numl

# Generate u-nullcline
v = np.linspace(limlst[0], limlst[1], 1000)
un= getasymp([unulc(i) for i in v])

# Generate v-nullcline
u = np.linspace(limlst[0], limlst[1], 1000)
vn= getasymp([vnulc(i) for i in u])

# Generate determinant contour map
det_v = np.linspace(limlst[0], limlst[1], 1000)
det_u = np.linspace(limlst[0], limlst[1], 1000)
V, U = np.meshgrid(det_v, det_u)
Z = (-1-D*U-2*D*V-P)*(-2*U-V-Q)-(1-U)*(B-D*V)

# Plot the contour map
plt.contourf(V, U, Z, 0,cmap=cm.gray)

# Insert color bar, note stable/unstable conditions
clb=plt.colorbar()
clb.ax.set_title('D=')
plt.text(limlst[1], 0, '*SS is stable if D>0\nunstable if D<0', fontsize=10, ha='right',va='bottom')

# Plot the u-nullcline, v-nullcline
plt.plot(v,un, vn, u)
plt.legend(['u-nullcline','v-nullcline'])

# Configure the plot
plt.xlim(limlst)
plt.ylim(limlst)
plt.xlabel("Immature (v)") 
plt.ylabel("Mature (u)")
plt.title("B="+str(B)+", D="+str(D)+", P="+str(P)+", Q="+str(Q))
plt.grid()
plt.show()