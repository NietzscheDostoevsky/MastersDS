# function to calculate quadratic equations 

import cmath
from typing import Tuple

def quad_solver(a:float = 1.0, b:float=1.0, c:float=1.0) ->  Tuple[complex, complex] :
    """
    Solve a quadratic equation of the form ax^2 + bx + x = 0

    Args:
        a (float) : Coefficient of x^2
        b (float) : Coefficiant of x
        c (float) : constant
    
    Returns:
        Tuple[complex, complex]
    """

    if a == 0:
        return ValueError("Coefficient of x^2 can't be zero for a quadratic equation")
    
    discriminant:float = cmath.sqrt( b**2 - 4 * a * c )
    root1 = ( -b + discriminant) / 2*a
    root2 = (-b - discriminant) / 2*a

    return (root1, root2)


if __name__ == "__main__":
    print(quad_solver(a=10, b=2, c=1))