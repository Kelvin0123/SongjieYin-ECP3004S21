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

##################################################
# Question 1:
##################################################

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

# Delete the header imported from the CSV file

cur.execute('DELETE FROM Density WHERE State = (SELECT max(State) FROM Density)')

#

con.commit()

# d) Retrieve the contents of the table.

cur.execute('''SELECT * FROM Density''')
for row in cur.fetchall():
    print(row)

# e) Retrieve the populations.

cur.execute('SELECT Population FROM Density;')
for row in cur.fetchall():
    print(row)

# f) Retrieve the states that have populations of less than one million.

cur.execute('SELECT state FROM Density WHERE Population < 1000000')
for row in cur.fetchall():
    print(row)

# g) Retrieve the states that have populations of less than one million or 
# greater than five million.

cur.execute('SELECT state FROM Density WHERE Population < 1000000 OR Population > 5000000')
for row in cur.fetchall():
    print(row)

# h) Retrieve the states that do not have populations of less than one million 
# or greater than five million.

cur.execute('SELECT state FROM Density WHERE NOT (Population < 1000000 OR Population > 5000000)')
for row in cur.fetchall():
    print(row)


# i) Retrieve the populations of states that have a land area greater than 
# 200,000 square miles.

cur.execute('SELECT population FROM Density WHERE area > 200000')
for row in cur.fetchall():
    print(row)

# j) Retrieve the states along with their population densities (population 
# divided by land area).

cur.execute('SELECT state, population/area FROM Density')
for row in cur.fetchall():
    print(row)

##################################################
# Question 2:
##################################################

# a) Retrieve the contents of the table.

cur.execute('''CREATE TABLE Capitals(State TEXT, Capital TEXT, Area REAL, 
            Population INTEGER) ''')

table_file = open("US_cap_cities_pop.csv")
rows = csv.reader(table_file)
cur.executemany("INSERT INTO Capitals VALUES (?, ?, ?, ?)",rows)


# Delete the header imported from the CSV file

cur.execute('DELETE FROM Capitals WHERE State = (SELECT max(State) FROM Capitals)')

#

cur.execute('SELECT * FROM Capitals')
for row in cur.fetchall():
    print(row)

# b) Retrieve the populations of the states and capitals (in a list of tuples 
# of the form [state population,capital population]).

cur.execute('''SELECT Density.population, Capitals.Population FROM Capitals INNER 
            JOIN Density WHERE Capitals.State = Density.State''')
for row in cur.fetchall():
    print(row)

# c) Retrieve the land area of the states whose capitals that have populations 
# greater than 100,000.

cur.execute('SELECT Density.area FROM Density INNER JOIN Capitals\
            ON Density.state = Capitals.State WHERE Capitals.Population > 100000')
for row in cur.fetchall():
    print(row)

# d) Retrieve the states with land densities greater than ten people per 
# square mile and capital city populations more than 500,000.

cur.execute('SELECT Capitals.State FROM Capitals INNER JOIN Density\
            ON Density.state = Capitals.State WHERE\
            Density.population/Density.area > 10 AND Capitals.Population > 500000')
for row in cur.fetchall():
    print(row)

# e) Retrieve the total land area of Canada.
    
cur.execute('SELECT area FROM Density WHERE state = Canada')
for row in cur.fetchall():
    print(row)

# f) Retrieve the average population of the capital cities.

cur.execute('SELECT AVG(Population) FROM Capitals')
print(cur.fetchone())

# g) Retrieve the lowest population of the capital cities.

cur.execute('SELECT MIN(Population) FROM Capitals')
print(cur.fetchone())

# h) Retrieve the highest population of the states or territories.

cur.execute('SELECT MAX(Population) FROM Capitals')
print(cur.fetchone())

# i) Retrieve the states that have land densities within 0.5 persons per 
# square mile of one another. Have each pair of states reported only once.

# This requires a self join: 

cur.execute('SELECT Density.state, Density.population, Capitals.Population\
            FROM Density LEFT JOIN Capitals ON Density.state = Capitals.State\
            WHERE Capitals.State IS NULL')
for row in cur.fetchall():
    print(row)

# j) Revisit item (b) above: Retrieve the populations of the states and 
# capitals (in a list of tuples of the form [state name, state population, 
# capital population]), except modify the query as follows:
# i) List only the rows corresponding to states but not territories.

cur.execute('SELECT Density.state, Density.population, Capitals.Population\
             FROM Density INNER JOIN Capitals ON Density.state = Capitals.State')
for row in cur.fetchall():
    print(row)

# ii) List all rows corresponding to both states and territories. Leave any 
# missing values as None.

cur.execute('SELECT Density.state, Density.population, Capitals.Population\
             FROM Density LEFT JOIN Capitals ON Density.state = Capitals.State\
             WHERE Capitals.State IS NULL')
for row in cur.fetchall():
    print(row)

# This is perfectly correct for 2j. Good work. 