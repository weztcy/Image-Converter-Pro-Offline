from pathlib import Path

from reports.report_generator import ReportGenerator



def test_csv_report(tmp_path):


    history = [

        (
            1,
            "input.jpg",
            "output.webp",
            "WEBP",
            1000,
            200,
            "success",
            "2026-10-04"
        )

    ]


    output = (
        tmp_path
        /
        "report.csv"
    )


    generator = ReportGenerator()


    generator.export_csv(
        history,
        output
    )


    assert output.exists()



def test_pdf_report(tmp_path):


    history = [

        (
            1,
            "input.jpg",
            "output.webp",
            "WEBP",
            1000,
            200,
            "success",
            "2026-10-04"
        )

    ]


    output = (
        tmp_path
        /
        "report.pdf"
    )


    generator = ReportGenerator()


    generator.export_pdf(
        history,
        output
    )


    assert output.exists()