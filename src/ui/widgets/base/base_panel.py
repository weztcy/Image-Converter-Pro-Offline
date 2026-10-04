"""
Base Panel Widget

Reusable large content container.
"""


from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout
)




class BasePanel(QFrame):


    def __init__(
        self,
        parent=None
    ):

        super().__init__(
            parent
        )


        self.setup_ui()



    def setup_ui(
        self
    ):


        self.layout = QVBoxLayout()


        self.setLayout(
            self.layout
        )


        self.setObjectName(
            "BasePanel"
        )



    def add_widget(
        self,
        widget
    ):


        self.layout.addWidget(
            widget
        )