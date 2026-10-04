"""
JPEG Encoder
"""

from .base_encoder import BaseEncoder



class JPGEncoder(BaseEncoder):


    def encode(
        self,
        image,
        output_path,
        settings=None
    ):

        settings = settings or {}


        quality = settings.get(
            "quality",
            85
        )


        if image.mode != "RGB":

            image = image.convert(
                "RGB"
            )


        image.save(
            output_path,
            "JPEG",
            quality=quality,
            optimize=True
        )


        return output_path