import socket

def Main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket()  #create a socket
    s.connect((host, port)) #try to connect to server


    message = raw_input("\nBob: ")
    while message != 'q':
        s.send(message)
        data = s.recv(1024)
        print '\nAlice: ' + str(data)
        message = raw_input("\nBob: ")
    s.close()

if __name__ == '__main__':
    Main()
