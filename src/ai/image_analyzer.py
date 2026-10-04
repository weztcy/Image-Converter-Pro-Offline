"""
Image Analyzer

Analyze image characteristics.
"""


from PIL import ImageStat



class ImageAnalyzer:


    def analyze(
        self,
        image
    ):


        stat = ImageStat.Stat(
            image.convert("RGB")
        )


        brightness = (
            sum(stat.mean)
            /
            3
        )


        return {

            "brightness": brightness,

            "width": image.width,

            "height": image.height,

            "pixels":
                image.width
                *
                image.height

        }