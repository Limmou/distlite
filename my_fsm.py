

def if_else(condition, a, b):
    if condition : return a
    else : return b

class Fsm_Worker():

    def __init__(self):
        self.cur_state = 'nojob'
        self.transfer = {
            'lazy':lambda x: if_else(x,'nojob', 'lazy'),
            'nojob':lambda x: if_else(x,'findjob', 'lazy'),
            'findjob':lambda x: 'runjob',
            'runjob':lambda x: 'lazy'
        }
    
    def next(self,condition):
        self.cur_state = self.transfer[self.cur_state](condition)
        return self.cur_state
        
        
class Fsm_Timer():

    def __init__(self):
        self.cur_state = 'heartbeat'
        self.transfer = {
            'lazy':lambda x: if_else(x,'heartbeat', 'lazy'),
            'heartbeat':lambda x: if_else(x,'heartbeat', 'quit'),
            'quit':lambda x: 'quit'
        }
    
    def next(self,condition):
        
        self.cur_state = self.transfer[self.cur_state](condition)
        return self.cur_state

            
            
class Fsm_Master_Job():

    def __init__(self):
        self.cur_state = 'lazy'
        self.transfer = {
            'lazy':lambda x: if_else(x,'searchjob', 'lazy'),
            'searchjob':lambda x: if_else(x,'findjob', 'lazy'),
            'findjob':lambda x: 'findslave',
            'findslave':lambda x: if_else(x,'pushjob', 'noslave'),
            'noslave':lambda x: 'lazy',
        }
    
    def next(self,condition):
        
        self.cur_state = self.transfer[self.cur_state](condition)
        return self.cur_state

        
class Fsm_Manager():

    def __init__(self, job_fsm, ):
        self.cur_state = 'lazy'
        self.mangaer_transfer = {
            'lazy':lambda x: 'lazy',
            'getJob':lambda x: if_else(x,'cmd', 'lazy'),
            'sendJob':lambda x: 'lazy',
            'quit':lambda x: 'quit'
        }
    
    def next(self,condition):
        
        self.cur_state = self.transfer[self.cur_state](condition)
        return self.cur_state
        

if __name__ == "__main__":

    fsm_worker = Fsm_Worker()
    print fsm_worker.next(False)
    print fsm_worker.next(True)
    print fsm_worker.next(True)
    print fsm_worker.next(True)
    
    fsm_timer = Fsm_Timer()
    print fsm_timer.next(True)
    print fsm_timer.next(False)
    
    fsm_master_job = Fsm_Master_Job()
    
    fsm_manager = Fsm_Manager(fsm_master_job)
    print fsm_manager.next(True)
    print fsm_manager.next(False)
    
    
    

