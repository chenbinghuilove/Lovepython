#!/usr/bin/python
#coding:utf-8
#filename:cdays-exercise.py
#author:chenbinghuilove
import os,sys
def get_top_three(path):
	all_file={}#初始化一个字典数据结构
	for root,dirs,files in os.walk(path):
		for onefile in files:
			fname=os.path.join(root,onefile)#字符串进行柔和
			fsize=os.stat(fname).st_size
			if all_file.has_key(fsize):#这里如果有相同大小的则合并起来
				all_file[fsize].append(fname)
			else:	
				all_file[fsize]=[fname]
		fsize_key=all_file.keys()
		fsize_key.sort()
#		print all_file  #测试用
		result=[]#初始化一个列表
	for i in [-1,-2,-3]:#排序算法
		for j in all_file[fsize_key[i]]:
			result.append((fsize_key[i],j))
	return result

if __name__=="__main__":
	if len(sys.argv)==1:
		print "usage python cdays.py /test/python"
	else:
		abs_path=os.path.abspath(sys.argv[1])
		if not os.path.isdir(abs_path):
			print '%s is not exist' %abs_path
		else:
			top=get_top_three(abs_path)
			for(s,f) in top:	
				print '%s---->%s\n' %(f,s)
			
