import socket
import json
import sys
if(len(sys.argv) < 4):
    print("Usage:\n"
          "\tsearch-server.py <ip> <port> <data file path>")
    exit(0)

host = sys.argv[1]
port = int(sys.argv[2])
data_file_path = sys.argv[3]

#Load the data
data_file = open(data_file_path)
epics = json.load(data_file)

#Setup the network listener
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

def response_echo(input):
    return input.upper()

def response_find_data(input):
    ret_val = "Not Found"
    key = input.lower()
    if(key == '*'):
        ret_val = "\n".join(epics.keys())
    elif(key == '+'):
        #get all the characters
        char_list = ",".join(epics.values())
        ret_val = "\n".join([x.lstrip() for x in char_list.split(',')])
    elif(key in epics):
        ret_val = epics[key]
        
    return ret_val

while(True):
    #Wait till someone connects
    conn, addr = serv.accept()
    #Now someone has connected
    from_client = ''
    while True:
        #Read the request from the client
        data = conn.recv(4096)
        if not data: break
        from_client += data
        print from_client
        #conn.send( response_echo (from_client) )
        conn.send( response_find_data (from_client) )
    conn.close()
    print 'client disconnected'

