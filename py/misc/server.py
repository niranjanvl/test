import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address given on the command line
server_address = ('127.0.0.1', 10000)
sock.bind(server_address)
print >>sys.stderr, 'starting up on %s port %s' % sock.getsockname()
sock.listen(1)

epics = {
         "ramayana" : "Rama, Sita, Bharata, Lakshmana, Shatrugna, Hanuma",
         "mahabharata" : "Krishna, Pandavas, Kauravas, Bhishma, ...",
         "bhagavatam" : "Devaki, Vasudeva, Krishna, Balarama, Kamsa, Gadendra, ..."
        }

while True:
    print >>sys.stderr, 'waiting for a connection'
    connection, client_address = sock.accept()
    try:
        print >>sys.stderr, 'client connected:', client_address
        while True:
            data = connection.recv(128)
            print >>sys.stderr, 'received "%s"' % data
            if (data):
                resp = data.lower()
                if((len(resp) > 0) and (resp in epics)):
                    resp = epics[resp]
                else:
                    resp = "Not Available"
                print >>sys.stderr, 'sent "%s"' % resp
                connection.sendall(resp)
            else:
                break
    finally:
        connection.close()
