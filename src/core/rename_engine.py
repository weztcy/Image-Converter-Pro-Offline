"""
Rename Engine

Handle output filename generation.
"""

from datetime import datetime

from pathlib import Path



class RenameEngine:


    def generate(
        self,
        original_file,
        extension,
        template="{name}"
        ,
        number=None
    ):

        original_file = Path(
            original_file
        )


        name = original_file.stem


        date = datetime.now().strftime(
            "%Y%m%d"
        )


        filename = template


        filename = filename.replace(
            "{name}",
            name
        )


        filename = filename.replace(
            "{date}",
            date
        )


        filename = filename.replace(
            "{format}",
            extension.replace(
                ".",
                ""
            )
        )


        if number is not None:

            filename = filename.replace(
                "{number}",
                f"{number:03d}"
            )


        return (
            filename
            +
            "."
            +
            extension.replace(
                ".",
                ""
            )
        )