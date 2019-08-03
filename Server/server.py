import time, socket, sys

print("Welcome to Chat Room")
print("Initialising....")
time.sleep(1)

a = socket.socket()
host = socket.gethostname()
address = socket.gethostbyname(host)
port = 1234
a.bind((host, port))
print(host, "(", address, ")\n")
name = input(str("Enter your name: "))
           
a.listen(1)
print("Waiting for incoming connections..")
conn, address = a.accept()
print("Received connection from ", address[0], "(", address[1], ")")

a_name = conn.recv(1024)
a_name = a_name.decode()
print(a_name, "has connected to the chat room. Enter [e] to exit chat room")
conn.send(name.encode())

while True:
    message = input(str("Me : "))
    if message == "[e]":
        message = "Left chat room!"
        conn.send(message.encode())
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(a_name, ":", message)
