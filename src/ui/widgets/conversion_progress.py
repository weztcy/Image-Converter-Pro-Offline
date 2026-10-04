"""
Premium Conversion Progress Widget

Display conversion progress and status.
"""


from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QLabel,
    QProgressBar
)




class ConversionProgress(QFrame):


    def __init__(
        self
    ):

        super().__init__()


        self.setup_ui()



    def setup_ui(
        self
    ):


        self.setObjectName(
            "ConversionProgress"
        )


        layout = QVBoxLayout()


        layout.setSpacing(
            8
        )



        # ==============================
        # Status Label
        # ==============================

        self.status = QLabel(
            "Ready to convert"
        )


        self.status.setObjectName(
            "ProgressStatus"
        )



        # ==============================
        # Progress Bar
        # ==============================

        self.progress = QProgressBar()


        self.progress.setRange(
            0,
            100
        )


        self.progress.setValue(
            0
        )


        self.progress.setTextVisible(
            True
        )


        self.progress.setFormat(
            "%p%"
        )



        layout.addWidget(
            self.status
        )


        layout.addWidget(
            self.progress
        )


        self.setLayout(
            layout
        )



    # ==============================
    # Update Progress
    # ==============================

    def update_progress(
        self,
        value
    ):


        self.progress.setValue(
            value
        )


        self.status.setText(
            f"Processing {value}%"
        )



    # ==============================
    # Completed
    # ==============================

    def completed(
        self,
        path
    ):


        self.progress.setValue(
            100
        )


        self.status.setText(
            f"Completed: {path}"
        )



    # ==============================
    # Reset
    # ==============================

    def reset(
        self
    ):


        self.progress.setValue(
            0
        )


        self.status.setText(
            "Ready to convert"
        )



    # ==============================
    # Custom Status
    # ==============================

    def set_status(
        self,
        text
    ):


        self.status.setText(
            text
        )