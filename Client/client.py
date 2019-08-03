import time, socket, sys

print("Welcome to Chat Room!")
print("Initialising...")
time.sleep(1)

a = socket.socket()
ahost = socket.gethostname()
address = socket.gethostbyname(ahost)
print(ahost, "(", address,")")
host = input(str("Enter server address: "))
name = input(str("Enter your name: "))
port= 1234
print(" Trying to connect to ", host, "(", port,")") 
time.sleep(1)
a.connect((host,port))
print("Connected...")

a.send(name.encode())
a_name = a.recv(1024)
a_name = a_name.decode()
print(a_name, "joined the chat\Enter [e] to exit")

while True: 
    message = a.recv(1024)
    message = message.decode()
    print(a_name, ":", message)
    message = input(str("Me : "))
    if message == "[e]": 
        message = "Left chat room!"
        a.send(message.encode())
        print("")
        break
    a.send(message.encode())

