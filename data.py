print("Mugheera")
import mysql.connector
from tabulate import tabulate

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="atm"
)

cursor = conn.cursor()

cursor.execute("SELECT * FROM atm")

myresult = cursor.fetchall()

data=[]
for x in myresult:
    x=list(x)
    data.append(x)
table = tabulate(data, headers=["id","Name","username","password","amount"], tablefmt="fancy_grid")
print(table)
