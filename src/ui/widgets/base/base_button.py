"""
Base Button Widget

Reusable application button.
"""


from PySide6.QtWidgets import QPushButton




class BaseButton(QPushButton):


    def __init__(
        self,
        text="",
        parent=None
    ):

        super().__init__(
            text,
            parent
        )


        self.setup_ui()



    def setup_ui(
        self
    ):


        self.setObjectName(
            "BaseButton"
        )