from numpy import array, ndarray, eye, zeros

A = array([[0,1,0],[0,0,1],[0,0,0]])

def delta(
    A:ndarray,
    x:ndarray = array([0,0,0]).T,
    B:ndarray = array([0,0,1]).T,
    u:ndarray = array([0,0,0]).T
    )->ndarray:
    return A @ x + B @ u

u = [[0,0,9.8]*50]

dt = 0.1