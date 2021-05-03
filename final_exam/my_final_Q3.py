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
# Script for Question 3
#
##################################################
"""





##################################################
# Import Required Modules
##################################################

# import name_of_module

import os
import pandas as pd
import sqlite3 as dbapi

##################################################
# Set Working Directory.
##################################################


# Find out the current directory.
os.getcwd()
# Change to a new directory.
git_path = 'C:\\Users\\kelvi\\OneDrive\\Documents\\GitHub\\SongjieYin-ECP3004S21\\'
os.chdir(git_path + 'final_exam')
# Check that the change was successful.
os.getcwd()



#--------------------------------------------------
# Question 3, part a
#--------------------------------------------------


# Read the US roads data into Python.
con = dbapi.connect('population.db')

cur = con.cursor()
cur.execute('''CREATE TABLE ROADS(State TEXT,
 Road_miles INTEGER, Speed_limit REAL)''')

con.commit()

roads_df = pd.read_csv('US_state_roads.csv')

roads_df.dtypes

for row in roads_df.index:
   cur.execute('INSERT INTO ROADS VALUES (?, ?, ?)', 
               (str(roads_df['state'][row]), 
                int(roads_df['road_miles'][row]), 
                float(roads_df['speed_limit'][row]) ))
con.commit()

#--------------------------------------------------
# Question 3, part b
#--------------------------------------------------


# List the states and speed limits 
# for the states with speed limits greater than or equal to 75 mph. 

cur.execute('SELECT State FROM Roads')
for row in cur.fetchall():
    print(row)

cur.execute('SELECT Speed_limit FROM Roads')
for row in cur.fetchall():
    print(row)

cur.execute('SELECT State FROM Roads WHERE Speed_limit >= 75')
for row in cur.fetchall():
    print(row)

#--------------------------------------------------
# Question 3, part c
#--------------------------------------------------

# i. Calculate the average length of road miles across all states. 

cur.execute('SELECT AVG(Road_miles) FROM Roads')
for row in cur.fetchall():
    print(row)

# ii. Calculate the average length of road miles 
# for the states with speed limits greater than or equal to 75 mph. 

cur.execute('''SELECT AVG(Road_miles) FROM Roads
            WHERE Speed_limit >= 75''')
print(cur.fetchone())

#--------------------------------------------------
# Question 3, part d
#--------------------------------------------------

# Read in the Density data from Assignment 8.

density_df = pd.read_csv('US_state_pop_area.csv')

density_df.dtypes

cur = con.cursor()
cur.execute('''CREATE TABLE Density(State TEXT,
 Population INTEGER, Area REAL)''')
con.commit()

for row in density_df.index:
   cur.execute('INSERT INTO Density VALUES (?, ?, ?)', 
               (str(density_df['state_terr'][row]), 
                int(density_df['population'][row]), 
                float(density_df['area'][row]) ))
con.commit()

cur.execute('SELECT * FROM Density')
for row in cur.fetchall():
    print(row)


#--------------------------------------------------
# Question 3, part e
#--------------------------------------------------


# i. Calculate a list of the state names 
# and the number of lane miles per person. 
# List them in increasing order from highest to lowest 
# lane miles per person.

cur.execute('''SELECT Density.State, (Density.Population / Roads.Road_miles)
            FROM Roads INNER JOIN Density
            WHERE Roads.State = Density.State
            ORDER BY (Density.Population / Roads.Road_miles) DESC''')
for row in cur.fetchall():
    print(row)


# ii. Calculate a list of the state names 
# and the number of lane miles per square mile of land area. 
# List them in increasing order from highest to lowest 
# lane miles per square mile.

cur.execute('''SELECT Density.State, (Roads.Road_miles / Density.area)
            FROM Roads INNER JOIN Density
            WHERE Roads.State = Density.State
            ORDER BY (Roads.Road_miles / Density.area) DESC''')
for row in cur.fetchall():
    print(row)


##################################################
# End
##################################################



