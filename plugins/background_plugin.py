"""
Background Removal Plugin Example
"""


from ai.background_remover import BackgroundRemover



class BackgroundPlugin:


    def __init__(self):

        self.remover = BackgroundRemover()



    def process_image(
        self,
        image,
        settings
    ):


        if settings.get(
            "plugin_remove_background",
            False
        ):

            return (
                self.remover
                .remove_background(
                    image
                )
            )


        return image



plugin = BackgroundPlugin()