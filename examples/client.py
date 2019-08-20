import socket
import sys
import binascii
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8090)
print >>sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)
login_message = "78 78 0D 01 01 23 45 67 89 01 23 45 00 01 8C DD 0D 0A".replace(' ', '').decode('hex')
sock.send(login_message)
time.sleep(3)

try:

    # login packet
    # location packet
    # location_message = "78781F120B081D112E10CC027AC7EB0C46584900148F01CC00287D001FB8000380810D0A".replace(' ', '').decode('hex')
    # sock.send(location_message)
    # time.sleep(3)

    # alarm packet
    print "Sending alarm packet"
    alarm_message = "78 78 25 16 0B 0B 0F 0E 24 1D CF 02 7A C8 87 0C 46 57 E6 00 14 02 09 01 CC 00 28 7D 00 1F 72 65 06 04 01 01 00 36 56 A4 0D 0A".replace(' ', '').decode('hex')
    sock.sendall(alarm_message)
    time.sleep(3)

    # heartbit packet
    heartbit_message = "78 78 0A 13 4B 04 03 00 01 00 11 06 1F 0D 0A".replace(' ', '').decode('hex')
    sock.send(heartbit_message)
    amount_received = 0

    data = sock.recv(16)
    received_string = binascii.hexlify(data)
    amount_received = len(data)
    print 'amount_received', amount_received
    print 'received_string', received_string

finally:
    print 'closing socket'
    sock.close()

