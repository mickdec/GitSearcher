import requests
from netaddr import *
import urllib3
import os
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

ips = IPNetwork('50.0.0.0/8')
for ip in ips:
    try:
        print(ip)
        req = requests.get("http://"+str(ip)+'/.git', timeout=.1)
        print(req.status_code)
        if req.status_code == 200:
            if "gitlab" in req.text and "Explore" in req.text:
                f = open("RESULT","a+")
                f.write("GITLAB >> http://"+str(ip)+"/.git/\n")
                f.close()
            if "Index of /.git" in req.text:
                f = open("RESULT","a+")
                f.write(".git >> http://"+str(ip)+"/.git/\n")
                f.close()
                # try:
                #     os.system("githacker --url http://"+str(ip)+"/.git/ --output "+str(ip))
                # except:
                #     print("",end="")
                
    except:
        print("",end="")
