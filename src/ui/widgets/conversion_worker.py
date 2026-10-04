"""
Conversion Background Worker

Handle single and multiple image conversion.
"""


from PySide6.QtCore import (
    QThread,
    Signal
)


from core.batch_processor import BatchProcessor




class ConversionWorker(QThread):


    progress = Signal(
        int
    )


    finished = Signal(
        dict
    )


    failed = Signal(
        str
    )



    def __init__(
        self,
        files,
        output,
        output_format
    ):

        super().__init__()


        self.files = files

        self.output = output

        self.output_format = output_format



    def run(
        self
    ):


        try:


            if not self.files:


                self.failed.emit(

                    "No files selected"

                )

                return



            processor = BatchProcessor()



            total = len(
                self.files
            )


            completed = 0



            for file in self.files:


                processor.process_files(

                    [
                        file
                    ],

                    self.output,

                    self.output_format

                )


                completed += 1



                progress_value = int(

                    (

                        completed

                        /

                        total

                    )

                    *

                    100

                )



                self.progress.emit(

                    progress_value

                )



            self.finished.emit(

                processor.results

            )



        except Exception as error:


            self.failed.emit(

                str(error)

            )