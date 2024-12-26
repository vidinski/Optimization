import numpy as np

global discreteTime

def solveSys(y, t, controlVar):
    #print(controlVarArray)
    controlVarArray = np.asarray(controlVar)
    # M = np.interp(t, controlVarArray[0,:], controlVarArray[1,:])
    M = np.interp(t, discreteTime, controlVarArray)
    
    # lift = 75.0 
    # drag = -100.0
    # mass = 10.0
    # g = 9.81
    # inertiayy = 10.0

    mass = 1500.0
    g = 9.81
    inertiayy = 2.0*mass/2.0*100.0
    airdensity = 1.23
    PI = np.pi; 
    S = 50; 
    alphaBreakPoints = [-PI/2.0, -PI/4.0, 0.0,  PI/4.0, PI/2.0]; 
    Cl = [ 0.025, 0.05, -0.01, -0.05, -0.025 ]
    Cd = [ -0.005,  -0.0025, -0.001, -0.0025,  -0.005 ]

    # states = u, w, x, z, q, theta
    u =     y[0]
    w =     y[1]
    x =     y[2]
    z =     y[3]
    q =     y[4]
    theta = y[5]

    # Angle of attack
    alpha = np.arctan2(w,u)

    #airspeed: 
    airspeed = np.sqrt(u**2+w**2)

    # Dynamic Pressure
    DynPres = 0.5*airdensity*airspeed**2

    # Look up CD and CL 
    lookedUpCl = np.interp(alpha, alphaBreakPoints, Cl)
    lookedUpCd = np.interp(alpha, alphaBreakPoints, Cd)
    drag = lookedUpCd*S*DynPres
    lift = lookedUpCl*S*DynPres

    # axial velocity
    ud = drag/mass - g*np.sin(theta) - q*w
    # vertical velocity
    wd = lift/mass - g*np.cos(theta) +  q*u

    # Range 
    rd = u*np.cos(theta) + w*np.sin(theta)

    # Altitude
    zd = -(-u*np.sin(theta) + w*np.cos(theta))

    # pitch rate
    qd = M/inertiayy

    #dydt = [-k1 * y[0] + k2 * y[1], k1 * y[0] - k2 * y[1]]
    
    dydt =  [ ud, wd, rd, zd, qd, q]

    return dydt
