# database-connection





## Overview

Both parts were made and run on Python 2.7.12 in CSIL. A python package PyMySQL was imported to retrieve data from the CSIL SQL server.
All programs connect to my own personal account on cypress, and are already included in the code.
The database "AdventureWorks" in CSIL's SQL server is used for both programs.


## Part 1. Database Connection (354A3Part1.py)

This program imports PyMySQL and connects to cypress using my own account. A cursor is created and an SQL query is executed, selecting the total count of customers in AdventureWorks.
The count, now in a table with 1 row/1 column, is printed to the user. There is no user input needed; only a run of the .py file.



## Part 2. Stored Procedures/Functions.

This program contains a function called AverageCost, which connects to cypress, takes a string input colour and executes a query that selects the average of all the prices of products in AdventureWorks.
The result is the average cost of the products that are the colour of the parameter given.
The function is called with the parameter 'Red', and prints to shell the average StandardCost of red products in the Product table.

## Part 2 - Extra
Added user input functionality to find the average cost of parts of any colour.
The function is called after a user inputs a valid input in python shell. If an incorrect input is given the user will be asked to try again.
After the user has given a valid input, AverageCost prints the average cost of products that are the colour that the user had given.

