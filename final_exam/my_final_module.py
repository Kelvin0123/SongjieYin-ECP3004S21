# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Songjie Yin
#
# Date: 5/3/2021
# 
##################################################
#
# Sample Script for Final Exam: 
# Module with Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for a script that you might call
# my_midterm_tests.py (but is not graded).
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module
import math
import numpy as np
from scipy.optimize import minimize

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def ln_check(x: float, a: float) -> float:
    """
    
    Calculates calculates the difference between math.log(x) 
	and some candidate value a, which is a guess of the value of math.log(x).
    
    >>> ln_check(math.exp(7), 3)
    4.0
    >>> ln_check(math.exp(9), 4.5)
    4.5
    >>> ln_check(math.exp(10), 10)
    0.0
    
    """
    ln = math.log(x)
    
    check = ln - a
    
    return check

# Exercise 2

def calc_e(x_0: float, max_iter: int, tol: float) -> float:
    """
    Preconditions: x_0, iter, tol > 0
    
    Calculates the base of the natural logarithm.
    
    >>> calc_e(2, 10, 0.001)
    2.718281064358138
    >>> calc_e(5,20, 0.001)
    2.718281828458728
    >>> calc_e(1, 10, 0.1)
    2.718281064358138
    
    """
    x = x_0
    for i in range(max_iter):
        x_next = x-x*ln_check(x, 1)
        if abs(x_next-x)<tol:
            return x_next
        x = x_next
        
    return x_next

# Exercise 3

def SSR_conc(beta_1: float, y: np.ndarray, x: np.ndarray) -> float:
    """
    Calculates the sum of squared residuals 
    for the linear regression model,
    as a function of the slope coefficient only, 
    concentrating out the intercept.
    
    
    >>> SSR_conc(1.0, [3, -3, 3], [1, 1, 1])
    24.0
    >>> SSR_conc(1.0, [3, 0, 3], [0, 2, 2])
    12.666666666666666
    >>> SSR_conc(0.5, [2, 3, 4], [1, 2, 3])
    0.5
    
    """
    
    y_bar = sum(y)/len(y)
    x_bar = sum(x)/len(x)
    
    beta_0 = y_bar - (x_bar * beta_1)
    
    ssr = sum((np.array(y) - beta_0 - beta_1*np.array(x))**2)
            
    return ssr

# Exercise 4

def ols_slope_conc(y: np.ndarray, x: np.ndarray) -> float:
    """
    Calculates the estimated slope coefficient 
    for the linear regression model,
    by minimizing the concentrated sum of squared resduals, 
    which concentrates out the intercept.
    
    >>> ols_slope_conc([2, 1, 2], [1, 0, 1])
    1.0
    >>> ols_slope_conc([3, 4, 5], [5, 4, 3])
    -1.00000001888464
    >>> ols_slope_conc([2, 1, 0], [1, 1, 0])
    1.500000003725291
    
    """
    
    initial_beta_1 = 1.0
    return minimize(SSR_conc, initial_beta_1, args=(y, x)).x[0]

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 
# One example is already provided. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# Add code so that the tests are implemented below 
# -- but only when the script is run,
# not when it is imported. 

import doctest

if __name__ == "__main__":

    doctest.testmod()



##################################################
# End
##################################################

