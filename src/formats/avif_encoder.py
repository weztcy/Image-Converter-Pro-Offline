"""
AVIF Encoder
"""

from .base_encoder import BaseEncoder



class AVIFEncoder(BaseEncoder):


    def encode(
        self,
        image,
        output_path,
        settings=None
    ):

        settings = settings or {}


        mode = settings.get(
            "mode",
            "lossy"
        )


        quality = settings.get(
            "quality",
            60
        )


        options = {}


        if mode == "lossless":

            options["lossless"] = True

        else:

            options["quality"] = quality


        image.save(
            output_path,
            "AVIF",
            **options
        )


        return output_path