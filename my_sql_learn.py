import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
    host='localhost',
    user="root",
    passwd="2125253032",
    port="3306",
    database="patiens"
)
c=mydb.cursor()
c.execute("SELECT * FROM add_win")
#c.execute(f"""INSERT INTO add_win
#VALUES ("asd","sfs","123","34","2000-11-11",'asfsdf')
#""")
a=c.fetchall()
########
########pip install mysql-connector-python
############
mydb.commit()
mydb.close()
print(a)
