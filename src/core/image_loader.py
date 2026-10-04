"""
Image Loader Module

Responsible for:
- Loading image files
- Validating image format
- Reading image metadata
"""

from pathlib import Path
from PIL import Image

from pillow_heif import register_heif_opener

import pillow_avif

register_heif_opener()

class ImageLoader:
    """
    Handle image loading operation.
    """

    SUPPORTED_FORMATS = {
        "JPEG",
        "PNG",
        "WEBP",
        "GIF",
        "TIFF",
        "BMP",
        "HEIC",
        "HEIF",
        "AVIF",
        "SVG",
    }

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def validate_file(self):
        """
        Check file existence.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(
                f"File not found: {self.file_path}"
            )

        return True

    def load(self):
        """
        Load image using Pillow.
        """

        self.validate_file()

        image = Image.open(self.file_path)

        return image

    def get_information(self):
        """
        Return basic image information.
        """

        image = self.load()

        return {
            "filename": self.file_path.name,
            "format": image.format,
            "size": image.size,
            "mode": image.mode,
        }
        
    def get_animation_info(self):

        image = self.load()

        return {
            "is_animated": getattr(
                image,
                "is_animated",
                False
            ),

            "frames": getattr(
                image,
                "n_frames",
                1
            )
        }