"""
ICO Encoder
"""

from .base_encoder import BaseEncoder



class ICOEncoder(BaseEncoder):


    def encode(
        self,
        image,
        output_path,
        settings=None
    ):

        settings = settings or {}


        sizes = settings.get(
            "sizes",
            [
                (16,16),
                (32,32),
                (48,48),
                (64,64),
                (128,128),
                (256,256)
            ]
        )


        image.save(
            output_path,
            "ICO",
            sizes=sizes
        )


        return output_path