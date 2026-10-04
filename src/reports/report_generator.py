"""
Report Generator
"""


from .csv_report import CSVReport
from .pdf_report import PDFReport



class ReportGenerator:


    def __init__(self):

        self.csv = CSVReport()

        self.pdf = PDFReport()



    def export_csv(
        self,
        history,
        output
    ):

        self.csv.export(
            history,
            output
        )



    def export_pdf(
        self,
        history,
        output
    ):

        self.pdf.export(
            history,
            output
        )