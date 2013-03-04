#!/usr/bin/python
#author:chenbinghuilove
#date:2013/03/04

#with open('jules.txt','r') as data:
#	jules=data.readline()
#jules=jules.strip().split(',')
#with open('james.txt','r') as data:
#	james=data.readline()
#james=james.strip().split(',')
#with open('mikey.txt','r') as data:
#	mikey=data.readline()
#mikey=mikey.strip().split(',')
#with open('saran.txt','r') as data:
#	saran=data.readline()
#saran=saran.strip().split(',')



def unity_data(time_string):
	if '-' in time_string:
		spliter='-'
	elif ':' in time_string:
		spliter=':'
	else:
		return time_string
	(mins,secs)=time_string.split(spliter)
	return (mins+'.'+secs)
def fetch_data(filename):
	try:
		with open(filename) as f:
			data=f.readline()
		temple=data.strip().split(',')
	#	temp={'name' : temple.pop[0],'birthday' : temple.pop[0],'time' : str(sorted(set([unity_data(t) for t in temple]))[0:3])}
		temp={}
		temp['name']=temple.pop(0)
		temp['birthday']=temple.pop(0)
		temp['time']=str(sorted(set([unity_data(t) for t in temple]))[0:3])
		return (temp)
	except IOError as err:
		print ('File error:'+str(err))
		return(None)

james=fetch_data('james.txt')
jules=fetch_data('jules.txt')
mikey=fetch_data('mikey.txt')
saran=fetch_data('saran.txt')
print (james['name']+"'s fastest times are:"+james['time'])
print (jules['name']+"'s fastest times are:"+jules['time'])
print (mikey['name']+"'s fastest times are:"+mikey['time'])
print (saran['name']+"'s fastest times are:"+saran['time'])

