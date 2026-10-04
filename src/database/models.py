"""
Database Models
"""


CREATE_HISTORY_TABLE = """

CREATE TABLE IF NOT EXISTS conversion_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    input_file TEXT,

    output_file TEXT,

    format TEXT,

    size_before INTEGER,

    size_after INTEGER,

    status TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)

"""