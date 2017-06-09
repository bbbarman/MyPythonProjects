import socket
"""
To test Python socket programming
"""
s = socket.socket()
host = socket.gethostname()
port = 1234
s.connect((host, port))
print s.recv(1024)
