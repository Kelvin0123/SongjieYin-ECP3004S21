# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: 
#
# Date:
# 
##################################################
#
# Sample Script for Assignment 5: 
# Function Definitions
#
##################################################
"""



"""
##################################################
##################################################
# Note: there should be no printing or calculations
# in this script, aside from function definitions. 
# Save those for the script my_A5_tests.py.
##################################################
##################################################
"""






##################################################
# Import Required Modules
##################################################

# import name_of_module

import numpy as np


##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def variance(x: list) -> float:
    """ Calculates the sample variance of the variable
    in the list x.
    
    >>> variance([1,2,3])
    0.6666666666666666
    >>> variance([-2.3,3,4,5,6,7,8])
    9.949795918367347
    >>> variance([0,0,0,0,0,0,0,0,0])
    0.0
    
    """
    var = 0
    diff = 0
    
    list_avg = sum(x)/len(x)
    
    for i in range(len(x)):
        diff += (x[i] - list_avg)**2
    
    var = 1/len(x) * diff
    
    return var

# Exercise 2
def covariance(y: list,x: list) -> float:
    """ Calculates the sample covariance of the variables
    in the lists y and x.
    
    Lists y and x both must have the same length.
    
    >>> covariance([1,2,3],[4,5,6])
    0.6666666666666666
    >>> covariance([5,12,18,23,45],[2,8,18,20,28])
    116.88
    >>> covariance([0,1,2,3],[4,5])
    None
    """
    diff=0
    
    y_bar = sum(y)/len(y)
    x_bar = sum(x)/len(x)
    
    if len(y)==len(x):
        for i in range(len(y)):
            diff += (y[i] - y_bar)*(x[i] - x_bar)
    else:
        print("Lists y and x both must have the same length.")
        cov = None
    
    cov = 1/len(y) * diff

    return cov

# Exercise 3
def ols_slope(y: list,x: list) -> float:
    """ Calculates the slope coefficients for the linear
    regression model.
    
    >>> ols_slope([1,2,3],[4,5,6])
    1.0
    >>>
    >>>
    
    """
    cov = 0
    var = 0    
    y_bar = sum(y)/len(y)
    x_bar = sum(x)/len(x)
    
    for i in range(len(y)):
        cov += (y[i] - y_bar)*(x[i] - x_bar)
    
    for i in range(len(x)):
        var += (x[i] - x_bar)**2
    
    beta_1_hat = cov/var
    
    return beta_1_hat

# Exercise 4
def ols_intercept(y: list,x: list,beta_1_hat: float) -> float:
    """ Calculates the intercept co-efficient for the linear
    regression model.
    
    >>> ols_intercept([1,2,3],[4,5,6],7)
    -33.0
    >>>
    >>>
    
    """
    y_bar = sum(y)/len(y)
    x_bar = sum(x)/len(x)

    beta_0_hat = y_bar - beta_1_hat*x_bar
    
    return beta_0_hat

# Exercise 5
def ssr(y: list,x: list,beta_0: float,beta_1: float) -> float:
    """Calculates the sum of squared residuals for 
    the bivariate linear regression model.
    y and x are lists of equal length
    and beta_0 and eta_1 are scalar coefficients. 
    
    >>> ssr(y = [2, 2, 2], x = [1, 1, 1], beta_0 = 0.5, beta_1 = 0.5)
    3.0
    >>> ssr(y = [3, 0, 3], x = [0, 2, 2], beta_0 = 1.0, beta_1 = 0.5)
    9.0

    """
    ssr = 0
    for i in range(len(y)):
        ssr_i = (y[i] - beta_0 - beta_1*x[i])**2
        ssr = ssr + ssr_i
        
    return ssr

# Exercise 6
def min_ssr(y, x, beta_0_min, beta_0_max, beta_1_min, beta_1_max) -> float:
    """ Calculates the sum of squared residuals for the linear
    regression model.
    
    min_ssr([1,2,3,4],[4,5,6,50],0.5,100,0.5,6)
    
    """
    beta_0_list = list(np.arange(beta_0_min,beta_0_max,0.5))
    beta_1_list = list(np.arange(beta_0_min,beta_0_max,0.5))

    min_ssr = 999999
    for i in range(len(beta_0_list)):
        for j in range(len(beta_1_list)):
            ssr_i = ssr(y, x, beta_0_list[i], beta_1_list[j])
            if ssr_i < min_ssr:
                min_ssr = ssr_i
                beta = [i,j]
                
    return beta

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
