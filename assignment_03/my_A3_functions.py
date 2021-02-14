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
# Sample Script for Assignment 3: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

import math
import cmath

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def quad_roots_1(x: float, a: float, b: float, c: float) -> float:
    """Return two real-valued roots of the quadratic equation.

    >>> quad_roots_1(-3,1,7,12)
    [-3.0,-4.0]
    
    >>> quad_roots_1()
    [0,0]
    
    """
    
    d = (b**2) - (4*a*c)
    x_1 = (-b+math.sqrt(d))/(2*a)
    x_2 = (-b-math.sqrt(d))/(2*a)

    return [x_1,x_2]

# Exercise 2

def quad_roots_real(x: float, a: float, b: float, c: float) -> float:
    """Return two real-valued roots of the quadratic equation.

    >>> quad_roots_real(-3,1,7,12)
    []
    
    >>> quad_roots_real()
    []
    
    """
    
    d = (b**2) - (4*a*c) 
    x_1 = (-b+cmath.sqrt(d))/(2*a)
    x_2 = (-b-cmath.sqrt(d))/(2*a)

    return [x_1,x_2]

# Exercise 3

def utility_positive(x: float, y: float, alpha: float) -> float:
    """Return the value of the Cobb-Douglass utility function when all 
    
    >>> utility_positive()
    
    >>> utility_positive()
    
    """
    
    if x<0:
        return print('Please input a positive number for x.')
    if y<0:
        return print('Please input a positive number for y.')
    if alpha<0:
        return print('Please input a positive number for alpha.')
    else:
        return (x**alpha)*(y**(1-alpha))


# Exercise 4

def logit_like(yi: float,xi: float,Beta_0: float,Beta_1: float) -> float:
    """Return the value of the logit link function when yi=1,or return 1-logit
    link function when yi=0.
    
    >>> logit_like()
    
    >>> logit_like()
    
    """
    
    if yi == 1:
        return (math.e**(Beta_0+xi*Beta_1))/(1+math.e**(Beta_0+xi*Beta_1))
    if yi == 0:
        return (1-(math.e**(Beta_0+xi*Beta_1))/(1+math.e**(Beta_0+xi*Beta_1)))

# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating quad_roots_1()")
print("Expected: " + str())
print("Got: " + str(quad_roots_1()))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating quad_roots_1()")
print("Expected: " + str())
print("Got: " + str(quad_roots_1()))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating quad_roots_1()")
print("Expected: " + str())
print("Got: " + str(quad_roots_1()))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating quad_roots_real()")
print("Expected: " + str())
print("Got: " + str(quad_roots_real()))


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating quad_roots_real()")
print("Expected: " + str())
print("Got: " + str(quad_roots_real()))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating quad_roots_real()")
print("Expected: " + str())
print("Got: " + str(quad_roots_real()))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating utility_positive()")
print("Expected: " + str())
print("Got: " + str(utility_positive()))


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating utility_positive()")
print("Expected: " + str())
print("Got: " + str(utility_positive()))


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating utility_positive()")
print("Expected: " + str())
print("Got: " + str(utility_positive()))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like()")
print("Expected: " + str())
print("Got: " + str(logit_like()))


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating logit_like()")
print("Expected: " + str())
print("Got: " + str(logit_like()))


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating logit_like()")
print("Expected: " + str())
print("Got: " + str(logit_like()))

##################################################
# End
##################################################