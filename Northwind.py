import sqlite3
from sqlite3 import Error

conn = sqlite3.connect('northwind_small (1).sqlite3')
c = conn.cursor()
c.execute("SELECT * FROM Product ORDER BY UnitPrice DESC")
# print(c.fetchmany(10))
# print("Average age at hire:", 
# 	c.execute("SELECT AVG(HireDate - BirthDate) from Employee").fetchall(),
# 	"years old.")
c.execute("""SELECT Product.ProductName, 
	Product.SupplierId, 
	Product.UnitPrice, 
	Supplier.Id, 
	Supplier.CompanyName
FROM [Product] JOIN Supplier
ON [Product].SupplierId = Supplier.Id
ORDER BY UnitPrice DESC""")
print(c.fetchmany(10))
print("The largest category is:",
	c.execute("""SELECT COUNT(Id), CategoryName
FROM ProductDetails_V
GROUP BY CategoryName
ORDER BY COUNT(Id) DESC""").fetchone())
c.close()
conn.commit()