#AbedEl-Rahman Itani
#202001300
import socket
import datetime 

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serveraddress=('LocalHost',42069)
server.bind(serveraddress)
print("The Server is running on: ", serveraddress)

while True:
    Message = server.recvfrom(4096)
    if Message:
        print("The recieved message from client: ", Message[0].decode('utf-8'))
        print(datetime.datetime.now())
        server.sendto(Message[0],Message[1])
server.close()
