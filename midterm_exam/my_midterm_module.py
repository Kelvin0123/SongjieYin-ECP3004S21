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
# Sample Script for Midterm Exam: 
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

import numpy as np

##################################################
# Function Definitions
##################################################

# Only function definitions here - no other calculations. 

# Exercise 1


def in_budget(x: float, y: float,p_x: float, p_y: float,w: float) -> bool:
    """
    Preconditions: x, y, w >= 0 and p_x, p_y > 0
    
    Calculates returns a boolean indicator 
    of whether the consumer's expenditure 
    is less than or equal to wealth.
    
    >>> in_budget(3, 1, 10, 25, 100)
    True
    >>> in_budget(2, 2, 2, 2, 2)
    False
    >>> in_budget(50, 20, 5, 5, 3)
    False
    
    """
    exp = x*p_x + y*p_y
    
    if exp < w:
        return True
    else:
        return False

# Exercise 2


def calc_bundle(p_x: float,p_y: float,w: float,alpha: float) -> list:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    
    >>> calc_bundle(10, 20, 120, 1.0/3.0)
    [4.0, 4.0]
    >>> calc_bundle(5, 10, 15, 2.5)
    [7.5, -2.25]
    >>> calc_bundle(2, 4, 6, 8)
    [24.0, -10.5]
    
    """
    x_star = (alpha/p_x)*w
    
    y_star = ((1-alpha)/p_y)*w
    
    return [x_star,y_star]

# Exercise 3


def y_solve(x_star: float,p_x: float,p_y: float,w: float) -> float:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= x_star <= w/p_x
    
    Calculates the remaining expenditure on good y, 
    given an expenditure x_star in good x.
    
    >>> y_solve(5, 5, 10, 100)
    7.5
    >>> y_solve(10, 20, 30, 60)
    -4.666666666666667
    >>> y_solve(1, 2, 3, 5)
    1.0
    
    """
    y_star = (w - x_star*p_x)/p_y
    
    return y_star

# Exercise 4


def one_loop_bundle(p_x: float,p_y: float,w: float,alpha: float,step: float) -> list:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over a loop on x_star and assigns the remaining
    wealth to y using y_solve.
    
    >>> one_loop_bundle(5, 10, 100, 0.25, 0.01)
    [5.0, 7.5]
    >>> one_loop_bundle(5, 10, 100, 0.25, 0.01)
    answer_you_expect
    >>> one_loop_bundle(5, 10, 100, 0.25, 0.01)
    answer_you_expect
    
    """
    max_util = 0
    max_y_star = 0
    i_max = None
    
    x_star_list = np.arange(0,w/p_x,step)
    
    for i in range(len(x_star_list)):
       
        x_star = x_star_list[i]
        
        y_star = y_solve(x_star,p_x,p_y,w)

        util = (x_star**alpha)*y_star**(1-alpha)

        if max_util < util:
            
            max_util = util
        
            max_y_star = y_star
        
            i_max = i

    return [x_star_list[i_max],max_y_star]

# Exercise 5


def util_in_budget(x: float,y: float,p_x: float,p_y: float,w: float,alpha: float) -> float:
    """Calculates the value of the Cobb-Douglass utility
    function for consumption goods x and y with exponent alpha.
    It restricts x and y to non-negative values and 
    alpha to the unit interval.
    It also restricts the calculation to bundles [x, y] within budget w, 
    otherwise it assigns zero.
    
    >>> util_in_budget(4, 4, 10, 20, 120, 1.0/3.0)
    4.0
    >>> util_in_budget(0, 0, 0, 0, 0, 4)
    None
    >>> util_in_budget(10, 20, 30, 40, 200, 0.5)
    14.142135623730953
    
    """
    if x>=0 and y>=0 and p_x>=0 and p_y>=0 and alpha<=1 and alpha>=0:
        util = (x**alpha)*y**(1-alpha)
    else:
        return None
    
    return util

# Exercise 6


def two_loop_bundle(p_x,p_y,w,alpha,step) -> list:
    """
    Preconditions: w >= 0 and p_x, p_y > 0 and 0 <= alpha <= 1
    
    Calculates the consumer's optimal bundle of goods
    for a consumer with Cobb-Douglass utility function.
    It searches over two loops on x_star and y_star.
    
    Note that there is no error handling
    because that is taken care of in util_in_budget() and np.arange(). 
    
    >>> two_loop_bundle(10, 25, 100, 0.5, 0.01)
    [5.0, 2.0]

    """
    x_star_list = np.arange(0,w/p_x,step)
    y_star_list = np.arange(0,w/p_y,step)
    
    max_util = 0
    
    i_max = None
    j_max = None

    for i in range(len(x_star_list)):
       for j in range(len(y_star_list)):
           
           x = x_star_list[i]
           y = y_star_list[j]

           util = util_in_budget(x, y, p_x, p_y, w, alpha)

           if max_util < util:
               
               max_util = util
        
               i_max = i
               j_max = j
               
    if (i_max is not None and j_max is not None):
        return [x_star_list[i_max], y_star_list[j_max]]
    else:
        return None

                
# Only function definitions above this point. 


##################################################
# Test the examples in your docstrings
##################################################


# Question 2: Test using the doctest module. 


# Make sure to include exampes in your docstrings above
# with the proper formatting. 

# Test all functions with three examples each. 

# Choose good examples that will test interesting cases. 
# Make sure they all work correctly. 


# Add code so that the tests are implemented below 
# -- but only when the script is run,
# not when it is imported. 



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    


##################################################
# End
##################################################

