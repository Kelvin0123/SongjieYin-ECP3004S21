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
# Sample Script for Assignment 2: 
# Function Definitions
#
##################################################
"""


##################################################
# Import Required Modules
##################################################

# import name_of_module


##################################################
# Function Definitions
##################################################

# Exercise 1

def average(num1: float, num2: float) -> float:
    """Return the average of num1 and num2.

    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """

    return (num1 + num2) / 2

# Exercise 2

import math

def area_of_circle(r: float) -> float:
    """Return the area of the circle.
    
    >>> area_of_circle(5)
    78.53981633974483
    >>> area_of_circle(10.5)
    346.3605900582747
    """
    
    return  math.pi*r**2

# Exercise 3

def volume_of_cylinder(r: float,h: float) -> float:
    """Return the volume of the cylinder.
    
    >>>volume_of_cylinder(10,3)
    942.4777960769379
    >>>volume_of_cylinder(5.5,46)
    4371.526177470197
    """
    
    return math.pi*h*r**2

# Exercise 4

def utility(x:float,y:float,α:float) -> float:
    """Return the value of the Cobb-Douglass utility function.
    
    >>>utility(10,5,3)
    40.0
    >>>utility(8.2,6,8)
    73.02172134541375
    """
    
    return x**α*y**(1-α)

# Exercise 5

def logit(x:float,β0:float,β1:float) -> float:
    """Return the value of the logit link function
    >>>logit(16.3,8.6,9.24)
    1.0
    >>>logit(0,6,7)
    0.9975273768433652
    """
    return (math.e**(β0+x*β1))/(1+math.e**(β0+x*β1)) 

##################################################
# Run the examples to test these functions
##################################################


# Test the examples and print the results. 

# Exercise 1

print("#" + 50*"-")
print("Testing my Examples for Exercise 1.")

print("#" + 50*"-")
print("Exercise 1, Example 1:")
print("Evaluating average(10,20)")
print("Expected: " + str(15.0))
print("Got: " + str(average(10,20)))


print("#" + 50*"-")
print("Exercise 1, Example 2:")
print("Evaluating average(2.5, 3.0)")
print("Expected: " + str(2.75))
print("Got: " + str(average(2.5, 3.0)))


print("#" + 50*"-")
print("Exercise 1, Example 3:")
print("Evaluating average(50.25, 8)")
print("Expected: " + str(29.125))
print("Got: " + str(average(50.25, 8)))

# Exercise 2

print("#" + 50*"-")
print("Testing my Examples for Exercise 2.")

print("#" + 50*"-")
print("Exercise 2, Example 1:")
print("Evaluating area_of_circle(5)")
print("Expected: " + str(78.53981633974483))
print("Got: " + str(area_of_circle(5)))

print("#" + 50*"-")
print("Exercise 2, Example 2:")
print("Evaluating area_of_circle(10.5)")
print("Expected: " + str(346.3605900582747))
print("Got: " + str(area_of_circle(10.5)))

print("#" + 50*"-")
print("Exercise 2, Example 3:")
print("Evaluating area_of_circle(50.8)")
print("Expected: " + str(8107.319665559963))
print("Got: " + str(area_of_circle(50.8)))

# Exercise 3

print("#" + 50*"-")
print("Testing my Examples for Exercise 3.")

print("#" + 50*"-")
print("Exercise 3, Example 1:")
print("Evaluating volume_of_cylinder(10,3)")
print("Expected: " + str(942.4777960769379))
print("Got: " + str(volume_of_cylinder(10,3)))

print("#" + 50*"-")
print("Exercise 3, Example 2:")
print("Evaluating volume_of_cylinder(5.5,46)")
print("Expected: " + str(4371.526177470197))
print("Got: " + str(volume_of_cylinder(5.5,46)))

print("#" + 50*"-")
print("Exercise 3, Example 3:")
print("Evaluating volume_of_cylinder(0,3)")
print("Expected: " + str(0.0))
print("Got: " + str(volume_of_cylinder(0,3)))

# Exercise 4

print("#" + 50*"-")
print("Testing my Examples for Exercise 4.")

print("#" + 50*"-")
print("Exercise 4, Example 1:")
print("Evaluating utility(10,5,3)")
print("Expected: " + str(40.0))
print("Got: " + str(utility(10,5,3)))

print("#" + 50*"-")
print("Exercise 4, Example 2:")
print("Evaluating utility(8.2,6,8)")
print("Expected: " + str(73.02172134541375))
print("Got: " + str(utility(8.2,6,8)))

print("#" + 50*"-")
print("Exercise 4, Example 3:")
print("Evaluating utility(2,3,5)")
print("Expected: " + str(0.3950617283950617))
print("Got: " + str(utility(2,3,5)))

# Exercise 5

print("#" + 50*"-")
print("Testing my Examples for Exercise 5.")

print("#" + 50*"-")
print("Exercise 5, Example 1:")
print("Evaluating logit(16.3,8.6,9.24)")
print("Expected: " + str(1.0))
print("Got: " + str(logit(16.3,8.6,9.24)))

print("#" + 50*"-")
print("Exercise 5, Example 2:")
print("Evaluating logit(0,6,7)")
print("Expected: " + str(0.9975273768433652))
print("Got: " + str(logit(0,6,7)))

print("#" + 50*"-")
print("Exercise 5, Example 3:")
print("Evaluating logit(2.3,0,4.5)")
print("Expected: " + str(0.9999680082337281))
print("Got: " + str(logit(2.3,0,4.5)))

# Continue with the rest of your examples.
# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


##################################################
# End
##################################################