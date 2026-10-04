import time

from core.queue_manager import QueueManager
from core.queue_runner import QueueRunner



def test_queue_runner():


    queue = QueueManager()


    runner = QueueRunner(
        queue
    )


    runner.start()


    assert runner.running is True


    runner.stop()


    assert runner.running is False