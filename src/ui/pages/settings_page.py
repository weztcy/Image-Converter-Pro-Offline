"""
Settings Page
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QSpinBox,
    QPushButton
)


from utils.settings_manager import SettingsManager




class SettingsPage(QWidget):


    def __init__(
        self
    ):

        super().__init__()


        self.manager = SettingsManager()


        self.setup_ui()



    def setup_ui(
        self
    ):


        layout = QVBoxLayout()



        title = QLabel(
            "Application Settings"
        )



        self.format_box = QComboBox()


        self.format_box.addItems(
            [
                "JPG",
                "PNG",
                "WEBP",
                "AVIF",
                "TIFF",
                "ICO",
                "SVG",
            ]
        )



        self.quality_box = QSpinBox()


        self.quality_box.setRange(
            1,
            100
        )



        self.webp_mode = QComboBox()


        self.webp_mode.addItems(
            [
                "lossy",
                "lossless"
            ]
        )



        self.save_button = QPushButton(
            "Save Settings"
        )



        layout.addWidget(
            title
        )



        layout.addWidget(
            QLabel(
                "Default Format"
            )
        )


        layout.addWidget(
            self.format_box
        )



        layout.addWidget(
            QLabel(
                "WEBP Mode"
            )
        )


        layout.addWidget(
            self.webp_mode
        )



        layout.addWidget(
            QLabel(
                "WEBP Quality"
            )
        )


        layout.addWidget(
            self.quality_box
        )



        layout.addWidget(
            self.save_button
        )



        self.setLayout(
            layout
        )



        self.load_settings()



        self.save_button.clicked.connect(
            self.save_settings
        )



    def load_settings(
        self
    ):


        format_value = self.manager.get(
            "default_format"
        )



        index = self.format_box.findText(
            format_value
        )


        if index >= 0:


            self.format_box.setCurrentIndex(
                index
            )



        self.webp_mode.setCurrentText(
            self.manager.get(
                "webp_mode"
            )
        )



        self.quality_box.setValue(
            self.manager.get(
                "webp_quality"
            )
        )



    def save_settings(
        self
    ):


        self.manager.set(
            "default_format",
            self.format_box.currentText()
        )



        self.manager.set(
            "webp_mode",
            self.webp_mode.currentText()
        )



        self.manager.set(
            "webp_quality",
            self.quality_box.value()
        )