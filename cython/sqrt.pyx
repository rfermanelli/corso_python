cdef extern from "math.h":
    double sqrt(double x)

def cython_sqrt(double x):
    return sqrt(x)