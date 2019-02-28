import socket

def gcd(a, h):
    while(1):
        temp=a%h
        if (temp==0):
            return h
        a = h
        h = temp

def Main():
    host = '127.0.0.1'
    port = 12345

    s = socket.socket()  #create a socket
    s.connect((host, port)) #try to connect to server


    message = raw_input("\nBob(to quit press q): ")
    while message != 'q':
        p = 2
        q =7
        n = p *q
        phi = (p-1)*(q-1)
        e = 2
        while(e < phi):
            count = gcd(e, phi)
            if (count ==1 ):
                break
            else:
                e = e + 1
        #s.send(message)
        msg =2
        c = msg**e
        s.send(str(c))
        print "Encrypted message sent to Alice: " + str(c)+"\n"
        #s.send(str(e))
        #ce = []
        #ce.append(c)
        #ce.append(e)
        #s.send(str(c))
        #s.send(str(e))

        # data = s.recv(1024)
        # print '\nAlice: ' + str(data)
        message = raw_input("\nBob: ")
    s.close()

if __name__ == '__main__':
    Main()
