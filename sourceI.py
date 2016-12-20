import pymssql
conn = pymssql.connect(host='cypress.csil.sfu.ca', user='s_jsoliman', password='jGTL34g3TGre6Tyr', database='AdventureWorks')

cur = conn.cursor()

cur.execute('SELECT COUNT(CustomerID) from Sales.Customer')
row = cur.fetchone()

print "Total amount of Customers:", row[0]

conn.close()

