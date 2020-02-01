



from warnings import filterwarnings
import threading
from threading import Lock
import dns.resolver
import urllib3
import socket
import requests

http = urllib3.PoolManager()
filterwarnings(action="ignore")
lock = threading.Lock()

a = ['10.10.34.35','10.10.34.36','10.10.34.34']
c = open(r"C:\Users\test\Documents\IP.txt", 'r')
writer = open(r"C:\Users\test\Documents\IPnahaee1.txt", "a")
writer1 = open(r"C:\Users\test\Documents\IPnadarad.txt", "a")
q = []
for line in c:
        #print(p,line)
        n = line.split('\n')
        #print(n[0])

        #urljadid = "http://" + n[0]



        try:
            myResolver = dns.resolver.Resolver()   #dnsresolve
            myAnswers = myResolver.query(n[0])
            host_ip = socket.gethostbyname(n[0])
            if host_ip not in a:

                    writer.writelines(n[0] + ":" + host_ip)
                    writer.write('\n')
                    print(n[0] + ":" + host_ip)


        except Exception as e:
            writer1.writelines(n[0])
            writer1.write('\n')
            print(e)


