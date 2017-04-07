# database-connection
## Author
Jason Soliman

## Compile Notes

Both parts were made and run on Python 2.7.12 in CSIL. A python package PyMySQL was imported to retrieve data from the CSIL SQL server.
All programs are connected to my own personal account on Cypress, and are already included in the code.
The database "AdventureWorks" in CSIL's SQL server is used for both programs.

## Implementations
### Part 1. Database Connection 

This program imports PyMySQL and connects to cypress using my own account. A cursor is created and an SQL query is executed, selecting the total count of customers in AdventureWorks.
The count, now in a table with 1 row/1 column, is printed to the user. There is no user input needed; only a run of the .py file.


### Part 2. Stored Procedures/Functions

This program contains a function called AverageCost, which is connected to Cypress. AverageCost function takes a string input colour and executes a query that selects the average of all the prices of products of that colour in AdventureWorks.
The result is the average cost of the products that are the colour of the parameter given.
The function is called with the parameter 'Red', and prints to show the average StandardCost of red products in the Product table.

### Extra Feature
User input functionality to find the average cost of parts of any colour is implemented.
The function is called after the user inputs a valid input in python shell. If an incorrect input is given, the user will be asked to try again.
With a valid input, AverageCost prints the average cost of products that is the colour that the user has given.

