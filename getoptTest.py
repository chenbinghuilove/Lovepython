#!/usr/bin/python
# -*- coding: utf-8 -*-
#coding=utf-8
import os,sys
import getopt
print sys.argv
CDROW='/home/zhouqian/test'
def cdWalker(CDROW,cdfile):
	result=[]
	for root,dirs,files in os.walk(CDROW):
		result.append("%s %s %s" %(root,dirs,files))
		print root
	open(cdfile,'w').write('\n'.join(result))
def usage():
	print '''pycdc 使用方式：
	python cdays-3-exercise-1.py -d cdc -k 中国火
	#检索cdc中有没有中国火字样的目录，
         '''
try:
	opts,args=getopt.getopt(sys.argv[1:],'hd:e:k:')
except getopt.GetoptError:
	usage()
	sys.exit()

if len(opts)==0:
	usage()
	sys.exit()
c_path=''
name=''
for opt,arg in opts:
	if opt in('-h','--help'):
		usage()
		sys.exit()
	elif opt=='-e':
		if os.path.exists(arg):#判断目标路径是否存在
		#	cdWalker(CDROW,arg)
			print "记录光盘的位置是 %s" %arg
		else:
			print "不存在这样的目录"
	elif opt=='-d':
			c_path=arg
			print c_path
			cdWalker(CDROW,c_path)
	elif opt=='-k':
			if not c_path:
				usage()
				sys.exit()
			else:
				name=arg
				for root,dirs,files in os.walk(c_path):
					if root=='%s' %name:
						print '您要找的文件在%s' %dirs
			
