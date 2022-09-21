import pyodbc

server_name = ""
database_name = ""
username = ""
password = ""

print(username)

connection = pyodbc.connect('Driver={SQL Server};'
                            f'Server={server_name};'
                            f'Database={database_name};'
                            f'UID={username};'
                            f'PWD={password};'
                            f'Trusted_Connection=no;')

cursor = connection.cursor()
cursor.execute('SELECT * FROM table_name')

for i in cursor:
    print(i)


cursor.close()
connection.close()
