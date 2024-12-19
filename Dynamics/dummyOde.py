def solveSys(y, t, params):
    k1, k2 = params
    dydt = [-k1 * y[0] + k2 * y[1], k1 * y[0] - k2 * y[1]]
    return dydt
