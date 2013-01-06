#!/usr/bin/python
#coding=utf-8
#filename:codingTest.py
import sys
import urllib2
import chardet

def blog_detect(blogurl):
	try:
		fp=urllib2.urlopen(blogurl)#了解下就可以了。
	except Exception,e:
		print e
		print 'download exception %s' %blogurl
		return 0
	blog=fp.read()
#	print blog
	codedetect=chardet.detect(blog)["encoding"]#主要的操作之一
	print '%s------>%s' %(blogurl,codedetect)
	fp.close()
	print '########进行转换#####'
	if codedetect<>'utf-8':
		try:
			#这里是代码的核心，也是python文本编码的主要用法所在unicode和ASCII这两种编码方式
			blog=unicode(blog,codedetect)#进行解码操作
			blog=blog.encode('utf-8')#进行编码操作
		except:
			print 'bad unicode encode try'
			print 'failed convert'
			return 0
	filename='%s_utf-8' %blogurl[7:]#存储的是文件名以博客的链接来命名的
	filename=filename.replace('/','_')
	open(filename,'w').write(blog)
	print 'save to file %s' %filename
	return 1	
if __name__=='__main__':
	if len(sys.argv)==1:
		print 'usage:\n\t python codingTest.py http://'	
	else:
		blog_detect(sys.argv[1])
