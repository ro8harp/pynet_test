#!/usr/bin/env python

import telnetlib
import time

TELNET_PORT = 23
TELNET_TIMEOUT = 6

def main():
#    print "Hello"
    ip_addr = '184.105.247.70'
    username = 'pyclass'
    password = '88newclass'

    remote_conn = telnetlib.Telnet(ip_addr, TELNET_PORT, TELNET_TIMEOUT)
    output = remote_conn.read_until("sername:", TELNET_TIMEOUT)
    remote_conn.write(username + '\n')
    output = remote_conn.read_until("ssword:", TELNET_TIMEOUT)
    remote_conn.write(password + '\n')
    
    time.sleep(1)
    output = remote_conn.read_very_eager()
    
    remote_conn.write("terminal length 0" + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()

    remote_conn.write("show version" + '\n')
    time.sleep(1)
    output = remote_conn.read_very_eager()
    print output
    
    
    remote_conn.close()

if __name__ == "__main__":
    main()
