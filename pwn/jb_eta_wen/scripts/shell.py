#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys, socket, pty

ADDR = ("0.0.0.0", 9999)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(ADDR)
sock.listen(5)

def recv_until(f, delim="\n"):
    buf = ""
    while not buf.endswith(delim):
        buf += f.read(1)
    return buf

while True:
    client, addr = sock.accept()

    if os.fork() == 0:
        sock.close()
        try:
            token = open("/tmp/.token", "r").read().strip()
        except Exception as e:
            client.sendall("Host-Guest synchronization failed.\n")
            client.sendall("Please report this to admin.\n")
            client.close()
            sys.exit(127)
        
        client.sendall("Gimme the token: ")
        f = client.makefile("rw", 0)
        user_input = recv_until(f).strip().replace("\r", "")
        if user_input == token:
            os.dup2(client.fileno(), 0)
            os.dup2(client.fileno(), 1)
            os.dup2(client.fileno(), 2)
            pty.spawn("/bin/bash")
        else:
            print user_input.encode("hex"), token.encode("hex")
            client.sendall("Invalid token.\n")
        sys.exit(127)
    client.close()
    
