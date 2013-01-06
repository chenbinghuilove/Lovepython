#!/usr/bin/python
#coding=utf-8
#filename:cdctool.py
import sys,cmd
class PyCDC(cmd.Cmd):
	def __init__(self):
		cmd.Cmd.__init__(self)
	def help_EOF(self):
		print '退出程序 Quit the progrem'
	def do_EOF(self,line):
		sys.exit()
	def help_walk(self):
		print '扫描光盘内容 walk cd and export into .cdc'
	def do_walk(self,filename):
		if filename=='':filename=raw_input('输入cdc的文件名')
		print'扫描光盘内容保存到:%s' %filename
	def help_dir(self):
		print '指定保存/搜索目录'
	def do_dir(self,pathname):
		if pathname=='':pathname=raw_input('输入指定保存的地址')
	def help_find(self):
		print '搜索关键字'
	def do_find(self,keyword):
		if keyword=='':keyword=raw_input('输入关键字')
		print'搜索的关键字：%s'%keyword
if __name__=='__main__':
	cdc=PyCDC()
	cdc.cmdloop()
