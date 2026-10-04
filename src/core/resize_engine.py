"""
Resize Engine

Handle image resizing operations.
"""


from PIL import Image



class ResizeEngine:


    def resize_by_pixel(
        self,
        image,
        width,
        height,
        keep_ratio=True
    ):

        original_width, original_height = image.size


        if keep_ratio:

            ratio = min(
                width / original_width,
                height / original_height
            )


            new_size = (
                int(original_width * ratio),
                int(original_height * ratio)
            )

        else:

            new_size = (
                width,
                height
            )


        return image.resize(
            new_size,
            Image.Resampling.LANCZOS
        )



    def resize_by_percentage(
        self,
        image,
        percentage
    ):

        width, height = image.size


        new_size = (
            int(width * percentage / 100),
            int(height * percentage / 100)
        )


        return image.resize(
            new_size,
            Image.Resampling.LANCZOS
        )