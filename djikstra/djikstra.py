#!/usr/bin/python

from collections import deque
import mysql.connector, time

def connect():
    #connects to the database in order to read node and edge data 
    try:
        conn = mysql.connector.connect(
            host="mysql",
            database="djikstra",
            user="djikstra",
            password="G3n3r1cP@ssw0rd!"
        )
    except mysql.connector.Error as err:
        #this boots way faster than the DB in Docker, automating restart
        print("Something went wrong: {}".format(err))
        time.sleep(15)
        return connect()

    return conn

def routingTable(start, values, pending):
    '''
Given a node to check paths from, a set of current path values, and the queue of pending
nodes to check, check the nodes adjacent to the current node to see if a path formed here
is shorter than any previous path.  Updates values, and appends any updated nodes to the queue to 
check or recheck.
    '''
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT weight, destination FROM edges WHERE source=%s", (start,))
    for result in cursor:
        if values[result[1]] > (values[start] + result[0]) or values[result[1]] == 0: 
            values.update({result[1] : (values[start] + result[0])})
            pending.append(result[1])



values = {i : 0 for i in (0, 1, 2, 4, 5, 7, 9, 10)}
pending = deque()
pending.append(0)

while len(pending) > 0:
    print(values)
    routingTable(pending.popleft(), values, pending)

