#!/usr/bin/python

import MySqlConn.connector as conn

values = {i : 0 for i in (0, 1, 2, 4, 5, 7, 9, 10)}
conn.routingTable(0, values)