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
        #data = c.recv(1024)
        p = 2
        q =7
        n = p *q
        phi = (p-1)*(q-1)
        e=5
        # c = int(c.recv(1024))
        # e = int(c.recv(1024))
        c = int(c.recv(1024))
        print "Encrypted data = " + str(c)


        k=2
        d=(1+(k*phi))/e
        # msg = 2
        # c = msg**e
        m = c**d
        c = c%n
        m = m%n
        print "\nBob: " + str(e) + str(n)
        print "Original Message sent= "+str(m)


        serverMessage = raw_input("\nAlice(to quit press q): ")
        if serverMessage == 'q':
            break
        #while serverMessage != 'q':
        #c.send(serverMessage)

    c.close()
if __name__ == '__main__':
    Main()
