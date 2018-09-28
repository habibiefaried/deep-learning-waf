#!/usr/bin/python
from TheServer import TheServer

listen_port = 9090
buffer_size = 8192
forward_to  = ('192.168.234.133', 80)

if __name__ == '__main__':
        server = TheServer('', listen_port, buffer_size, forward_to)
        print "Listening on port "+str(listen_port)
        try:
            server.main_loop()
        except KeyboardInterrupt:
            print "Ctrl C - Stopping server"
            sys.exit(1)
