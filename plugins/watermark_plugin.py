"""
Watermark Plugin Example
"""


from PIL import ImageDraw



class WatermarkPlugin:


    def process_image(
        self,
        image,
        settings
    ):


        watermark = settings.get(
            "plugin_watermark"
        )


        if not watermark:

            return image



        draw = ImageDraw.Draw(
            image
        )


        draw.text(
            (10,10),
            watermark,
        )


        return image



plugin = WatermarkPlugin()