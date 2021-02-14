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
import doctest

doctest.testmod()

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1

def quad_roots_1(x: float, a: float, b: float, c: float) -> float:
    """Return two real-valued roots of the quadratic equation.

    >>> quad_roots_1(3,1,7,12)
    [-3.0, -4.0]
    >>> quad_roots_1(-5,1,2,-35)
    [5.0, -7.0]
    >>> quad_roots_1(1.5,1,-5.5,6)
    [4.0, 1.5]
    """
    d = (b**2) - (4*a*c)
    x_1 = (-b+math.sqrt(d))/(2*a)
    x_2 = (-b-math.sqrt(d))/(2*a)

    return [x_1,x_2]

# Exercise 2

def quad_roots_real(x: float, a: float, b: float, c: float) -> float:
    """Return two real-valued roots of the quadratic equation.

    >>> quad_roots_real(-3,1,7,12)
    [-3.0, -4.0]
    >>> quad_roots_real(1,1,1,1)
    None
    >>> quad_roots_real(-5,1,2,-35)
    [5.0, -7.0]
    """
    d = (b**2) - (4*a*c) 
    if d<0:
        return None
    x_1 = (-b+math.sqrt(d))/(2*a)
    x_2 = (-b-math.sqrt(d))/(2*a)
        
    return [x_1,x_2]

# Exercise 3

def utility_positive(x: float, y: float, alpha: float) -> float:
    """Return the value of the Cobb-Douglass utility function when x,y,and
    alpha are all positive. If one or more numbers are negative, the code 
    will show the problem of the inputs.
    
    >>> utility_positive(1.0,1.0,0.7)
    1.0
    >>> utility_positive(-4,-8,-2)
    None
    >>> utility_positive(5,2,-8)
    None
    """
    utility=(x**alpha)*(y**(1-alpha))
    
    if x or y or alpha<0:
        if x<0 and y<0 and alpha<0:
           return print ('Please input positive numbers for all.')
        elif y<0 and alpha<0:
           return print ('Please input positive numbers for y and alpha.')
        elif x<0 and alpha<0:
            return print ('Please input positive numbers for x and alpha.')
        elif x<0 and y<0:
            return print ('Please input positive numbers for x and y.')
        elif x<0:
            return print('Please input a positive number for x.')
        elif y<0:
            return print('Please input a positive number for y.')
        elif alpha<0:
            return print('Please input a positive number for alpha.')
        return utility
    
str('Please input a positive number for all.')

# Exercise 4

def logit_like(yi: float,xi: float,beta_0: float,beta_1: float) -> float:
    """Return the value of the logit link function when yi=1,or 
    return 1-logit link function when yi=0.
    
    >>> logit_like(1.0,0.0,0.0,0.0)
    0.5
    >>> logit_like(0.0,0.0,0.0,0.0)
    0.5
    >>> logit_like(1,0.0, math.log(2),2.0)
    2.0/3.0
    """
    link=(math.e**(beta_0+xi*beta_1))/(1+math.e**(beta_0+xi*beta_1))
    
    if yi == 1:
        return link
    if yi == 0:
        return 1-link

# Only function definitions above this point. 


##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating quad_roots_1(3,1,7,12)")
print("Expected: " + str([-3.0,-4.0]))
print("Got: " + str(quad_roots_1(3,1,7,12)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating quad_roots_1(-5,1,2,-35)")
print("Expected: " + str([5.0,-7.0]))
print("Got: " + str(quad_roots_1(-5,1,2,-35)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating quad_roots_1(1.5,1,-5.5,6)")
print("Expected: " + str([4.0,1.5]))
print("Got: " + str(quad_roots_1(1.5,1,-5.5,6)))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating quad_roots_real(-3,1,7,12)")
print("Expected: " + str([-3.0,-4.0]))
print("Got: " + str(quad_roots_real(-3,1,7,12)))


print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating quad_roots_real(1,1,1,1)")
print("Expected: " + str(None))
print("Got: " + str(quad_roots_real(1,1,1,1)))


print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating quad_roots_real(-5,1,2,-35)")
print("Expected: " + str([5.0,-7.0]))
print("Got: " + str(quad_roots_real(-5,1,2,-35)))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating utility_positive(1.0,1.0,0.7)")
print("Expected: " + str(1.0))
print("Got: " + str(utility_positive(1.0,1.0,0.7)))


print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating utility_positive(-4,-8,-2)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(-4,-8,-2)))


print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating utility_positive(5,2,-8)")
print("Expected: " + str(None))
print("Got: " + str(utility_positive(5,2,-8)))

#--------------------------------------------------

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating logit_like(1.0,0.0,0.0,0.0)")
print("Expected: " + str(0.5))
print("Got: " + str(logit_like(1.0,0.0,0.0,0.0)))


print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating logit_like(0.0,0.0,0.0,0.0)")
print("Expected: " + str(0.5))
print("Got: " + str(logit_like(0.0,0.0,0.0,0.0)))


print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating logit_like(1,0.0, math.log(2), 2.0)")
print("Expected: " + str(2.0/3.0))
print("Got: " + str(logit_like(1,0.0, math.log(2), 2.0)))

##################################################
# End
##################################################