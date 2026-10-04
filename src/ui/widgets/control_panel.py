"""
Premium Conversion Control Panel
"""


from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QComboBox,
    QSlider,
    QCheckBox,
    QPushButton,
    QSpinBox,
    QHBoxLayout
)


from PySide6.QtCore import (
    Qt,
    Signal
)


from formats.encoder_manager import EncoderManager




class ControlPanel(QFrame):


    convert_clicked = Signal(dict)



    def __init__(
        self
    ):

        super().__init__()


        self.encoder_manager = EncoderManager()


        self.setup_ui()



    def setup_ui(
        self
    ):


        self.setObjectName(
            "ControlPanel"
        )


        layout = QVBoxLayout()


        layout.setSpacing(
            12
        )



        # ==============================
        # Title
        # ==============================

        title = QLabel(
            "Conversion Settings"
        )


        title.setObjectName(
            "SectionTitle"
        )


        layout.addWidget(
            title
        )



        # ==============================
        # Format
        # ==============================

        layout.addWidget(
            QLabel(
                "Output Format"
            )
        )


        self.format_box = QComboBox()


        self.load_formats()


        layout.addWidget(
            self.format_box
        )



        # ==============================
        # Quality
        # ==============================

        layout.addWidget(
            QLabel(
                "Quality"
            )
        )


        self.quality_slider = QSlider(
            Qt.Horizontal
        )


        self.quality_slider.setRange(
            1,
            100
        )


        self.quality_slider.setValue(
            85
        )


        self.quality_value = QLabel(
            "85%"
        )


        self.quality_value.setAlignment(
            Qt.AlignRight
        )


        layout.addWidget(
            self.quality_slider
        )


        layout.addWidget(
            self.quality_value
        )


        self.quality_slider.valueChanged.connect(
            self.update_quality_label
        )



        # ==============================
        # Resize
        # ==============================

        self.resize_option = QCheckBox(
            "Resize"
        )


        layout.addWidget(
            self.resize_option
        )



        resize_layout = QHBoxLayout()



        self.width_input = QSpinBox()


        self.width_input.setRange(
            1,
            10000
        )


        self.width_input.setValue(
            1920
        )


        self.width_input.setSuffix(
            " px"
        )



        self.height_input = QSpinBox()


        self.height_input.setRange(
            1,
            10000
        )


        self.height_input.setValue(
            1080
        )


        self.height_input.setSuffix(
            " px"
        )



        resize_layout.addWidget(
            QLabel(
                "Width"
            )
        )


        resize_layout.addWidget(
            self.width_input
        )


        resize_layout.addWidget(
            QLabel(
                "Height"
            )
        )


        resize_layout.addWidget(
            self.height_input
        )


        layout.addLayout(
            resize_layout
        )



        self.keep_ratio = QCheckBox(
            "Keep Aspect Ratio"
        )


        self.keep_ratio.setChecked(
            True
        )


        layout.addWidget(
            self.keep_ratio
        )



        # ==============================
        # Other Options
        # ==============================


        self.auto_optimize = QCheckBox(
            "Auto Optimize"
        )


        self.watermark_option = QCheckBox(
            "Watermark"
        )


        self.background_option = QCheckBox(
            "Remove Background"
        )



        layout.addWidget(
            self.auto_optimize
        )


        layout.addWidget(
            self.watermark_option
        )


        layout.addWidget(
            self.background_option
        )



        # ==============================
        # Convert Button
        # ==============================

        self.convert_button = QPushButton(
            "Convert"
        )


        layout.addWidget(
            self.convert_button
        )



        self.setLayout(
            layout
        )



        self.convert_button.clicked.connect(
            self.emit_settings
        )



    # ==============================
    # Load Formats
    # ==============================

    def load_formats(
        self
    ):


        formats = (

            self.encoder_manager

            .get_supported_formats()

        )


        self.format_box.addItems(
            formats
        )



    # ==============================
    # Quality Label
    # ==============================

    def update_quality_label(
        self,
        value
    ):


        self.quality_value.setText(

            f"{value}%"

        )



    # ==============================
    # Emit Settings
    # ==============================

    def emit_settings(
        self
    ):


        settings = {


            "format":

                self.format_box.currentText(),



            "quality":

                self.quality_slider.value(),



            "resize":

                self.resize_option.isChecked(),



            "width":

                self.width_input.value(),



            "height":

                self.height_input.value(),



            "keep_ratio":

                self.keep_ratio.isChecked(),



            "auto_optimize":

                self.auto_optimize.isChecked(),



            "watermark":

                self.watermark_option.isChecked(),



            "remove_background":

                self.background_option.isChecked()

        }



        self.convert_clicked.emit(
            settings
        )