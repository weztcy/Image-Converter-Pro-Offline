"""
Premium Image Preview Panel
"""


from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel
)


from PySide6.QtGui import (
    QPixmap
)


from PySide6.QtCore import (
    Qt
)


from pathlib import Path


from PIL import Image




class PreviewPanel(QFrame):


    def __init__(
        self
    ):

        super().__init__()


        self.current_image = None


        self.setup_ui()



    def setup_ui(
        self
    ):


        self.setObjectName(
            "PreviewPanel"
        )


        layout = QVBoxLayout()



        self.image_label = QLabel(
            "Preview Image"
        )


        self.image_label.setAlignment(
            Qt.AlignCenter
        )
        
        self.image_label.setMinimumSize(
            400,
            300
        )


        self.image_label.setObjectName(
            "ImagePreview"
        )


        self.image_label.setAlignment(
            Qt.AlignCenter
        )


        self.image_label.setMinimumHeight(
            250
        )



        self.info_label = QLabel(
            "No image selected"
        )


        self.info_label.setAlignment(
            Qt.AlignCenter
        )



        layout.addWidget(
            self.image_label
        )


        layout.addWidget(
            self.info_label
        )



        self.setLayout(
            layout
        )



    def load_image(
        self,
        path
    ):


        self.current_image = path



        pixmap = QPixmap(
            path
        )


        if not pixmap.isNull():


            self.image_label.setPixmap(

                pixmap.scaled(

                    400,

                    300,

                    Qt.KeepAspectRatio,

                    Qt.SmoothTransformation

                )

            )



        self.update_information(
            path
        )



    def update_information(
        self,
        path
    ):


        try:

            image = Image.open(
                path
            )


            width, height = (
                image.size
            )


            mode = image.mode



            filename = (
                Path(path)
                .name
            )



            self.info_label.setText(

                f"{filename}\n"
                f"{width} x {height}\n"
                f"Mode: {mode}"

            )



        except Exception:


            self.info_label.setText(
                "Unable to read image information"
            )