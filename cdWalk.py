#!/usr/bin/python
#coding=utf-8
#filename:cdWalk.py
import os,sys
def cdWalker(CDROW,cdfile):
        result=[]
        for root,dirs,files in os.walk(CDROW):
                result.append("%s %s %s" %(root,dirs,files))
		print root
        open(cdfile,'w').write('\n'.join(result))
	
