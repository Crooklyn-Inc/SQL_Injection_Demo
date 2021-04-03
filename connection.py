import mysql.connector
from getpass import getpass

from mysql.connector import MySQLConnection
from prettytable import PrettyTable


def ask_for_login():
    try:
        login = input("Login: ")
        pswd = input("Password: ")
        return login, pswd
    except Exception as e:
        print("Something went wrong!")


def print_res():
    try:
        res = mycursor.fetchall()
        t = PrettyTable(["User name", "User pass", "Type", "Account balance", "Id"])
        if len(res) > 0:
            print("Login successfully!")
            for x in res:
                t.add_row([x[0], x[1], x[2], x[3], x[4]])
            print(t)
    except Exception as e:
        print("login Failed due to: ", e)
    start()


def get_info_bad(login, pswd):
    statement = 'select * from sqlinjdemo.sqlinj where username = \'%s\' and userpass = \'%s\';' % (
        login.lower(), pswd.lower())

    st = statement.split(';')
    try:
        for s in st:
            if len(statement) > 0:
                mycursor.execute(s)
                mydb.commit()
    except Exception as e:
        print("ERROR! ERROR! ERROR! ERROR!")


def get_info_good(login, pswd):
    statement = ("select * from sqlinjdemo.sqlinj where username = %(username)s"
                 " and userpass = %(userpass)s");
    mycursor.execute(statement, {'username': login, 'userpass': pswd})
    result = mycursor.fetchall()
    if len(result) > 0:
        mycursor.execute(statement, {'username': login, 'userpass': pswd})
        mydb.commit()
    else:
        print("!!!!!!!!   Error! Error!!!!!!")


def start():
    log_detail = ask_for_login()
    get_info_bad(log_detail[0], log_detail[1])
    # get_info_good(log_detail[0], log_detail[1])
    print_res()


if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="YegorShramchenko",
        port=3308
    )
    mycursor = mydb.cursor(buffered=True)
    start()
