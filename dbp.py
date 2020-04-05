import sqlite3

conn=sqlite3.connect('data.db')
c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS data(name TEXT,hours REAL)')




def insert_data(name,hours):
    
    c.execute('SELECT * FROM data WHERE name=?',(name,))
    data=c.fetchall()
    
    if(data):
        
        c.execute('UPDATE data SET hours=? WHERE name=?',(hours+data[0][1],name))
    else:
        c.execute('INSERT INTO data (name,hours) VALUES (?,?)',(name,hours))
    
    conn.commit()
    
def find(name):
    c.execute('SELECT * FROM data WHERE name=?',(name,))
    data=c.fetchall()
    if(data):
        return f'You have coded {(data[0][1])} hours'
    else:
        return "Start coding now you lazy ass!"
'''
create_table()
insert_data("varun","code",1)
c.execute('SELECT * FROM data')
data=c.fetchall()
print(data)

c.close()
conn.close()
'''