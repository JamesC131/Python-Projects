import sqlite3


def connect():
    conn = sqlite3.connect('1.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY ,name text, phone_number integer, no_of_days integer, total integer)")
    conn.commit()
    conn.close()

def insert(name, phone_number, no_of_days):
    conn = sqlite3.connect('1.db')
    cur = conn.cursor()
    cur.execute("INSERT INTO test VALUES(NULL,?,?,?,?)", (name,phone_number,no_of_days,calculator(no_of_days)))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM test")
    row = cur.fetchall()
    conn.close()
    print(row)

def calculator(no_of_days):
    total = 1000 * no_of_days
    return total

connect()

option=int(input('''What do you want to do
1) insert entity
2) view all
3) edit
4) update
5) delete
6) search'''))


def search(a, b, c):
    conn = sqlite3.connect('1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM test WHERE name = ? OR phone_number = ? OR no_of_days = ?",(a,b,c))
    row = cur.fetchall()
    conn.close()
    print(row)


def edit(a, b, c):
    conn = sqlite3.connect('1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM test WHERE name = ? OR phone_number = ? OR no_of_days = ?", (a, b, c))
    row = cur.fetchall()
    index = row[0][0]

    x = input('Enter your edited name: ')
    y = input('Enter your edited phone number: ')
    z = input('Enter your edited number of days staying: ')

    cur.execute("UPDATE test SET name = ?, phone_number = ?, no_of_days = ?, total = ? WHERE id = ?",(x,y,z,calculator(z),index))
    conn.commit()
    conn.close()


def delete(name = "", phone_number = "", no_of_days = ""):
    conn = sqlite3.connect('1.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM test WHERE name = ? OR phone_number = ? OR no_of_days = ?", (a, b, c))
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

elif option == 6:
    a = input('Enter your name: ')
    b = input('Enter your phone number: ')
    c = input('Enter number of days you will be staying: ')
    search(a,b,c)

elif option == 3:
    a = input('Enter your name: ')
    b = input('Enter your phone number: ')
    c = input('Enter number of days you will be staying: ')
    edit(a,b,c)

elif option == 5:
    a = input('Enter your name: ')
    b = input('Enter your phone number: ')
    c = input('Enter number of days you will be staying: ')
    delete(a, b, c)