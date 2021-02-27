# -*- coding: utf-8 -*-
"""
##################################################
#
# ECP 3004: Python for Business Analytics
#
# Name: Songjie Yin
#
# Date: 2/19/2021
# 
##################################################
#
# Sample Script for Assignment 4: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module

import numpy
import math
import doctest

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1
def matrix_multiple(mat_1: numpy.ndarray,mat_2: numpy.ndarray) ->numpy.ndarray:
    """Return the multiple of two matrices. 
    Precondition: the column of mat_1 must equal 
    the row of mat_2. If the precondition is 
    not met,the function will return None and 
    print a warning message.
    
    >>> matrix_multiple(numpy.array([[1.,2.,3.],[4.,5.,6.]]),numpy.array([[10.,11.],[20.,21.],[30.,31.]]))
    array([[140, 146],
           [320, 335]])
    >>> matrix_multiple(numpy.array([[0.,0.],[0.,0.]]),numpy.array([[0.,0.],[0.,0.]]))
    array([[0, 0],
           [0, 0]])
    >>> matrix_multiple(numpy.array([[3.,6.],[4.,7.]]),numpy.array([[1.,2.,3.]]))
    None
    """
    if len(mat_1[0]) != len(mat_2):
        print('Please input the correct matrices so that the column of mat_1 equals the row of mat_2')
    else:   
        result = numpy.array([[0 for x in range(len(mat_1))] for y in range(len(mat_2[0]))])
        for i in range(len(mat_1)):
            for j in range(len(mat_2[0])):
                for k in range(len(mat_2)):
                    result[i][j] += mat_1[i][k] * mat_2[k][j]
        return result
    
# Exercise 2
def ssr_loops(y: list,x: list,beta_0: float,beta_1: float) -> float:
    """ Calculates the value of the sum of squared residuals
        of the regression model.
        Precondition: length of y must equal length of x.
        
    >>> ssr_loops([1,2,3],[4,5,6],7.0,8.0)
    6173.0
    >>> ssr_loops([2.0,0.0,-1.0],[10.0,-5.0,2.0],1.0,2.0)
    478.0
    >>> ssr_loops([2],[3,4],5,6)
    None
    """
    ssr=0   
    if len(x) != len(y):
        return None
    else: 
        for i in range(len(x)):
            ssr += ((y[i]-beta_0-beta_1*x[i])**2)
    return ssr
    
# Exercise 3
def ssr_vec(y: list,x: list,beta_0: float,beta_1: float) -> float:
    """Calculates the value of the sum of squared residuals
        of the regression model.
        Precondition: length of y must equal length of x.
        
    >>> ssr_vec(numpy.array([[1,2,3]]),numpy.array([[4,5,6]]),7.0,8.0)
    6173.0
    >>> ssr_vec(numpy.array([[2.0,0.0,-1.0]]),numpy.array([[10.0,-5.0,2.0]]),1.0,2.0)
    478.0
    >>> ssr_vec(numpy.array([[2]]),numpy.array([[3,4]]),5,6)
    None
    """
    if len(x) != len(y):
        return None
    else:
        ssr = ((y-beta_0-beta_1*x)**2) 
    return numpy.sum ([ssr])

# Exercise 4
def logit_like_sum(y: list,x: list,beta_0: float,beta_1: float) -> float:
    """Return the value of the logit link function when yi=1,or 
    return 1-logit link function when yi=0.

    >>> logit_like_sum([1,0],[13,0], 0, 0)
    -1.3862943611198906
    >>> logit_like_sum([0,1,0,1,1], [0.0,12.5,2.6,1,3], math.log(2), 2.0)
    -7.061229058181034
    >>> logit_like_sum([1,3], [1.0,12], 0.0, math.log(5))
    None
    """
    like = 0
    
    for i in range(len(y)):
        if y[i] == 0:
            like += math.log(1 - (math.exp(beta_0 + x[i]*beta_1)/(1 + math.exp(beta_0 + x[i]*beta_1))))
        elif y[i] == 1:
            like += math.log(math.exp(beta_0 + x[i]*beta_1)/(1 + math.exp(beta_0 + x[i]*beta_1)))
        else:
            print("Warning: y is not binary. y should be either 1 or 0.")
            like = None
        
    return like

# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 

doctest.testmod()

# Make sure to include exampes in your docstring
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 




##################################################
# End
##################################################
