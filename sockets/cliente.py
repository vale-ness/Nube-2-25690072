import socket
c = socket.socket()
c.connect(("10.10.192.58", 5001))
while True: 
    dato = input("Mensaje: ")
    c.send(dato.encode())
    if dato == "salir":
        break
    print(c.recv(1024).decode())
