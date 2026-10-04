"""
PNG Encoder
"""

from .base_encoder import BaseEncoder



class PNGEncoder(BaseEncoder):


    def encode(
        self,
        image,
        output_path,
        settings=None
    ):

        settings = settings or {}


        compression = settings.get(
            "compression",
            6
        )


        image.save(
            output_path,
            "PNG",
            compress_level=compression
        )


        return output_path