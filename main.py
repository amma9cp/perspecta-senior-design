import os,sys,time
import logging

if __main__ == '__main__':
	base = "http://boxstarter.org/package/nr/url?"
	print("[-] 01/28/2019 Demo - Ammar Al-Kahfah")
	script_url = input("[~] Enter BoxStarter Script URL: ").strip()
	command = base + script_url
	print(command)
	os.system("START {}".format(command))
	
