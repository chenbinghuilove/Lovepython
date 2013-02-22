#!/usr/bin/python
#content:master to slave
#author:chenbinghuilove
#date:2013/02/22
import os
import time
class server:
        def __init__(self):
                pass
        def check_slave(self,port):
                slaveIO="/etc/dbCluster/mysqlha_login.sh -P %s -e 'show slave status\G;' | grep Slave_IO_Running |awk '{print$2}'" %(port)

                slaveSQL="/etc/dbCluster/mysqlha_login.sh -P %s -e 'show slave status\G;' | grep Slave_SQL_Running |awk '{print$2}'" %(port)
                IO=os.popen(slaveIO).readlines()[-1].strip()
                SQL=os.popen(slaveSQL).readlines()[-1].strip()
                if IO == 'No' and SQL == 'No':
                        print "slave is stop"
                else:
                        print "slave is ready"
                        return 0
        def stop_slave(self,server):
                print "##stop slave##"
                slaveSql="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'stop slave'" %(server.port,server.ip)
                os.popen(slaveSql)
        def start_slave(self,server):
                print "##start slave##"
                slaveSql="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'start slave'" %(server.port,server.ip)
                os.popen(slaveSql)
        def replicate_to_position(self,server,pos):
                slaveSql1="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'start slave until master_log_file=%s,master_log_pos=%s", %(server.port,server.ip,pos.file,pos.pos)
                slaveSql2="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'select master_pos_wait(%s,%s)", %(pos.file,pos.pos)
                os.popen(slaveSql1)
                time.sleep(3)
                os.popen(slaveSql2)
        def fetch_slave_position(self,server):
                slavePos="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'show slave status\G;' | grep Exec_Master_Log_Pos |awk '{print$2}'" %(server.port,server.ip)
                return os.popen(slavePos).readlines().[-1].strip()

if __name__=="__main__":
erver=server()
        server.check_slave(8009)
        server.start_slave(8009)
        server.check_slave(8009)

