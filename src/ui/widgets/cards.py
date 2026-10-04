"""
Dashboard Card Component
"""


from PySide6.QtWidgets import QLabel


from .base import BaseCard




class InfoCard(BaseCard):


    def __init__(
        self,
        title,
        value,
        subtitle=""
    ):

        super().__init__()


        self.setup_ui(
            title,
            value,
            subtitle
        )



    def setup_ui(
        self,
        title,
        value,
        subtitle
    ):


        self.title_label = QLabel(
            title
        )


        self.value_label = QLabel(
            value
        )


        self.subtitle_label = QLabel(
            subtitle
        )



        self.title_label.setObjectName(
            "CardTitle"
        )


        self.value_label.setObjectName(
            "CardValue"
        )


        self.subtitle_label.setObjectName(
            "CardSubtitle"
        )



        self.layout.addWidget(
            self.title_label
        )


        self.layout.addWidget(
            self.value_label
        )


        if subtitle:


            self.layout.addWidget(
                self.subtitle_label
            )



        self.setObjectName(
            "InfoCard"
        )


        self.setFixedHeight(
            130
        )



    # ==================================
    # Update Value
    # ==================================

    def set_value(
        self,
        value
    ):


        self.value_label.setText(

            str(value)

        )



    # ==================================
    # Update Subtitle
    # ==================================

    def set_subtitle(
        self,
        text
    ):


        self.subtitle_label.setText(

            str(text)

        )