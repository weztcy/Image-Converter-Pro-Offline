from database.database import Database
from database.history_repository import HistoryRepository



def test_history_database():


    db = Database()


    repository = HistoryRepository(
        db
    )


    repository.add(
        {
            "input_file": "input.jpg",

            "output_file": "output.webp",

            "format": "WEBP",

            "size_before": 1000,

            "size_after": 200,

            "status": "success"
        }
    )


    history = repository.get_all()


    assert len(history) >= 1


    db.close()