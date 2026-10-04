"""
Theme Manager

Handle application themes.
"""


from pathlib import Path



class ThemeManager:


    def __init__(
        self
    ):

        self.theme_path = (
            Path(__file__).parent
            /
            "style.qss"
        )



    def load_theme(
        self
    ):

        if not self.theme_path.exists():

            return ""



        with open(
            self.theme_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()



    def apply(
        self,
        app
    ):

        stylesheet = self.load_theme()


        app.setStyleSheet(
            stylesheet
        )