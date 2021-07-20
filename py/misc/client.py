import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port on the server given by the caller
host = sys.argv[1]
port = int(sys.argv[2])
message = sys.argv[3]

server_address = (host, port)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    print >>sys.stderr, 'sending "%s"' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(128)
        amount_received += len(data)
        print >>sys.stderr, 'received "%s"' % data

finally:
    sock.close()
