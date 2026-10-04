"""
Image Edit Engine

Handle:
- Crop
- Rotate
- Flip
"""

from PIL import Image



class ImageEditEngine:



    def crop(
        self,
        image,
        box
    ):

        """
        Crop image.

        box:
        (
            left,
            top,
            right,
            bottom
        )
        """

        return image.crop(
            box
        )



    def crop_center(
        self,
        image,
        width,
        height
    ):

        """
        Center crop.
        """

        image_width, image_height = image.size


        left = (
            image_width - width
        ) // 2


        top = (
            image_height - height
        ) // 2


        right = left + width

        bottom = top + height


        return image.crop(
            (
                left,
                top,
                right,
                bottom
            )
        )



    def rotate(
        self,
        image,
        angle
    ):

        return image.rotate(
            angle,
            expand=True
        )



    def flip_horizontal(
        self,
        image
    ):

        return image.transpose(
            Image.Transpose.FLIP_LEFT_RIGHT
        )



    def flip_vertical(
        self,
        image
    ):

        return image.transpose(
            Image.Transpose.FLIP_TOP_BOTTOM
        )