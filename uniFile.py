#!/usr/bin/python
#coding=utf-8
#filename:uniFile.py
CODEC='utf-8'
FILE='unicode.txt'
hello_out=u"hello world\n"
byte_out=hello_out.encode(CODEC)
f=open(FILE,'w')
f.write(byte_out)
f.close()

f=open(FILE,'r')
byte_in=f.read()
f.close()
hello_in=byte_in.decode(CODEC)
print hello_in
