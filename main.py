# from Dynamics import longitudinalAircraft as ode
import numpy as np
import scipy.integrate as integrate

from scipy.optimize import minimize

dt = 0.1
tf = 0.75
tspan = [0., tf]
tmr = np.arange(0.0, tspan[1], dt)

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

# x_sim0 = np.array(x0[0]) 
input_Sim = [[0, 1], [0, 0.5]]; # After 1 second step command to 0.5 
# x = integrate.solve_ivp(ode.solveSys, tspan, x0[0], method='RK45',t_eval = tmr)
# x_sim = integrate.odeint(ode.solvSys, y0, t, args=(input_Sim,))
# x_sim = integrate.odeint(ode.solvSys, x_sim0, tmr, args=(controlVariable = input_Sim,))

###########################################################################################
			# HOW TO SOLVE PROBLEM WITH NUMPY MINIMIZE
###########################################################################################

#from scipy.integrate import odeint
from scipy.optimize import minimize

# Define the ODE model
def model(y, t, params):
    k1, k2 = params
    dydt = [-k1 * y[0] + k2 * y[1], k1 * y[0] - k2 * y[1]]
    return dydt

# Define the objective function to minimize
def objective(params):
    y0 = [1, 0]  # Initial conditions
    t = np.linspace(0, 10, 100)
    y_sim = integrate.odeint(model, y0, t, args=(params,))
    y_exp = [np.exp(-t), 1 - np.exp(-t)]  # Simulated experimental data
    return np.sum((y_sim - np.transpose(y_exp))**2)

# Initial guess for parameters
params0 = [0.5, 0.5]

# Minimize the objective function
result = minimize(objective, params0)

# Print the optimized parameters
print(result.x)
