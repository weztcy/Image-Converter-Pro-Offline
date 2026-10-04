"""
Report Summary Calculator
"""


class ReportSummary:


    def calculate(
        self,
        history
    ):

        total_files = len(
            history
        )


        total_before = 0

        total_after = 0

        success = 0

        failed = 0



        for row in history:


            total_before += (
                row[4]
                or
                0
            )


            total_after += (
                row[5]
                or
                0
            )


            if row[6] == "success":

                success += 1

            else:

                failed += 1



        saved = 0


        if total_before > 0:

            saved = (
                (
                    total_before
                    -
                    total_after
                )
                /
                total_before
            ) * 100



        return {

            "total_files": total_files,

            "before": total_before,

            "after": total_after,

            "saved_percent": round(
                saved,
                2
            ),

            "success": success,

            "failed": failed

        }