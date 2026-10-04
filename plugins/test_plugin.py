"""
Example External Plugin
"""


class TestPlugin:


    def process_image(
        self,
        image,
        settings
    ):

        return image



plugin = TestPlugin()