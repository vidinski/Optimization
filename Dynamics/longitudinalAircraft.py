import numpy as np

def solveSys(y, t, controlVar):
    k1, k2 = controlVar
    M = 0.0; 
    lift = 1.0 
    drag = 2.0
    mass = 10.0
    g = 9.81
    inertiay = 10.0

    # states = u, w, x, z, q, theta
    u = y[0] 
    w = y[1]
    x = 0 #y[2]
    z = 0 #y[3]
    q = 0 #y[4]
    theta = 0  #y[5]

    # axial velocity
    u = lift/mass - g*np.sin(theta) - q*w
    # vertical velocity
    w = drag/mass - g*np.cos(theta) +  q*u

    # Range 
    rd = u*np.cos(theta) + w*np.sin(theta)

    # Altitude
    zd = -u*np.sin(theta) + w*np.cos(theta)

    # pitch rate
    qd = M/inertiay

    dydt = [-k1 * y[0] + k2 * y[1], k1 * y[0] - k2 * y[1]]
    return dydt
