import socket
# Socket Class
class Socket:
    def __init__(self, input_port):
        self.port = input_port
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(None)
        self.s.bind(('', self.port))
        self.s.listen(5000)

    def accept_socket(self):
        conn, addr = self.s.accept()
        conn.settimeout(None)
        print 'Server start, connected by ', addr

global socket_server
socket_server = Socket(8002)
print 'Socket Defined'

# for send
#socket_server.conn.send("Current Position = ({:f}, {:f})".format(Px, Py))

# for receive
socket_server.accept_socket()
info = socket_server.conn.recv(1024)
print 'info from Socket: ', info
