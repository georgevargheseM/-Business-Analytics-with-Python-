import sqlite3

X = sqlite3.connect('SQL11FEB6.db')
Y = X.cursor()

print("A new Database is created")
Y.execute('''CREATE TABLE IF NOT EXISTS COMPANY 
             (ID INT,
              NAME TEXT NOT NULL,
              Date_Join text,
              Place text,
              Salary integer,
              Age real);''')
             
Y.execute('''INSERT INTO COMPANY
             VALUES
             (1,'George','2020-01-01',
              'Kerala', 25000,25),
             (2,'Jojo','2020-01-01',
              'Kerala', 30000,20),
             (3,'Colin','2020-02-05',
              'Bihar', 65000,19),
             (4,'Ebin','2020-02-10',
              'Kerala', 50000,20),
             (5,'Darren','2020-03-02',
              'Kuwait', 40000,20);''')
print("A new Table is created ");


Y.execute('''UPDATE COMPANY SET Salary = 50000 WHERE ID=1;''')
X.commit()
Y.close()

