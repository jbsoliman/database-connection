import pymssql
conn = pymssql.connect(host='cypress.csil.sfu.ca', user='s_jsoliman', password='jGTL34g3TGre6Tyr', database='jsoliman354')

cur = conn.cursor()

cur.execute("SELECT * from dbo.AverageCost('Red')")
for row in cur:
        print("The average cost of red parts are"),
        print(row[0])


conn.close()

