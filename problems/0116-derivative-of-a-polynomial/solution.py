import numpy as np
def poly_term_derivative(c: float, x: float, n: float) -> float:
    return (c * n)*np.power(x,n-1) 