"""
Queue Manager

Manage conversion jobs.
"""


from queue import Queue


class QueueManager:

    def __init__(self):

        self.queue = Queue()


    def add_job(self, job):

        self.queue.put(job)


    def get_job(self):

        if self.queue.empty():
            return None

        return self.queue.get()


    def size(self):

        return self.queue.qsize()


    def clear(self):

        while not self.queue.empty():

            self.queue.get()