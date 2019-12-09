#!/usr/bin/env python2

# Multicast Receiver
# -------------------

import socket
import struct
import sys

# do not forget setup multicast routing such as
# sudo route add -net 239.0.0.0 netmask 255.255.255.0 dev eth0.77
# then it will start working :-)
# Explanation: mcast route instruct OS to use
# IGMP on interface for MCAST addresses.


multicast_group = '239.0.0.2'
server_address = ('', 10000)

# Create the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to the server address
sock.bind(server_address)



# Tell the operating system to add the socket to the multicast group
# on all interfaces.
group = socket.inet_aton(multicast_group)
mreq = struct.pack('4sL', group, socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)



# Receive/respond loop
while True:
    print >>sys.stderr, '\nwaiting to receive message'
    data, address = sock.recvfrom(1024)
    
    print >>sys.stderr, 'received %s bytes from %s' % (len(data), address)
    print >>sys.stderr, data

    print >>sys.stderr, 'sending acknowledgement to', address
    sock.sendto('ack', address)

# --- end ---

