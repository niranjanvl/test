import socket
import sys
if(len(sys.argv) < 4):
    print("Usage:\n"
          "\tsearch-client.py <host> <port> <serarch term>")
    exit(0)

host = sys.argv[1]
port = int(sys.argv[2])
search_term = sys.argv[3]

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))
client.send(search_term)
from_server = client.recv(4096)
client.close()
print from_server

