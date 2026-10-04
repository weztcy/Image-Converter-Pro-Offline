"""
SVG Converter

Using Qt SVG Renderer
"""

from pathlib import Path

from PySide6.QtSvg import QSvgRenderer
from PySide6.QtGui import QImage, QPainter
from PySide6.QtCore import QSize

import sys

from PySide6.QtWidgets import QApplication

class SVGConverter:

    def __init__(self):

        self.app_created = False

        if QApplication.instance() is None:

            self.app = QApplication(
                sys.argv
            )

            self.app_created = True


    def convert(
        self,
        input_path,
        output_path,
        width=1024,
        height=1024
    ):

        input_path = Path(
            input_path
        )


        if not input_path.exists():

            raise FileNotFoundError(
                f"SVG not found: {input_path}"
            )


        renderer = QSvgRenderer(
            str(input_path)
        )


        if not renderer.isValid():

            raise ValueError(
                "Invalid SVG file"
            )


        image = QImage(
            QSize(
                width,
                height
            ),
            QImage.Format_ARGB32
        )


        image.fill(0)


        painter = QPainter(
            image
        )


        renderer.render(
            painter
        )


        painter.end()


        image.save(
            output_path
        )


        return output_path