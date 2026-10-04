"""
Premium Converter Page

Single + Multiple + Folder conversion workflow UI.
"""


from pathlib import Path


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QPushButton,
    QFileDialog,
    QHBoxLayout,
    QListWidget
)


from ..widgets.drop_area import DropArea
from ..widgets.preview_panel import PreviewPanel
from ..widgets.control_panel import ControlPanel
from ..widgets.conversion_progress import ConversionProgress


from ..workers.conversion_worker import ConversionWorker

from pathlib import Path


class ConverterPage(QWidget):


    def __init__(self):

        super().__init__()


        self.files = []

        self.output_folder = None

        self.worker = None


        self.setup_ui()



    def setup_ui(self):


        root_layout = QVBoxLayout()


        root_layout.setContentsMargins(
            0,
            0,
            0,
            0
        )



        scroll = QScrollArea()


        scroll.setWidgetResizable(
            True
        )


        scroll.setFrameShape(
            QScrollArea.NoFrame
        )



        container = QWidget()


        layout = QVBoxLayout()


        layout.setSpacing(
            18
        )


        layout.setContentsMargins(
            20,
            20,
            20,
            20
        )



        # INPUT BUTTONS

        input_layout = QHBoxLayout()


        self.select_file_button = QPushButton(
            "Select Image"
        )


        self.select_files_button = QPushButton(
            "Select Multiple Images"
        )


        self.select_folder_button = QPushButton(
            "Select Folder"
        )



        input_layout.addWidget(
            self.select_file_button
        )


        input_layout.addWidget(
            self.select_files_button
        )


        input_layout.addWidget(
            self.select_folder_button
        )


        layout.addLayout(
            input_layout
        )



        # DROP AREA

        self.drop_area = DropArea()


        self.drop_area.setMinimumHeight(
            120
        )


        layout.addWidget(
            self.drop_area
        )



        # QUEUE

        layout.addWidget(
            QLabel(
                "Selected Files"
            )
        )


        self.file_list = QListWidget()


        self.file_list.setMinimumHeight(
            120
        )


        layout.addWidget(
            self.file_list
        )



        queue_buttons = QHBoxLayout()


        self.remove_button = QPushButton(
            "Remove Selected"
        )


        self.clear_button = QPushButton(
            "Clear All"
        )


        queue_buttons.addWidget(
            self.remove_button
        )


        queue_buttons.addWidget(
            self.clear_button
        )


        layout.addLayout(
            queue_buttons
        )

        # ======================
        # Output Folder
        # ======================


        layout.addWidget(
            QLabel(
                "Output Folder"
            )
        )


        output_layout = QHBoxLayout()



        self.output_label = QLabel(
            "Default: converted_output"
        )


        self.output_button = QPushButton(
            "Select Output Folder"
        )



        output_layout.addWidget(
            self.output_label
        )


        output_layout.addWidget(
            self.output_button
        )



        layout.addLayout(
            output_layout
        )

        # PREVIEW

        self.preview_panel = PreviewPanel()


        self.preview_panel.setMinimumHeight(
            220
        )


        layout.addWidget(
            self.preview_panel
        )



        # CONTROL

        self.control_panel = ControlPanel()


        layout.addWidget(
            self.control_panel
        )



        # PROGRESS

        self.progress_widget = ConversionProgress()


        layout.addWidget(
            self.progress_widget
        )



        # STATUS

        self.status_label = QLabel(
            "Ready to convert"
        )


        self.status_label.setObjectName(
            "StatusLabel"
        )


        layout.addWidget(
            self.status_label
        )



        container.setLayout(
            layout
        )


        scroll.setWidget(
            container
        )


        root_layout.addWidget(
            scroll
        )


        self.setLayout(
            root_layout
        )



        # SIGNALS

        self.select_file_button.clicked.connect(
            self.select_single_file
        )


        self.select_files_button.clicked.connect(
            self.select_multiple_files
        )


        self.select_folder_button.clicked.connect(
            self.select_folder
        )


        self.drop_area.file_selected.connect(
            self.load_drop_file
        )


        self.remove_button.clicked.connect(
            self.remove_selected_file
        )


        self.clear_button.clicked.connect(
            self.clear_files
        )


        self.control_panel.convert_clicked.connect(
            self.start_conversion
        )
        
        self.output_button.clicked.connect(
            self.select_output_folder
        )


    def select_single_file(self):


        file, _ = QFileDialog.getOpenFileName(

            self,

            "Select Image",

            "",

            "Images (*.jpg *.jpeg *.png *.webp *.avif *.tiff *.gif *.ico)"

        )


        if file:

            self.set_files(
                [
                    Path(file)
                ]
            )



    def select_multiple_files(self):


        files, _ = QFileDialog.getOpenFileNames(

            self,

            "Select Images",

            "",

            "Images (*.jpg *.jpeg *.png *.webp *.avif *.tiff *.gif *.ico)"

        )


        if files:

            self.set_files(

                [
                    Path(file)
                    for file in files
                ]

            )



    def select_folder(self):


        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Folder"

        )


        if folder:


            extensions = {

                ".jpg",
                ".jpeg",
                ".png",
                ".webp",
                ".avif",
                ".tiff",
                ".gif",
                ".ico"

            }


            files = [

                file

                for file in Path(folder).iterdir()

                if file.suffix.lower() in extensions

            ]


            self.set_files(
                files
            )



    def load_drop_file(
        self,
        path
    ):


        self.set_files(
            [
                Path(path)
            ]
        )



    def set_files(
        self,
        files
    ):


        self.files = list(files)


        self.file_list.clear()



        for file in self.files:

            self.file_list.addItem(
                str(file)
            )



        if self.files:

            self.preview_panel.load_image(

                str(self.files[0])

            )



        self.status_label.setText(

            f"{len(self.files)} file(s) selected"

        )



    def remove_selected_file(self):


        row = self.file_list.currentRow()


        if row >= 0:

            self.files.pop(
                row
            )


            self.set_files(
                self.files
            )



    def clear_files(self):


        self.files.clear()


        self.file_list.clear()


        self.status_label.setText(
            "No files selected"
        )

    def select_output_folder(
        self
    ):


        folder = QFileDialog.getExistingDirectory(

            self,

            "Select Output Folder"

        )


        if folder:


            self.output_folder = Path(
                folder
            )


            self.output_label.setText(

                str(self.output_folder)

            )

    def start_conversion(
        self,
        settings
    ):


        if not self.files:

            self.status_label.setText(
                "Please select image first"
            )

            return



        self.control_panel.convert_button.setEnabled(
            False
        )


        self.progress_widget.reset()



        if self.output_folder:


            output_folder = self.output_folder


        else:


            output_folder = (

                self.files[0].parent

                /

                "converted_output"

            )


        output_folder.mkdir(
            exist_ok=True
        )



        self.worker = ConversionWorker(

            self.files,

            output_folder,

            settings["format"]

        )


        self.worker.progress.connect(

            self.progress_widget.update_progress

        )


        self.worker.finished.connect(

            self.conversion_finished

        )


        self.worker.start()



    def conversion_finished(
        self,
        result
    ):


        self.control_panel.convert_button.setEnabled(
            True
        )


        self.progress_widget.completed(
            str(result)
        )


        self.status_label.setText(
            "Conversion completed"
        )



    def conversion_failed(
        self,
        error
    ):


        self.control_panel.convert_button.setEnabled(
            True
        )


        self.status_label.setText(
            f"Error: {error}"
        )