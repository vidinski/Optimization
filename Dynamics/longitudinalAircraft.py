import numpy as np

def solveSys(y, t, controlVar):
    #print(controlVarArray)
    controlVarArray = np.asarray(controlVar)
    M = np.interp(t, controlVarArray[0,:], controlVarArray[1,:])
    lift = -1.0 
    drag = -2.0
    mass = 10.0
    g = 9.81
    inertiayy = 10.0

    # states = u, w, x, z, q, theta
    u =     y[0]
    w =     y[1]
    x =     y[2]
    z =     y[3]
    q =     y[4]
    theta = y[5]

    # axial velocity
    ud = drag/mass - g*np.sin(theta) - q*w
    # vertical velocity
    wd = lift/mass - g*np.cos(theta) +  q*u

    # Range 
    rd = u*np.cos(theta) + w*np.sin(theta)

    # Altitude
    zd = -u*np.sin(theta) + w*np.cos(theta)

    # pitch rate
    qd = M/inertiayy

    #dydt = [-k1 * y[0] + k2 * y[1], k1 * y[0] - k2 * y[1]]
    
    dydt =  [ ud, wd, rd, zd, qd, q]

    return dydt
