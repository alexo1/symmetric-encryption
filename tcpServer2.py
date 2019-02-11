import socket

def Main():
    host = "127.0.0.1"  #host is this machine
    port = 12345

    s = socket.socket()  # create a new socket object
    s.bind((host, port)) # bind a socket to a new port

    s.listen(1) # tell server to start listening for one  connection at a time
    c , addr = s.accept() # accept conection that is trying to connect
    print "Connection from: " + str(addr)
    # while True:
    #     data = c.recv(1024)
    #     if not data:
    #         break
    #     print "from connected user: " + str(data)
    #     data = str(data).upper()
    #     print "sending: " + str(data)
    #     c.send(data)
    while True:
        data = c.recv(1024)
        print "\nBob: " + str(data)

        serverMessage = raw_input("\nAlice: ")
        if serverMessage == 'q':
            break
        #while serverMessage != 'q':
        c.send(serverMessage)

    c.close()
if __name__ == '__main__':
    Main()
