

import threading
import time
import logging

import my_fsm
import my_util

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                   )


g_running = True
class thread_worker(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.id = id
        
    def run(self):
        global g_running
        print('thread_worker g_running = '+str(g_running))
        while g_running:
            time.sleep(1)
            print('thread_worker g_running = '+str(g_running))
        
class thread_heartbeat(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.id = id
        
    def run(self):
        global g_running
        
        fsm_worker = Fsm_Worker()
        while g_running:
        
            fsm_worker.next(False)
            
            my_util.doJob(None)
            
            g_running = False
            print('thread_heartbeat g_running = '+str(g_running))
        
        
if __name__ == "__main__":

    try:
        logging.debug('starting slave')
        threads = []

        t_worker = thread_worker()
        threads.append(t_worker)
        t_worker.start()
        
        t_heartbeat = thread_heartbeat()
        threads.append(t_heartbeat)
        t_heartbeat.start()
        
    except:
        logging.debug('except')
    finally:
        logging.debug('done')

    
    