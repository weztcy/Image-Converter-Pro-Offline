"""
Base Card Widget

Reusable card container.
"""


from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout
)




class BaseCard(QFrame):


    def __init__(
        self,
        parent=None
    ):

        super().__init__(
            parent
        )


        self.layout = QVBoxLayout()


        self.setLayout(
            self.layout
        )


        self.setObjectName(
            "BaseCard"
        )



    def add_widget(
        self,
        widget
    ):


        self.layout.addWidget(
            widget
        )