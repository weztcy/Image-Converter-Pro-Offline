"""
Sidebar Widget
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton
)


from PySide6.QtCore import Signal




class Sidebar(QWidget):


    dashboard_clicked = Signal()

    converter_clicked = Signal()

    settings_clicked = Signal()



    def __init__(
        self
    ):

        super().__init__()

        self.setup_ui()



    def setup_ui(
        self
    ):


        self.setObjectName(
            "Sidebar"
        )


        layout = QVBoxLayout()


        layout.setSpacing(
            10
        )


        layout.setContentsMargins(
            15,
            15,
            15,
            15
        )



        # ==============================
        # Buttons
        # ==============================


        self.dashboard_button = QPushButton(
            "Dashboard"
        )


        self.converter_button = QPushButton(
            "Converter"
        )


        self.settings_button = QPushButton(
            "Settings"
        )



        buttons = [

            self.dashboard_button,

            self.converter_button,

            self.settings_button

        ]



        for button in buttons:


            button.setMinimumHeight(
                42
            )


            layout.addWidget(
                button
            )



        layout.addStretch()



        self.setLayout(
            layout
        )



        self.setMinimumWidth(
            180
        )


        self.setMaximumWidth(
            240
        )



        self.connect_events()



    def connect_events(
        self
    ):


        self.dashboard_button.clicked.connect(

            self.dashboard_clicked.emit

        )


        self.converter_button.clicked.connect(

            self.converter_clicked.emit

        )


        self.settings_button.clicked.connect(

            self.settings_clicked.emit

        )