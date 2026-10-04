"""
Plugin Manager
"""


import pluggy


from .hooks import PluginSpec



class PluginManager:


    def __init__(self):

        self.manager = pluggy.PluginManager(
            "image_converter"
        )


        self.manager.add_hookspecs(
            PluginSpec
        )



    def register(
        self,
        plugin
    ):

        self.manager.register(
            plugin
        )



    def process(
        self,
        image,
        settings
    ):


        results = (
            self.manager
            .hook
            .process_image(
                image=image,
                settings=settings
            )
        )


        for result in results:

            if result is not None:

                image = result


        return image