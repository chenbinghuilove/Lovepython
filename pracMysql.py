#!/usr/bin/python
#connect practise operation of mysql
#author:chenbinghuilove
#date:2013/02/21
import sys
import MySQLdb
class pyMysql:
        def __init__(self):
                pass
        def connect(self):
                  self.conn=MySQLdb.connect(db="test",
                                        host="localhost",
                                        user="root",
                                        passwd="123",
                                        unix_socket="/tmp/mysql7999.sock")
                  if self.conn.open == 1:
                        print "connect mysql server"
                  else:
                        print "cannot connect mysql server"
        def closeconnect(self):
                self.conn.close()
                print "connect is gone"
        def query(self,sqltext):
                cursor=self.conn.cursor()
                cursor.execute(sqltext)
                print "Rows selected:",cursor.rowcount
                for row in cursor.fetchall():
                   print "note:",row[0],row[1]
                cursor.close()
        def execute(self,sqltext,param):
                cursor=self.conn.cursor()
                result=cursor.execute(sqltext,param)
                self.conn.commit()
                if result==1:
                  print "success"
                else:
                  print "failed"
if __name__=="__main__":
        test=pyMysql()
        test.connect()
	sql="select * from replic"
        test.query(sql)
        insertsql="insert into replic values(%s,%s)"
        param=(11,'chen')
        test.execute(insertsql,param)

