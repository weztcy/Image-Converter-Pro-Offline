"""
Queue Runner

Automatically execute queued jobs.
"""


import threading
import time


from .worker import Worker



class QueueRunner:


    def __init__(
        self,
        queue,
        interval=1
    ):

        self.queue = queue

        self.interval = interval

        self.running = False

        self.thread = None

        self.worker = Worker()



    def start(self):

        if self.running:

            return


        self.running = True


        self.thread = threading.Thread(
            target=self.run,
            daemon=True
        )


        self.thread.start()



    def stop(self):

        self.running = False



    def run(self):

        while self.running:


            if self.queue.size() > 0:


                job = self.queue.get_job()


                self.worker.process(
                    job
                )


            else:

                time.sleep(
                    self.interval
                )