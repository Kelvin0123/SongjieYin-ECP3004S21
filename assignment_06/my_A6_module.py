# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Songjie Yin
#
# Date: 3/20/2021
# 
##################################################
#
# Sample Script for Assignment 6: 
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

def z_squared_diff(x: float,z: float)-> float:
    """ Return the value of x**2 - z
    
    >>> z_squared_diff(10,100)
    0
    >>> z_squared_diff(2.5,6.25)
    0.0
    >>> z_squared_diff(5,25)
    0
    """
    diff = x**2-z
    
    return diff

# Exercise 2

def sqrt_z_bisect(z: float,a_0: float,b_0: float,num_iter: int) -> float:
    """ Calculates the square root of z.
    
    >>> sqrt_z_bisect(100, 0.5, 20, 99)
    10.0
    >>> sqrt_z_bisect(6.25, 0.5, 20, 99)
    2.5
    >>> sqrt_z_bisect(25, 0.5, 20, 99)
    5.0
    
    """
    a_i = a_0
    b_i = b_0
    
    for i in range(num_iter):
        m_i = (a_i + b_i) / 2
        if z_squared_diff(m_i, z) < 0:
            a_i = m_i
        elif z_squared_diff(m_i, z) > 0:
            b_i = m_i
        elif z_squared_diff(m_i, z) == 0:
            return m_i
        
    return m_i

# Exercise 3

def z_squared_diff_prime(x: float,z: float) -> float:
    """ Returned the derivative with respect to x.
    
    >>> z_squared_diff_prime(10, 100)
    20
    >>> z_squared_diff_prime(2.5, 6.25)
    5.0
    >>> z_squared_diff_prime(5, 25)
    10
    
    """
    x = 2*x

    return x


# Exercise 4

def sqrt_z_newton(z, x0, tol, num_iter):
    """ Solves for the root of the function f(z)
    using Newton's method.
    
    >>> sqrt_z_newton(100, 0.5, 0.001, 99)
    10.0
    >>> sqrt_z_newton(6.25, 0.5, 0.001, 99)
    2.5
    >>> sqrt_z_newton(2.0, 2.0, 0.0, 4)
    None
    
    """
    x_i = x0
    for i in range(num_iter):
        
        x_i = x_i - z_squared_diff(x_i, z) / z_squared_diff_prime(x_i, z)
        if (abs(z_squared_diff(x_i, z)) < tol ):
            return x_i
        
    print("Exceeded allowed number of iterations")
    return None

# Exercise 5

def z_squared_mid(x, z):
    """ Returns the value f(x) for a given value z.
    
    >>> z_squared_mid(10, 100)
    10.0
    >>> z_squared_mid(2.5, 6.25)
    2.5
    >>> z_squared_mid(5, 25)
    5.0
    """
    fixed = 0.5*(z/x + x)
    
    return fixed

# Exercise 6

def sqrt_z_fixed_pt(z, x0, tol, num_iter):
    """ Solves for the root of the function f(z)
    using the fixed-point method.
    
    >>> sqrt_z_fixed_pt(100, 0.5, 0.001, 99)
    10.0
    >>> sqrt_z_fixed_pt(6.25, 0.5, 0.001, 99)
    2.5
    >>> sqrt_z_fixed_pt(2.0, 2.0, 0.0, 99)
    None
    
    """
    x_i = x0
    for i in range(num_iter):
        
        x_i = z_squared_mid(x_i, z)
        if abs(z_squared_mid(x_i, z)- x_i) < tol:
            return x_i
        
    print("Exceeded allowed number of iterations")
    return None

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
