"""
Main Content Area
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QStackedWidget,
    QSizePolicy
)


from ui.pages.dashboard_page import DashboardPage
from ui.pages.converter_page import ConverterPage
from ui.pages.settings_page import SettingsPage




class ContentArea(QWidget):


    def __init__(
        self
    ):

        super().__init__()


        self.setup_ui()



    def setup_ui(
        self
    ):


        self.setObjectName(
            "ContentArea"
        )



        layout = QVBoxLayout()


        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        layout.setSpacing(
            0
        )



        self.stack = QStackedWidget()



        self.stack.setSizePolicy(

            QSizePolicy.Expanding,

            QSizePolicy.Expanding

        )



        # ==============================
        # Pages
        # ==============================

        self.dashboard_page = DashboardPage()


        self.converter_page = ConverterPage()


        self.settings_page = SettingsPage()



        # ==============================
        # Register Pages
        # ==============================

        self.stack.addWidget(

            self.dashboard_page

        )


        self.stack.addWidget(

            self.converter_page

        )


        self.stack.addWidget(

            self.settings_page

        )



        layout.addWidget(

            self.stack

        )



        self.setLayout(

            layout

        )



        self.show_dashboard()



    # ==============================
    # Navigation
    # ==============================

    def show_dashboard(
        self
    ):


        self.stack.setCurrentWidget(

            self.dashboard_page

        )



    def show_converter(
        self
    ):


        self.stack.setCurrentWidget(

            self.converter_page

        )



    def show_settings(
        self
    ):


        self.stack.setCurrentWidget(

            self.settings_page

        )