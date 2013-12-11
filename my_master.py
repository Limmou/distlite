

import threading
import time
import logging
import json
import uuid

import my_globals
import my_fsm
import my_server

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                   )
                   
joblock = threading.Lock()


def sync(lock):
    def syncWithLock(fn):
        def newFn(*args,**kwargs):
            lock.acquire()
            try:
                return fn(*args,**kwargs)
            finally:
                lock.release()
        newFn.func_name = fn.func_name
        newFn.__doc__ = fn.__doc__
        return newFn
    return syncWithLock

class thread_dispatcher(threading.Thread):
    """
        
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.id = id
        
    def run(self):
        print('thread_dispatcher g_running = '+str(my_globals.g_running))
        while my_globals.g_running:
            time.sleep(1)
            print('thread_dispatcher g_running = '+str(my_globals.g_running))
        
        
        
class thread_manager(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.id = id
        
        
    
    def manager_handler(self, socket, address):

        try:
            raw_x = socket.recv(1024)
        except:
            ret = {'code':False,'msg':'handler failed : recv data'}
            socket.send(json.dumps(ret))
          
        if not raw_x:
            ret = {'code':False,'msg':'handler failed : empty package'}
            socket.send(json.dumps(ret))

        x = json.loads(raw_x)
        ret = {'code':True,'msg':'ok : cmd ['+x['cmd']+']'}
        
        if 'addJob' == x['cmd']:
        
            jobId = self.addJob(x['job'])
            ret = {'code':True,'msg':'ok ', 'jobId':jobId}
            
        elif 'getJob' == x['cmd']:
            
            job = self.getJob(x['slaveId'])
            ret = {'code':True,'msg':'ok ', 'job':job}
            
        elif 'getSlaves' == x['cmd']:
        
            slaves = self.getSlaves()
            ret = {'code':True,'msg':'ok ', 'slaves':slaves}
            
        elif 'sendHeartbeat' == x['cmd']:
            
            if x.has_key('slaveId'):
                slaveId = x['slaveId']
            else:
                slaveId = self.addSlave(address)
                
            ret = {'code':True,'msg':'ok ', 'slaveId':slaveId}
            
        elif 'quit' == x['cmd']:
        
            my_globals.g_running = False
            print x
        else:
            ret = {'code':False,'msg':'handler failed : unknown cmd ['+raw_x+']'}
        
        
        socket.send(json.dumps(ret))
        
        
    def addJob(self, job):
        
        jobId = str(uuid.uuid4())
        my_globals.g_job[jobId] = job
        
        return jobId
    
    
    def addSlave(self, address):
        
        slaveId = str(uuid.uuid4())
        my_globals.g_slave[slaveId] = {}
        my_globals.g_slave[slaveId]['slaveId'] = slaveId
        my_globals.g_slave[slaveId]['ip'] = address[0]
        my_globals.g_slave[slaveId]['port'] = address[1]
        
        return slaveId
    
    
    # get a job and work it out 
    @sync(joblock)
    def getJob(self, slave, do = False):
        pass
    
    
    # get all jobs without doing
    def getJobs(self):
        return my_globals.g_job
        
        
    # get all slaves
    def getSlaves(self):
        return my_globals.g_slave

            
    # get one slave
    def getSlave(self, slaveId):
        if my_globals.g_slave.has_key(slaveId):
            return my_globals.g_slave[slaveId]
        else:
            return {}
        
        
    def run(self):

        #handler RPC request
        srv = my_server.MyServer(self.manager_handler)
        srv.listen('0.0.0.0',6000)
            
        print 'thread_manager quit '
        
        
class thread_cmd(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.id = id
        
    def run(self):
        print('thread_cmd g_running = '+str(my_globals.g_running))
        time.sleep(10)
        my_globals.g_running = False
        print('thread_cmd g_running = '+str(my_globals.g_running))
        
        
if __name__ == "__main__":

    try:
        logging.debug('starting master')
        threads = []

        t_manager = thread_manager()
        threads.append(t_manager)
        t_manager.start()
        
        """
        t_dispatcher = thread_dispatcher()
        threads.append(t_dispatcher)
        t_dispatcher.start()
        """
        
    except:
        logging.debug('except')
    finally:
        logging.debug('done')

    
    