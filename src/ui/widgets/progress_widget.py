"""
Progress Widget
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar
)


class ProgressWidget(QWidget):

    def __init__(self):

        super().__init__()

        self.setup_ui()


    def setup_ui(self):

        layout = QVBoxLayout()


        self.status_label = QLabel(
            "Waiting..."
        )


        self.progress = QProgressBar()


        self.progress.setValue(
            0
        )


        layout.addWidget(
            self.status_label
        )


        layout.addWidget(
            self.progress
        )


        self.setLayout(
            layout
        )


    def update_progress(
        self,
        current,
        total
    ):

        percentage = int(
            (current / total) * 100
        )


        self.progress.setValue(
            percentage
        )


        self.status_label.setText(
            f"Processing {current}/{total}"
        )