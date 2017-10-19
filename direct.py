import sys
import socket
import select
import struct
import time


print("\n***AUDIO-SIFTER DIRECT***\n")

ip = 'localhost'
port = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
#s.connect((ip, port))
s.listen(1)

def helloworld(errorNum, errorType):
    header = 'HTTP/1.1 %d %s \r\nContent-Type: text/html\n' % (errorNum, errorType)
    body = '<html>\r\n\t<head>\r\n\t\t<title>Docker-App\r\n\t\t</title>\r\n\t</head>\r\n\r\n<body>\r\n\t<p><b>AUDIO-SIFTER</p></b>\r\n</body>\r\n</html>'
    #payload = "<form action='/action_page.php'><input type='file' name='pic' accept='image/*'><input type='submit'></form>"
    msg = header + body + '\r\n\r\n'
    return msg

print('AUDIO-SIFTER is listening on %s:%d' % (ip, port))

while 1:
    (clientsocket, address) = s.accept()
    toSend = helloworld(200, 'OK')
    clientsocket.send(toSend.encode())
    clientsocket.shutdown(1)
    clientsocket.close()
