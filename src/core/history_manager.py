"""
History Manager

Handle conversion history recording.
"""


from pathlib import Path


from database.database import Database
from database.history_repository import HistoryRepository




class HistoryManager:


    def __init__(self):


        self.database = Database()


        self.repository = HistoryRepository(

            self.database

        )



    # ==================================
    # Record Conversion
    # ==================================

    def record(
        self,
        input_file,
        output_file,
        output_format,
        status="success"
    ):


        input_path = Path(
            input_file
        )


        output_path = Path(
            output_file
        )



        size_before = 0

        size_after = 0



        if input_path.exists():

            size_before = (

                input_path.stat()

                .st_size

            )



        if output_path.exists():

            size_after = (

                output_path.stat()

                .st_size

            )



        self.repository.add(

            {

                "input_file":
                    str(input_path),


                "output_file":
                    str(output_path),


                "format":
                    output_format,


                "size_before":
                    size_before,


                "size_after":
                    size_after,


                "status":
                    status

            }

        )



    # ==================================
    # Dashboard Statistics
    # ==================================

    def get_statistics(
        self
    ):


        return (

            self.repository

            .get_statistics()

        )



    # ==================================
    # Recent Activity
    # ==================================

    def get_recent_history(
        self,
        limit=5
    ):


        return (

            self.repository

            .get_recent(

                limit

            )

        )



    # ==================================
    # Close Database
    # ==================================

    def close(
        self
    ):


        self.database.close()