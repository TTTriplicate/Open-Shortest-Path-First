#!/usr/bin/python

import mysql.connector, json

def connect():
    conn = mysql.connector.connect(
        host="127.0.0.1",
        database="djikstra",
        user="djikstra",
        password="G3n3r1cP@ssw0rd!"
    )

    return conn

def routingTable(start, ref values):
    print(values)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT weight, destination FROM edges WHERE source=" + str(start))
    for result in cursor:
        values.update({result[1] : values[result[1]] + result[0]})
    print(values)



def showDatabases():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SHOW DATABASES")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    return cursor.rowcount

def validateLogin(user, password):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT username from USERS WHERE username=%s AND password=%s", (user, password))
    result = cursor.fetchall()
    if len(result) == 1:
        return True
    else:
        return False