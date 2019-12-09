#!/usr/bin/env python2

# Multicast Sender 
# -----------------


import socket
import struct
import sys

# do not forget setup multicast routing such as
# sudo route add -net 239.0.0.0 netmask 255.255.255.0 dev eth0.77
# then it will start working :-)
# Explanation: mcast route instruct OS to use 
# IGMP on interface for MCAST addresses.


message = 'very important data'
multicast_group = ('239.0.0.2', 10000)

# Create the datagram socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set a timeout so the socket does not block indefinitely when trying
# to receive data.
sock.settimeout(0.2)


# Set the time-to-live for messages to 1 so they do not go past the
# local network segment.
ttl = struct.pack('b', 1)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

try:

    # Send data to the multicast group
    print >>sys.stderr, 'sending "%s"' % message
    sent = sock.sendto(message, multicast_group)

    # Look for responses from all recipients
    while True:
        print >>sys.stderr, 'waiting to receive'
        try:
            data, server = sock.recvfrom(16)
        except socket.timeout:
            print >>sys.stderr, 'timed out, no more responses'
            break
        else:
            print >>sys.stderr, 'received "%s" from %s' % (data, server)

finally:
    print >>sys.stderr, 'closing socket'
    sock.close()

# --- end ---

