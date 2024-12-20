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

#states: [x, y, z, p0, p1, p2, p3]

# x0 = np.concatenate((np.transpose(ode.bodies[1].xyz_global_center), np.transpose(ode.bodies[1].p)), axis = 1)

# #concatenate [x, y, z, p0, p1, p2, p3] with [xd, yd ,zd, w1, w2, w3]
# x_sim0 = np.concatenate((x0,vel0), axis = 1)
# #x0 = np.concatenate((x0,np.zeros([1,3])), axis = 1)
# x_sim0 = np.concatenate((x0,w0), axis = 1)
# #add subystems initial conditions: 
# x_sim0 = np.concatenate((x0,np.zeros([1,7])), axis = 1)
# #x0 = np.concatenate((x0,[[0.0]]), axis = 1)

x_sim0 = [1, 0]
input_Sim = [[0, 1], [0, 0.5]]; # After 1 second step command to 0.5 
# x = integrate.solve_ivp(ode.solveSys, tspan, x0[0], method='RK45',t_eval = tmr)
# x_sim = integrate.odeint(ode.solvSys, y0, t, args=(input_Sim,))
# x_sim = integrate.odeint(ode.solvSys, x_sim0, tmr, args=(controlVariable = input_Sim,))

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
def objective(params):
    x0 = x_sim0
    tmr_ = tmr
    global x_sim 
    x_sim = integrate.odeint(ode.solveSys, x0, tmr_, args=(params,))
    y_exp = [np.exp(-tmr_), 1 - np.exp(-tmr_)]  # Simulated experimental data
    return np.sum((x_sim - np.transpose(y_exp))**2)

# Initial guess for parameters
params0 = [0.5, 0.5]

# Minimize the objective function
if runMinimization == True : 
    result = minimize(objective, params0)

    # Print the optimized parameters
    print(result.x)
    print(x_sim)
else: 
    x_sim = integrate.odeint(ode.solveSys, x_sim0, tmr, args=(params0,))
    print(x_sim)
    fig = generate_plots(tmr, x_sim)

    plt.show()


