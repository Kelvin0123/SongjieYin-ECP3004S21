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
        
    >>> ssr_loops([1,2,3],[4,5,6],7.0,8.0)
    """
    ssr=0
    for i in range(len(x)):
            ssr = sum((y[i]-beta_0-beta_1*x[i])**2)
    return ssr

# Exercise 3
def ssr_vec(y,x,beta_0,beta_1):
    
    return


# Exercise 4
def logit_like_sum(y,x,beta_0,beta_1):
    return


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
