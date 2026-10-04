"""
Application Launcher

Image Converter Pro Offline
"""


import sys


from PySide6.QtWidgets import QApplication


from ui.windows.main_window import MainWindow

from ui.themes.theme_manager import ThemeManager




def run():


    app = QApplication(
        sys.argv
    )



    # ==============================
    # Load Application Theme
    # ==============================

    theme_manager = ThemeManager()


    theme_manager.apply(
        app
    )



    window = MainWindow()


    window.show()



    sys.exit(
        app.exec()
    )



if __name__ == "__main__":

    run()