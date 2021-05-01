# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Songjie Yin
#
# Date:
# 
##################################################
#
# Sample Script for Assignment 7: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for the script my_A6_tests.py.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module



##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def g(x: float) -> float:
    """ Calculates the value of the equation 
    g(x)=(x-2)*x*(x+2)**2.
    
    >>> g(1.0) 
    -9.0
    >>> g(2.0)
    0.0
    >>> g(3.0)
    75.0
    """
    
    return (x-2)*x*(x+2)**2

def g_prime(x: float) -> float:
    """ Calculates the first derivative of the
    equation g(x)=(x-2)*x*(x+2)**2, with respect
    to x.
    
    >>> g_prime(1.0)
    -6.0
    >>> g_prime(2.0)
    32.0
    >>> g_prime(3.0)
    130.0
    """
    
    return 2*(x+2)*(2*x**2-x-2)

def g_2prime(x: float) -> float:
    """ Calculates the second derivative of the 
    equation g(x)=(x-2)*x*(x+2)**2, with respect
    to x.
    
    >>> g_2prime(1.0)
    16.0
    >>> g_2prime(2.0)
    64.0
    >>> g_2prime(3.0)
    136.0
    """
    
    return 12*x**2+12*x-8

# Exercise 2

def newton_g_opt(x_0: float,maxiter: int,tol: float) -> float:
    """ Finds the minimum of g(x) using Newton's
    method.
    
    >>> newton_g_opt(1.0,100,0.0001)
    -9.91441130872133
    >>> newton_g_opt(2.0,100,0.01)
    -9.1875
    >>> newton_g_opt(3.0,100,1)
    1.4749109224775752
    """
    x = x_0
    for i in range(maxiter):
        x_next = x - (g_prime(x)/g_2prime(x))
        # if (x_next - x) < tol:
        if abs(x_next - x) < tol:
            # It is also acceptable to return g(x)
            # return g(x_next)
            # But my examples compare with x.
            return x_next
        x = x_next
    # if i == maxiter - 1 and x_next - x < tol:
    if i == maxiter - 1 and abs(x_next - x) > tol:
        
        # return g(x)
        return x

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# The tests are implemented below -- but only
# when the script is run, not when it is imported. 


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    






##################################################
# End
##################################################
