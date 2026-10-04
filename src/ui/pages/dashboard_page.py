"""
Dashboard Page

Main application dashboard.
"""


from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QListWidget
)


from PySide6.QtCore import (
    Qt,
    Signal
)


from ..widgets.cards import InfoCard
from ..widgets.base import BasePanel, BaseButton


from core.history_manager import HistoryManager
from core.queue_manager import QueueManager




class DashboardPage(QWidget):


    convert_clicked = Signal()



    def __init__(
        self
    ):

        super().__init__()


        self.history_manager = HistoryManager()

        self.queue_manager = QueueManager()


        self.setup_ui()



    def setup_ui(
        self
    ):


        main_layout = QVBoxLayout()


        main_layout.setSpacing(
            18
        )


        main_layout.setContentsMargins(
            20,
            20,
            20,
            20
        )



        # ==============================
        # Header
        # ==============================

        header_panel = BasePanel()


        title = QLabel(
            "Image Converter Pro Offline"
        )


        title.setObjectName(
            "DashboardTitle"
        )


        title.setAlignment(
            Qt.AlignCenter
        )


        header_panel.add_widget(
            title
        )


        main_layout.addWidget(
            header_panel
        )



        # ==============================
        # Quick Action
        # ==============================

        action_panel = BasePanel()


        action_layout = QHBoxLayout()


        action_layout.setSpacing(
            12
        )


        convert_button = BaseButton(
            "Convert Image"
        )


        action_layout.addWidget(
            convert_button
        )


        action_panel.layout.addLayout(
            action_layout
        )


        main_layout.addWidget(
            action_panel
        )



        convert_button.clicked.connect(
            self.convert_clicked.emit
        )



        # ==============================
        # Statistics
        # ==============================

        stats = self.load_statistics()



        stats_panel = BasePanel()


        stats_layout = QHBoxLayout()


        stats_layout.setSpacing(
            16
        )



        self.files_card = InfoCard(
            "Files Processed",
            str(
                stats["files_processed"]
            )
        )


        self.saved_card = InfoCard(
            "Saved Space",
            self.format_bytes(
                stats["saved_bytes"]
            )
        )


        self.jobs_card = InfoCard(
            "Current Jobs",
            str(
                stats["current_jobs"]
            )
        )



        stats_layout.addWidget(
            self.files_card
        )


        stats_layout.addWidget(
            self.saved_card
        )


        stats_layout.addWidget(
            self.jobs_card
        )


        stats_panel.layout.addLayout(
            stats_layout
        )


        main_layout.addWidget(
            stats_panel
        )



        # ==============================
        # Recent Activity
        # ==============================

        activity_panel = BasePanel()


        activity_title = QLabel(
            "Recent Activity"
        )


        activity_title.setObjectName(
            "SectionTitle"
        )


        self.activity_list = QListWidget()


        self.load_recent_activity()



        activity_panel.layout.addWidget(
            activity_title
        )


        activity_panel.layout.addWidget(
            self.activity_list
        )


        main_layout.addWidget(
            activity_panel
        )



        self.setLayout(
            main_layout
        )



    # ==================================
    # Load Statistics
    # ==================================

    def load_statistics(
        self
    ):


        try:

            history = (

                self.history_manager

                .get_statistics()

            )


        except Exception:


            history = {

                "files_processed": 0,

                "saved_bytes": 0

            }



        return {


            "files_processed":

                history.get(

                    "files_processed",

                    0

                ),



            "saved_bytes":

                history.get(

                    "saved_bytes",

                    0

                ),



            "current_jobs":

                self.queue_manager.size()

        }



    # ==================================
    # Refresh Dashboard
    # ==================================

    def refresh_data(
        self
    ):


        stats = self.load_statistics()



        self.files_card.set_value(

            stats["files_processed"]

        )


        self.saved_card.set_value(

            self.format_bytes(

                stats["saved_bytes"]

            )

        )


        self.jobs_card.set_value(

            stats["current_jobs"]

        )



        self.activity_list.clear()



        self.load_recent_activity()



    # ==================================
    # Recent Activity
    # ==================================

    def load_recent_activity(
        self
    ):


        try:

            history = (

                self.history_manager

                .get_recent_history()

            )


        except Exception:


            history = []



        for item in history:


            try:


                output_file = item[2]

                output_format = item[3]

                status = item[6]



                self.activity_list.addItem(

                    f"{output_file} | {output_format} | {status}"

                )


            except Exception:


                continue



    # ==================================
    # Format Bytes
    # ==================================

    def format_bytes(
        self,
        value
    ):


        if value < 1024:

            return f"{value} B"



        if value < 1024 ** 2:

            return f"{value / 1024:.1f} KB"



        if value < 1024 ** 3:

            return f"{value / (1024 ** 2):.1f} MB"



        return f"{value / (1024 ** 3):.1f} GB"