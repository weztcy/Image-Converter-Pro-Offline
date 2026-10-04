"""
TIFF Encoder
"""

from .base_encoder import BaseEncoder



class TIFFEncoder(BaseEncoder):


    def encode(
        self,
        image,
        output_path,
        settings=None
    ):

        settings = settings or {}


        compression = settings.get(
            "compression",
            "tiff_lzw"
        )


        image.save(
            output_path,
            "TIFF",
            compression=compression
        )


        return output_path