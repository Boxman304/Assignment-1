#AbedEl-Rahman Itani
#202001300
import socket
import time

user = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
serveraddress = ('LocalHost', 42069)

RTT =[0]*5
n=0

while n<=4:
    info = input("To send to server: ")
    start_time = time.time()
    user.sendto(info.encode('utf-8'),serveraddress)
    data = user.recvfrom(4096)
    print("Recieved from server: ", data[0].decode('utf-8'))
    end_time=time.time()
    RTTi=(end_time-start_time)
    RTT[n]=RTTi 
    print("RTT= ",round(RTTi,6)*10**6," microseconds")
    n+=1

Mean=(RTT[0]+RTT[1]+RTT[2]+RTT[3]+RTT[4])/5
print("The average Round Trip Time is: ", Mean*10**6 , "microseconds")
user.close()