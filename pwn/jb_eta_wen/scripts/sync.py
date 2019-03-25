#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os, sys, socket

ADDR = ("0.0.0.0", 2689)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(ADDR)
sock.listen(5)

client, addr = sock.accept()

token = client.recv(32)

open("/tmp/.token", "w").write(token)

client.close()
sock.close()

