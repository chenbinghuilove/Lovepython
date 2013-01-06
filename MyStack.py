#!/usr/bin/python
#coding=utf-8
#filename:MyStack.py
class MyStacker(object):
	'''
	   mystack 自定义栈，主要的操作put(),get(),isEmpty()
	'''
	def __init__(self,max):
		'''初始化栈头指针和清空栈'''
		self.head=-1
		self.max=max
		self.stack=list()#这里使用list列表来存储数据
		for i in range(self.max):
			self.stack.append(0)#这里是初始化stack的长度，也就是分配存储空间
	def put(self,item):	
		#首先判断是否超出了栈的长度
		if self.head>=self.max:
			return '栈已满，请先删除部分数据'
		else:
			self.head+=1
			self.stack[self.head]=item
			print 'put %s successfully' %item
	def get(self):
		print '进入get函数中'
		if self.head<0:	
			return '栈已空，请先插入数据'
		else:
			print '判断通过'
			self.head-=1
			print self.head
			return self.stack[self.head+1]#此处这样写的目的是为了能够取到我们需要的那个数据，并且self.head还要减1
	def isEmpty(self):
		if self.head<-1:
			print '该栈为空'
			return True
		else:
			print '该栈不为空,数据为%s' %self.stack
			return False
if __name__=='__main__':
	mystack=MyStacker(10)
	mystack.put('a')
	mystack.put('chen')
	mystack.put('zhou')
	print mystack.get()
	print '##########'
	mystack.isEmpty()
	print mystack.get()
	
