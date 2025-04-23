import sqlite3

# Step 1: Connect to SQLite Database
conn = sqlite3.connect("one.db")  
c = conn.cursor()

# Uncomment the below lines to create the table & insert records (run only once)

c.execute("CREATE TABLE IF NOT EXISTS EMP(ID INT PRIMARY KEY, NAME TEXT, SALARY REAL)")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(101, 'ABC', 1000)")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(102, 'DEF', 5000)")
c.execute("INSERT INTO EMP(ID, NAME, SALARY) VALUES(103, 'GHI', 7000)")
conn.commit()  # commit usage


# Step 2: Fetch All Records
c.execute("SELECT * FROM EMP")
rows = c.fetchall()  # Fetch all results

print("Initial Employee Records:")
for row in rows:
    print(row)

# Step 3: Update Salary for ID = 101
c.execute("UPDATE EMP SET SALARY = 3000 WHERE ID = 101")
conn.commit()  # commit usage

# Step 4: Fetch Updated Record
c.execute("SELECT * FROM EMP WHERE ID = 101")
print("\nUpdated Employee Record (ID=101):", c.fetchone())

# Step 5: Delete Employee with ID = 103
c.execute("DELETE FROM EMP WHERE ID = 103")
conn.commit()  # commit usage

# Step 6: Fetch All Records After Deletion
c.execute("SELECT * FROM EMP")
rows = c.fetchall()

print("\nEmployee Records After Deletion:")
for row in rows:
    print(row)



