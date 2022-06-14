# this works!

import pymysql


def mysqlconnect():
    database_connect = pymysql.connect(
        host="localhost", user="mmcgee", password="QAZwsx!23$", db="author"
    )

    cur = database_connect.cursor()

    cur.execute("describe AUTHORS")

    output = cur.fetchall()
    for i in output:
        print(i)

    database_connect.close()


if __name__ == "__main__":
    mysqlconnect()
