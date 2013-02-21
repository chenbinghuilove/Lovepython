#!/usr/bin/python
#content:connect to mysql server
#author:chenbinghuilove
#date:2013/02/21
import sys
import MySQLdb

try:
  conn=MySQLdb.connect(db="test",
                        host="localhost",
                        user="root",
                        passwd="123",
                        unix_socket="/tmp/mysql7999.sock")

  cursor=conn.cursor()
  cursor.execute("select * from replic")
  print "Rows selected:",cursor.rowcount

  for row in cursor.fetchall():
    print "replic:",row[0],row[1]
  cursor.close()
  print "Connected"
except MySQLdb.Error,e:
  print "Cannot connect to server"
  print "Error code:",e.args[0]
  print "Error message:",e.args[1]
  sys.exit(1)

