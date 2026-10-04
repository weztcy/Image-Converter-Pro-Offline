"""
Optimizer Plugin Example
"""


class OptimizerPlugin:


    def process_image(
        self,
        image,
        settings
    ):


        if settings.get(
            "plugin_optimize",
            False
        ):


            settings["quality"] = 80



        return image



plugin = OptimizerPlugin()