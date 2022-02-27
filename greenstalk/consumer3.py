import greenstalk

class BeanStalk:
    def __init__(self, host, port, encoding='utf-8', use='default', watch='default'):
        self.conn = greenstalk.Client(host=host, port=port, encoding=encoding, use=use, watch=watch)

    def producer(self, body, priority=65536, delay=0, ttr=60, tube='default'):
        self.use(tube)
        return self.conn.put(body, priority, delay, ttr)

    def consumer(self, timeout=None):
        return self.conn.reserve(timeout)

    def use(self, tube='default'):
        self.conn.use(tube)

    def delete(self, job):
        self.conn.delete(job)

    def relase(self, job, priority=65536, delay=0):
        self.conn.release(job, priority, delay)

    def bury(self, job, priority=65536):
        self.conn.bury(job, priority)

    def kick(self, bound):
        return self.conn.kick(bound)

    def kick_job(self, job):
        self.conn.kick_job(job)

    def touch(self, job):
        self.conn.touch(job)

    def watch(self, tube):
        return self.conn.watch(tube)

    def ignore(self, tube):
        return self.conn.ignore(tube)

    def peek(self, jobid):
        return self.conn.peek(jobid)

    def peek_ready(self):
        return self.conn.peek_ready()

    def peek_delayed(self):
        return self.conn.peek_delayed()

    def peek_buried(self):
        return self.conn.peek_buried()

    def stats_job(self, job):
        return self.conn.stats_job(job)

    def stats_tube(self, tube):
        return self.conn.stats_tube(tube)

    def stats(self):
        return self.conn.stats()

    def tubes(self):
        return self.conn.tubes()

    def using(self):
        return self.conn.using()

    def watching(self):
        return self.conn.watching()

    def pause_tube(self, tube, delay):
        self.conn.pause_tube(tube, delay)



deck = BeanStalk('localhost', 11300, 'utf-8', 'default', 'default')
deck()
