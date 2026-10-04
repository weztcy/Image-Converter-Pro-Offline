"""
Premium Conversion Worker

Run single and multiple conversions
in background thread.
"""


from pathlib import Path


from PySide6.QtCore import (
    QThread,
    Signal
)


from core.image_loader import ImageLoader
from core.converter import ImageConverter




class ConversionWorker(QThread):


    progress = Signal(
        int
    )


    finished = Signal(
        str
    )


    failed = Signal(
        str
    )



    def __init__(
        self,
        files,
        output_folder,
        output_format,
        settings=None
    ):

        super().__init__()


        if isinstance(
            files,
            (str, Path)
        ):

            files = [
                files
            ]



        self.files = [

            Path(file)

            for file in files

        ]


        self.output_folder = Path(
            output_folder
        )


        self.output_format = output_format


        self.settings = settings or {}



    def run(
        self
    ):


        try:


            total = len(
                self.files
            )


            completed = 0



            self.output_folder.mkdir(
                exist_ok=True
            )



            for file in self.files:



                # Load image

                image = ImageLoader(
                    str(file)
                ).load()



                converter = ImageConverter(

                    image,

                    str(file)

                )



                output = (

                    self.output_folder

                    /

                    f"{file.stem}.{self.output_format.lower()}"

                )



                converter.convert(

                    str(output),

                    self.output_format,

                    self.settings

                )



                completed += 1



                percentage = int(

                    completed

                    /

                    total

                    *

                    100

                )



                self.progress.emit(

                    percentage

                )



            self.finished.emit(

                str(self.output_folder)

            )



        except Exception as error:


            self.failed.emit(

                str(error)

            )