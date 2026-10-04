"""
History Repository
"""


from .models import CREATE_HISTORY_TABLE




class HistoryRepository:


    def __init__(
        self,
        database
    ):


        self.db = database

        self.create_table()



    # ==================================
    # Create Table
    # ==================================

    def create_table(
        self
    ):


        self.db.execute(

            CREATE_HISTORY_TABLE

        )



    # ==================================
    # Insert History
    # ==================================

    def add(
        self,
        data
    ):


        query = """

        INSERT INTO conversion_history

        (
            input_file,
            output_file,
            format,
            size_before,
            size_after,
            status
        )

        VALUES (?,?,?,?,?,?)

        """



        self.db.execute(

            query,

            (

                data["input_file"],

                data["output_file"],

                data["format"],

                data["size_before"],

                data["size_after"],

                data["status"]

            )

        )



    # ==================================
    # All History
    # ==================================

    def get_all(
        self
    ):


        cursor = self.db.execute(

            """

            SELECT *

            FROM conversion_history

            ORDER BY id DESC

            """

        )


        return cursor.fetchall()



    # ==================================
    # Recent History
    # ==================================

    def get_recent(
        self,
        limit=5
    ):


        cursor = self.db.execute(

            """

            SELECT *

            FROM conversion_history

            ORDER BY id DESC

            LIMIT ?

            """,

            (

                limit,

            )

        )


        return cursor.fetchall()



    # ==================================
    # Dashboard Statistics
    # ==================================

    def get_statistics(
        self
    ):


        cursor = self.db.execute(

            """

            SELECT

                COUNT(*),

                SUM(

                    size_before - size_after

                )

            FROM conversion_history

            WHERE status = 'success'

            """

        )



        result = cursor.fetchone()



        files_processed = (

            result[0]

            or

            0

        )



        saved_bytes = (

            result[1]

            or

            0

        )



        # Jangan tampilkan negatif

        if saved_bytes < 0:

            saved_bytes = 0



        return {


            "files_processed":

                files_processed,



            "saved_bytes":

                saved_bytes

        }