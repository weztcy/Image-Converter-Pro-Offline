from reports.summary import ReportSummary



def test_report_summary():


    history = [

        (
            1,
            "a.jpg",
            "a.webp",
            "WEBP",
            1000,
            200,
            "success",
            "date"
        ),

        (
            2,
            "b.jpg",
            "b.webp",
            "WEBP",
            500,
            100,
            "success",
            "date"
        )

    ]


    summary = ReportSummary().calculate(
        history
    )


    assert summary["total_files"] == 2

    assert summary["before"] == 1500

    assert summary["after"] == 300

    assert summary["saved_percent"] == 80

    assert summary["success"] == 2