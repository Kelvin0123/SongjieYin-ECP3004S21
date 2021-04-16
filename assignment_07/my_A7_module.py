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

def g(x):
    """
    """
    
    return (x-2)*x*(x+2)**2

def g_prime(x):
    """
    """
    
    return 2(x+2)(2*x**2-x-2)

def g_2prime(x):
    """
    """
    
    return 12*x**2+12*x-8

# Exercise 2

def newton_g_opt(x_0,maxiter,tol):
    return



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
