from pathlib import Path

from core.queue_manager import QueueManager
from core.worker import Worker


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_queue_worker():

    queue = QueueManager()


    input_file = (
        PROJECT_ROOT
        / "assets"
        / "test"
        / "sample.jpg"
    )


    output_file = (
        PROJECT_ROOT
        / "assets"
        / "test"
        / "output"
        / "queue_test.webp"
    )


    job = {
        "input": str(input_file),
        "output": str(output_file),
        "format": "WEBP",
        "quality": 80
    }


    queue.add_job(job)


    assert queue.size() == 1


    worker = Worker()


    result = worker.process(
        queue.get_job()
    )


    assert len(
        result["success"]
    ) == 1