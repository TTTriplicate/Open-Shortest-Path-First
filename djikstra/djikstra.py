#!/usr/bin/python

from collections import deque
import mysql.connector, time

def connect():
    try:
        conn = mysql.connector.connect(
            host="mysql",
            database="djikstra",
            user="djikstra",
            password="G3n3r1cP@ssw0rd!"
        )
    except mysql.connector.Error as err:
        print("Something went wrong: {}".format(err))
        time.sleep(10)
        return connect()

    return conn

def routingTable(start, values, pending):
    print(values)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT weight, destination FROM edges WHERE source=%s", (start,))
    for result in cursor:
        if values[result[1]] >= (values[start] + result[0]) or values[result[1]] == 0: 
            values.update({result[1] : (values[start] + result[0])})
            pending.append(result[1])



values = {i : 0 for i in (0, 1, 2, 4, 5, 7, 9, 10)}
values.update({0 : 0})
pending = deque()
pending.append(0)

while len(pending) > 0:
    routingTable(pending.popleft(), values, pending)

