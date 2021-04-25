# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 18:01:14 2021

@author: kelvi
"""

##################################################
# Import Modules.
##################################################

import os

import sqlite3

import csv

##################################################
# Set Working Directory.
##################################################

os.getcwd()
git_path = 'C:\\Users\\kelvi\\OneDrive\\Documents\\GitHub\\SongjieYin-ECP3004S21\\'
os.chdir(git_path + 'assignment_08')
os.getcwd()


# Question 1:
    
# a) Create a new database called population.db.

con = sqlite3.connect('population.db')
cur = con.cursor()

# b) Make a database table called Density that will hold the name of the state 
# or territory (TEXT), the population (INTEGER), and the land area (REAL).

cur.execute('CREATE TABLE Density(State TEXT, Population INTEGER, area REAL)')

# c) Insert the data from the table above.

table_file = open("US_state_pop_area.csv")
rows = csv.reader(table_file)
cur.executemany("INSERT INTO Density VALUES (?, ?, ?)",rows)

# d) Retrieve the contents of the table.

cur.execute('''SELECT * FROM Density''')
for row in cur.fetchall():
    print(row)

# e) Retrieve the populations.

cur.execute('SELECT Population FROM Density;')
for row in cur.fetchall():
    print(row)

# f) Retrieve the states that have populations of less than one million.

cur.execute('SELECT state FROM Density WHERE Population < 1000000;')
for row in cur.fetchall():
    print(row)

# g) Retrieve the states that have populations of less than one million or 
# greater than five million.

cur.execute('SELECT state FROM Density WHERE Population < 1000000 OR Population > 5000000;')
for row in cur.fetchall():
    print(row)

# h) Retrieve the states that do not have populations of less than one million 
# or greater than five million.

cur.execute('SELECT state FROM Density WHERE NOT (Population < 1000000 OR Population > 5000000);')
for row in cur.fetchall():
    print(row)


# i) Retrieve the populations of states that have a land area greater than 
# 200,000 square miles.

cur.execute('SELECT population FROM Density WHERE area > 200000;')
for row in cur.fetchall():
    print(row)

# j) Retrieve the states along with their population densities (population 
# divided by land area).

cur.execute('SELECT state, population/area FROM Density;')
for row in cur.fetchall():
    print(row)

# Question 2: