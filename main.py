from Dynamics import longitudinalAircraft as ode
import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from scipy.optimize import minimize

dt = 0.1
tf = 8
tmr = np.arange(0.0, tf, dt)

runMinimization = True

###########################################################################################
			#SETUP EQUATIONS OF MOTION AND SOLVE 
###########################################################################################
# states = u, w, x, z, q, theta
number_of_states = 6
x_sim0 = np.zeros((1,number_of_states))
x_sim0 = x_sim0[0]

# starting axial velocity
x_sim0[0] = 25
# starting altitude
x_sim0[3] = -100
print('---------------Initial Condtions are:', x_sim0, '--------------------')

dtDiscrete = 0.5
ode.discreteTime = np.arange(0.0, tf, dtDiscrete)
input_Sim = np.zeros((1,np.size(ode.discreteTime)))
input_Sim = input_Sim[0,:]

print('--------------- Discrete Time Points:', ode.discreteTime, '--------------------')

###########################################################################################
			# PLOTTER
###########################################################################################

def generate_plots(t, x_sim_out):
    # # Plot State Transition solution
    # fig = plt.figure(figsize=(16, 9), dpi=1920/16)
    # plt.rcParams["font.weight"] = "bold"
    # plt.rcParams["axes.labelweight"] = "bold"
    # ax = fig.add_subplot(111)
    # ax.grid('on')
    # plt.xlabel('Time (s)')
    # plt.ylabel('Altitude (meters)')
    # ax.plot(np.transpose(t),x_sim_out[:,0])

    # Plot Alt and Range
    fig = plt.figure(figsize=(16, 9), dpi=1920/16)
    plt.rcParams["font.weight"] = "bold"
    plt.rcParams["axes.labelweight"] = "bold"
    ax = fig.add_subplot(111)
    ax.grid('on')
    plt.xlabel('Range (meters)')
    plt.ylabel('Alt (meters)')
    ax.plot(x_sim_out[:,2],-x_sim_out[:,3])

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

# Minimize the objective function
if runMinimization == True : 
    result = minimize(maxRange, input_Sim)

    # Print the optimized parameters
    print(result.x)
    # print(x_sim)
    fig = generate_plots(tmr, x_sim)
    plt.show()
else: 
    x_sim = integrate.odeint(ode.solveSys, x_sim0, tmr, args=(input_Sim,))
    print(x_sim)
    fig = generate_plots(tmr, x_sim)
    plt.show()


