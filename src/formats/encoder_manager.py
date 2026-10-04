"""
Encoder Manager

Central encoder registry.
"""


from .webp_encoder import WebPEncoder
from .jpg_encoder import JPGEncoder
from .png_encoder import PNGEncoder
from .avif_encoder import AVIFEncoder
from .tiff_encoder import TIFFEncoder
from .gif_encoder import GIFEncoder
from .ico_encoder import ICOEncoder




class EncoderManager:


    def __init__(
        self
    ):


        self.encoders = {


            "WEBP":
                WebPEncoder(),


            "JPG":
                JPGEncoder(),


            "JPEG":
                JPGEncoder(),


            "PNG":
                PNGEncoder(),


            "AVIF":
                AVIFEncoder(),


            "TIFF":
                TIFFEncoder(),


            "GIF":
                GIFEncoder(),


            "ICO":
                ICOEncoder(),

        }



    # ==================================
    # Get Encoder
    # ==================================

    def get_encoder(
        self,
        format_name
    ):


        format_name = format_name.upper()



        if format_name not in self.encoders:


            raise ValueError(

                f"Unsupported encoder: {format_name}"

            )



        return self.encoders[
            format_name
        ]



    # ==================================
    # Get Available Formats
    # ==================================

    def get_supported_formats(
        self
    ):


        formats = []


        for name in self.encoders.keys():


            # hide alias
            # JPEG menggunakan JPG encoder

            if name == "JPEG":

                continue



            formats.append(
                name
            )



        return formats