import sqlite3

expenses = []
gains = []

def connect():
    conn = sqlite3.connect('bookkeeper.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY ,date text, expenses double, gains double)")
    conn.commit()
    conn.close()

def insert(date, expense):
    conn = sqlite3.connect('bookkeeper.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO test VALUES(NULL,?,?,?,?)", (date, expense))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('bookkeeper.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM test")
    row = cur.fetchall()
    conn.close()
    print(row)

def total_difference(expenses, gains):
    total_expenses = sum(expenses)
    total_gains = sum(gains)
    return total_gains - total_expenses

connect()

option=int(input('''What do you want to do
1) insert entity
2) view all
3) edit
4) update
5) delete
6) search'''))

def delete(date = "", expenses = "", gains = ""):
    conn = sqlite3.connect('bookkeeper.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM test WHERE date = ? OR expenses = ? OR gains = ?", (a, b, c))
    row = cur.fetchall()
    index = row[0][0]

    cur.execute("DELETE FROM test WHERE id = ?",(index,))
    conn.commit()
    conn.close()

if option == 1:

    a = str(input('Enter your name: '))
    b = int(input('Enter your phone number: '))
    c = int(input('Enter number of days you will be staying: '))

elif option == 2:
    view()

elif option == 5:
    a = input('Enter your name: ')
    b = input('Enter your phone number: ')
    c = input('Enter number of days you will be staying: ')
    delete(a, b, c)