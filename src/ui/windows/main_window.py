"""
Main Application Window
"""


from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QSizePolicy
)


from ui.widgets.sidebar import Sidebar
from ui.widgets.content_area import ContentArea




class MainWindow(QMainWindow):


    def __init__(
        self
    ):

        super().__init__()


        self.setup_ui()



    def setup_ui(
        self
    ):


        self.setWindowTitle(
            "Image Converter Pro Offline"
        )


        self.resize(
            1200,
            750
        )


        self.setMinimumSize(
            900,
            600
        )



        container = QWidget()



        layout = QHBoxLayout()


        layout.setContentsMargins(
            0,
            0,
            0,
            0
        )


        layout.setSpacing(
            0
        )



        # ==============================
        # Sidebar
        # ==============================

        self.sidebar = Sidebar()


        self.sidebar.setSizePolicy(

            QSizePolicy.Fixed,

            QSizePolicy.Expanding

        )



        # ==============================
        # Content
        # ==============================

        self.content = ContentArea()


        self.content.setSizePolicy(

            QSizePolicy.Expanding,

            QSizePolicy.Expanding

        )



        layout.addWidget(
            self.sidebar
        )


        layout.addWidget(
            self.content
        )



        container.setLayout(
            layout
        )


        self.setCentralWidget(
            container
        )



        self.connect_navigation()


        self.connect_dashboard_actions()



    # ==============================
    # Sidebar Navigation
    # ==============================

    def connect_navigation(
        self
    ):


        self.sidebar.dashboard_clicked.connect(

            self.content.show_dashboard

        )


        self.sidebar.converter_clicked.connect(

            self.content.show_converter

        )


        self.sidebar.settings_clicked.connect(

            self.content.show_settings

        )



    # ==============================
    # Dashboard Actions
    # ==============================

    def connect_dashboard_actions(
        self
    ):


        dashboard = (

            self.content.dashboard_page

        )


        dashboard.convert_clicked.connect(

            self.content.show_converter

        )