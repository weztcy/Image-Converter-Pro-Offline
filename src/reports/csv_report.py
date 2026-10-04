"""
CSV Report Generator
"""


import csv



class CSVReport:


    def export(
        self,
        history,
        output_file
    ):


        with open(
            output_file,
            "w",
            newline="",
            encoding="utf-8"
        ) as file:


            writer = csv.writer(
                file
            )


            writer.writerow(
                [
                    "ID",
                    "Input",
                    "Output",
                    "Format",
                    "Before",
                    "After",
                    "Status",
                    "Created"
                ]
            )


            for row in history:

                writer.writerow(
                    row
                )