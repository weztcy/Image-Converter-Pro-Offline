"""
PDF Report Generator
"""


from pathlib import Path


from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)


from reportlab.lib.styles import getSampleStyleSheet



from .summary import ReportSummary



class PDFReport:


    def __init__(self):

        self.summary = ReportSummary()



    def export(
        self,
        history,
        output_file
    ):


        output_file = Path(
            output_file
        )


        document = SimpleDocTemplate(
            str(output_file)
        )


        styles = getSampleStyleSheet()


        content = []


        summary = self.summary.calculate(
            history
        )


        content.append(
            Paragraph(
                "Image Converter Report",
                styles["Title"]
            )
        )


        content.append(
            Spacer(
                1,
                20
            )
        )


        lines = [

            f"Total Files: {summary['total_files']}",

            f"Before: {summary['before']} bytes",

            f"After: {summary['after']} bytes",

            f"Saved: {summary['saved_percent']}%",

            f"Success: {summary['success']}",

            f"Failed: {summary['failed']}"

        ]



        for line in lines:

            content.append(
                Paragraph(
                    line,
                    styles["Normal"]
                )
            )


            content.append(
                Spacer(
                    1,
                    8
                )
            )



        document.build(
            content
        )