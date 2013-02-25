#!/usr/bin/python
#author:chenbinghuilove
#content:change one of slaves to master,and continue work
#   m             s2  
#  / \   ---->     \
# s1  s2       m     s1
#date:2013/02/25
import os
import time
class Server(object):
        def __init__(self, **kwargs):
                for k, v in kwargs.iteritems():
                     setattr(self, k, v)
        def check_slave(self,server):
                slaveIO="/etc/dbCluster/mysqlha_login.sh -P %s -e 'show slave status\G;' | grep Slave_IO_Running |awk '{print$2}'" %(server.port)

                slaveSQL="/etc/dbCluster/mysqlha_login.sh -P %s -e 'show slave status\G;' | grep Slave_SQL_Running |awk '{print$2}'" %(server.port)
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
        def replicate_to_position(self,server,position):
                slaveSql1="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'start slave until master_log_file=%s,master_log_pos=%s", %(server.port,server.ip,position.file,position.pos)
                slaveSql2="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'select master_pos_wait(%s,%s)", %(pos.file,pos.pos)
                os.popen(slaveSql1)
                time.sleep(3)
                os.popen(slaveSql2)
        def fetch_slave_position(self,server):
                slavePos="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'show slave status\G;' | grep Exec_Master_Log_Pos |awk '{print$2}'" %(server.port,server.ip)
                return os.popen(slavePos).readlines().[-1].strip()

        def fetch_slave_file(self,server):
                slavePos="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'show slave status\G;' | grep Master_Log_File |awk '{print$2}'" %(server.port,server.ip)
                return os.popen(slavePos).readlines().[-1].strip()
        def change_master(self,server,master,position):
                changeSql="/etc/dbCluster/mysqlha_login.sh -P %s -h %s -e 'change master to MASTER_HOST=%s,MASTER_PORT=%s,MASTER_USER=%s,MASTER_PASSWORD=%s,MASTER_LOG_FILE=%s,MASTER_LOG_POS=%s'" %(server.port,server.ip,master.host,master.port,master.user,master.passwd,position.file,position.pos)
                os.popen(changeSql)
        #主函数主要的迁移过程，适合一主两从的情况
        def switch_to_master(self,slave1,slave2):
                self.stop_slave(slave1)
                self.stop_slave(slave2)
                slave1_pos=self.fetch_slave_position(slave1)
                slave2_pos=self.fetch_slave_position(slave2)
                position.file=self.fetch_slave_file(slave1)
                #选择合适的salve作为master，通过比较POS的值的大小来确定。
                if slave1_pos < slave2_pos:
                        position.pos=slave2_pos
                        self.replicate_to_position(slave2,position)
                        self.change_master(slave1,slave1,position)
                else:
                        position.pos=slave1_pos
                        self.replicate_to_position(slave1,position)
                        self.change_master(slave2,slave2,position)

                self.start_slave(slave1)
                self.start_slave(slave2)

#参数position实体化过程
class Position(object):
        def __init__(self, **kwargs):
                for k, v in kwargs.iteritems():
                        setattr(self, k, v)
#参数master实体化过程
class Master(object):
        def __init__(self, **kwargs):
                for k, v in kwargs.iteritems():
                        setattr(self, k, v)

if __name__=="__main__":
        server=Server()
        server.port=7999
        server.ip='10.5.110.234'
        print server.port
        print server.ip
         test=Server()
        result=test.check_slave(serve)
        print result
        if result == 0:
                test.stop_slave(serve)
        else:
                test.start_slave(serve)
        time.sleep(5)
        test.check_slave(serve)
        master=Master()
        master.host='localhost'
        master.port=8008
        master.user='replic'
        master.passwd='replic'
        position=Position()
        position.file='mysql-bin20007.log'
        position.pos=444
        test.change_master(serve,master,position)

