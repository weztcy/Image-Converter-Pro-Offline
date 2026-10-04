from pathlib import Path

from core.history_manager import HistoryManager



def test_history_manager():


    manager = HistoryManager()


    manager.record(
        "input.jpg",
        "output.webp",
        "WEBP"
    )


    manager.close()


    assert True