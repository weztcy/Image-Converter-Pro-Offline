"""
Database Connection

SQLite handler.
"""


import sqlite3

from pathlib import Path



DATABASE_FILE = (

    Path.home()

    /

    ".image_converter_history.db"

)



class Database:


    def __init__(self):

        self.connection = sqlite3.connect(
            DATABASE_FILE
        )


    def execute(
        self,
        query,
        params=()
    ):

        cursor = self.connection.cursor()


        cursor.execute(
            query,
            params
        )


        self.connection.commit()


        return cursor



    def close(self):

        self.connection.close()