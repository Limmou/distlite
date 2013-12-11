#!/usr/bin/env python

import socket  
import time
import sys
import json



class MyClient():
    
    def __init__(self, timeout=1, bufsize = 1024):
        self.timeout = timeout
        self.bufsize = bufsize
        self.conn = None
    
    def send(self, host, port, data):
        
        #connect
        try:
            addr = (host,port)
            self.conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.conn.connect(addr)
        except:
            return {'code':False,'msg':'connect failed','recv':''}
        
        #send
        try:
            self.conn.send(data)
        except:
            self.conn.close()
            return {'code':False,'msg':'send failed','recv':''}
        
        #recv
        try:
            revcdata = self.conn.recv(self.bufsize)
        except:
            return {'code':False,'msg':'recv failed','recv':''}
        finally:
            self.conn.close()
                    
        return {'code':True,'msg':'ok','recv':revcdata}
 

if __name__ == '__main__':
    cli = MyClient()
    
    
    data = {'cmd':'sendHeartbeat'}
    print cli.send('127.0.0.1',6000,json.dumps(data))
    
    data = {'cmd':'getSlaves'}
    a = cli.send('127.0.0.1',6000,json.dumps(data))
    
    
    """
    data_addjob = {'cmd':'addJob','job':'hi'}
    print cli.send('127.0.0.1',6000,json.dumps(data_addjob))
    
    data_addjob = {'cmd':'addJob','job':'hi2'}
    print cli.send('127.0.0.1',6000,json.dumps(data_addjob))

    data_getjob = {'cmd':'getJob'}
    print cli.send('127.0.0.1',6000,json.dumps(data_getjob))
    
    data_getjob = {'cmd':'getJob'}
    print cli.send('127.0.0.1',6000,json.dumps(data_getjob))
    """
    data_quit = {'cmd':'quit'}
    print cli.send('127.0.0.1',6000,json.dumps(data_quit))
    