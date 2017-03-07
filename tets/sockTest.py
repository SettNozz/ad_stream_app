#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import cv2
import msgpack

sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('0.0.0.0', 8080))
sock.setblocking(False)
sock.listen(1)
fileName = 'newImage.jpg'

def maybeNewImage():
    try:
        conn, addr = sock.accept()
    except:
        return None, None, None, None
    conn.setblocking(True)
    data = conn.recv(200000)
    unpackData = msgpack.unpackb(data)
    newFile = open(fileName, 'w')
    newFile.write(unpackData['Image'])
    newFile.close()
    imgRet = cv2.imread(fileName)
    dataTime = unpackData['Time']
    x = unpackData['x']
    y = unpackData['y']
    conn.close()
    print('HAHAHA')
    print(type(imgRet))
    print(type(x))
    print(type(y))
    return(imgRet, dataTime, x, y)
