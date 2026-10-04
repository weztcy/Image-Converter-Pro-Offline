"""
Watermark Engine

Handle:
- Text watermark
- Image watermark
- Position
- Opacity
- Scale
"""


from PIL import Image, ImageDraw, ImageFont


class WatermarkEngine:


    def apply_text(
        self,
        image,
        text,
        settings=None
    ):

        settings = settings or {}


        base = image.convert(
            "RGBA"
        )


        overlay = Image.new(
            "RGBA",
            base.size,
            (0, 0, 0, 0)
        )


        draw = ImageDraw.Draw(
            overlay
        )


        opacity = settings.get(
            "opacity",
            128
        )


        font_size = settings.get(
            "font_size",
            40
        )


        try:

            font = ImageFont.truetype(
                "arial.ttf",
                font_size
            )

        except:

            font = ImageFont.load_default()



        position = self.calculate_text_position(
            base.size,
            text,
            font,
            settings.get(
                "position",
                "bottom_right"
            )
        )


        draw.text(
            position,
            text,
            font=font,
            fill=(
                255,
                255,
                255,
                opacity
            )
        )


        return Image.alpha_composite(
            base,
            overlay
        )



    def apply_image(
        self,
        image,
        watermark_path,
        settings=None
    ):

        settings = settings or {}


        base = image.convert(
            "RGBA"
        )


        watermark = Image.open(
            watermark_path
        ).convert(
            "RGBA"
        )


        scale = settings.get(
            "scale",
            1.0
        )


        if scale != 1.0:

            size = (
                int(watermark.width * scale),
                int(watermark.height * scale)
            )

            watermark = watermark.resize(
                size,
                Image.Resampling.LANCZOS
            )


        opacity = settings.get(
            "opacity",
            128
        )


        alpha = watermark.getchannel(
            "A"
        )


        alpha = alpha.point(
            lambda value:
            value * opacity // 255
        )


        watermark.putalpha(
            alpha
        )


        position = self.calculate_image_position(
            base.size,
            watermark.size,
            settings.get(
                "position",
                "bottom_right"
            )
        )


        base.alpha_composite(
            watermark,
            position
        )


        return base



    def calculate_text_position(
        self,
        image_size,
        text,
        font,
        position
    ):

        width, height = image_size


        bbox = font.getbbox(
            text
        )


        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]


        margin = 20


        positions = {

            "top_left":
            (
                margin,
                margin
            ),

            "top_right":
            (
                width-text_width-margin,
                margin
            ),

            "center":
            (
                (width-text_width)//2,
                (height-text_height)//2
            ),

            "bottom_left":
            (
                margin,
                height-text_height-margin
            ),

            "bottom_right":
            (
                width-text_width-margin,
                height-text_height-margin
            )

        }


        return positions.get(
            position,
            positions["bottom_right"]
        )



    def calculate_image_position(
        self,
        image_size,
        watermark_size,
        position
    ):

        width, height = image_size

        wm_width, wm_height = watermark_size


        margin = 20


        positions = {

            "top_left":
            (
                margin,
                margin
            ),

            "top_right":
            (
                width-wm_width-margin,
                margin
            ),

            "center":
            (
                (width-wm_width)//2,
                (height-wm_height)//2
            ),

            "bottom_left":
            (
                margin,
                height-wm_height-margin
            ),

            "bottom_right":
            (
                width-wm_width-margin,
                height-wm_height-margin
            )

        }


        return positions.get(
            position,
            positions["bottom_right"]
        )