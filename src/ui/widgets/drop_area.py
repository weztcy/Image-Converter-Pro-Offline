"""
Premium Drag & Drop Image Area
"""


from pathlib import Path


from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QFileDialog
)


from PySide6.QtCore import (
    Qt,
    Signal
)



class DropArea(QFrame):


    file_selected = Signal(str)



    def __init__(
        self
    ):

        super().__init__()


        self.setAcceptDrops(
            True
        )


        self.setup_ui()



    def setup_ui(
        self
    ):


        layout = QVBoxLayout()


        self.label = QLabel(
            "Drag & Drop Image\n\nor Click to Select"
        )


        self.label.setAlignment(
            Qt.AlignCenter
        )


        layout.addWidget(
            self.label
        )


        self.setLayout(
            layout
        )


        self.setObjectName(
            "DropArea"
        )



        self.setMinimumHeight(
            180
        )



    def mousePressEvent(
        self,
        event
    ):


        file, _ = QFileDialog.getOpenFileName(
            self,
            "Select Image",
            "",
            "Images (*.jpg *.jpeg *.png *.webp *.heic *.heif)"
        )


        if file:

            self.file_selected.emit(
                file
            )



    def dragEnterEvent(
        self,
        event
    ):


        if event.mimeData().hasUrls():

            event.acceptProposedAction()



    def dropEvent(
        self,
        event
    ):


        urls = event.mimeData().urls()


        if urls:

            path = urls[0].toLocalFile()


            if Path(path).exists():

                self.file_selected.emit(
                    path
                )