from pathlib import Path

from core.queue_manager import QueueManager
from core.watch_processor import WatchProcessor



def test_watch_processor():


    queue = QueueManager()


    processor = WatchProcessor(
        queue,
        "output",
        "WEBP",
        {
            "quality":80
        }
    )


    job = processor.add_file(
        "photo.jpg"
    )


    assert queue.size() == 1


    assert job["format"] == "WEBP"