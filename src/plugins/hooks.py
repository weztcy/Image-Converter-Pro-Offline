"""
Plugin Hooks
"""


import pluggy



hookspec = pluggy.HookspecMarker(
    "image_converter"
)



class PluginSpec:


    @hookspec
    def process_image(
        self,
        image,
        settings
    ):

        """
        Process image using plugin.
        """