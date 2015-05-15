import numpy as np
from IPython.html.widgets import interact

def numericalStep(xi, vi, deltaT):
    #Compute acceleration:
    ai = -1*xi
    
    #Compute velocity half way through the interval:
    v = vi + deltaT*ai
    
    #Compute final position:
    x = xi + deltaT*v
    
    return x, v

numSteps = 63
deltaT = 0.1

#Initialize Vectors:
xVec = np.zeros(numSteps)
aVec = np.zeros(numSteps)
tVec = np.zeros(numSteps)
#Velocity at mid intervals:
vVec = np.zeros(numSteps)

#Velocity at intervals:
vIVec = np.zeros(numSteps)

#Initial Conditions:
xi = 1
v0 = 0
ai = -1*xi
#Go "back in time" by delta t/2 to compture velocity at time -delta t/2. 
vi = v0 - ai*deltaT/2

xVec[0] = xi
vVec[0] = vi
aVec[0] = ai
tVec[0] = 0

for i in range(1, numSteps):
    x, v = numericalStep(xi, vi, deltaT)
    #Compute velocity at interval marks:
    vIVec[i-1] = (v+vi)/2
    xi = x
    vi = v

    xVec[i] = x
    vVec[i] = v
    aVec[i] = -1*x
    tVec[i] = tVec[i-1]+deltaT
    
#Compute last element of vIVec, so lenghts match:
x, v = numericalStep(xi, vi, deltaT)
vIVec[i] = (v+vi)/2




