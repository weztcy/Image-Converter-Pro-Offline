"""
Background Remover AI Engine

Local AI background removal.
"""


from PIL import Image

from rembg import remove



class BackgroundRemover:



    def __init__(self):

        self.available = True



    def remove_background(
        self,
        image
    ):

        """
        Remove image background.

        Return:
        RGBA image
        """


        if image.mode != "RGBA":

            image = image.convert(
                "RGBA"
            )


        result = remove(
            image
        )


        return result



    def is_available(
        self
    ):

        return self.available