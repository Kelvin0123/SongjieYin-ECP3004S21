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

import math

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

def sqrt_z_bisect(z, a_0, b_0, num_iter):
    """ Calculates the square root of z.
    
    >>> sqrt_z_bisect(100, 0, 50, 100)
    10
    >>> sqrt_z_bisect(6.25, 0, 50, 100)
    2.5
    >>> sqrt_z_bisect(25, 0, 50, 100)
    5
    
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

def z_squared_diff_prime(x, z):
    """ Returned the derivative with respect to x.
    
    >>> z_squared_diff_prime()
    >>> z_squared_diff_prime()
    >>> z_squared_diff_prime()
    
    """
    diff_out = 1/x + math.exp(-x)
    return diff_out

help(math.exp)


# Exercise 4


# Exercise 5

def z_squared_mid(x, z):
    """
    >>> z_squared_mid()
    
    >>> z_squared_mid()
    >>> z_squared_mid()
    
    """
    fixed = 0.5*(z/x + x)
    return fixed

# Exercise 6



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
