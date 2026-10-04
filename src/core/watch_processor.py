"""
Watch Processor

Convert detected files into queue jobs.
"""


from pathlib import Path



class WatchProcessor:


    def __init__(
        self,
        queue,
        output_folder,
        output_format="WEBP",
        settings=None
    ):

        self.queue = queue

        self.output_folder = Path(
            output_folder
        )

        self.output_format = output_format

        self.settings = settings or {}



    def add_file(
        self,
        file_path
    ):

        file_path = Path(
            file_path
        )


        output_file = (
            self.output_folder
            /
            f"{file_path.stem}.{self.output_format.lower()}"
        )


        job = {

            "input": str(file_path),

            "output": str(output_file),

            "format": self.output_format,

            "settings": self.settings.copy()

        }


        self.queue.add_job(
            job
        )


        return job