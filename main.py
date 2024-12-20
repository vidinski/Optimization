from Dynamics import longitudinalAircraft as ode
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from scipy.optimize import minimize

dt = 0.1
tf = 0.75
tspan = [0., tf]
tmr = np.arange(0.0, tspan[1], dt)

runMinimization = False

###########################################################################################
			#SETUP EQUATIONS OF MOTION AND SOLVE 
###########################################################################################
# states = u, w, x, z, q, theta
number_of_states = 6
x_sim0 = np.zeros((1,number_of_states))
x_sim0 = x_sim0[0]
input_Sim = [[0, 1], [0, 0.5]]; # After 1 second step command to 0.5 

###########################################################################################
			# PLOTTER
###########################################################################################

def generate_plots(t, x_sim_out):
    # Plot State Transition solution
    fig = plt.figure(figsize=(16, 9), dpi=1920/16)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    ax = fig.add_subplot(111)
    ax.grid('on')
    plt.xlabel('Time (s)')
    plt.ylabel('Altitude (meters)')
    ax.plot(np.transpose(t),x_sim_out[:,0])

###########################################################################################
			# HOW TO SOLVE PROBLEM WITH NUMPY MINIMIZE
###########################################################################################

# Define the objective function to minimize
def maxRange(params):
    x0 = x_sim0
    tmr_ = tmr
    global x_sim 
    x_sim = integrate.odeint(ode.solveSys, x0, tmr_, args=(params,))
    return -x_sim[2,-1]

# Initial guess for parameters
params0 = [0.5, 0.5]

# Minimize the objective function
if runMinimization == True : 
    result = minimize(maxRange, params0)

    # Print the optimized parameters
    print(result.x)
    print(x_sim)
else: 
    x_sim = integrate.odeint(ode.solveSys, x_sim0, tmr, args=(params0,))
    print(x_sim)
    fig = generate_plots(tmr, x_sim)

    plt.show()


