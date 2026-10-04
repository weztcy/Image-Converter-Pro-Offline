"""
Plugin Auto Loader
"""


import importlib.util

from pathlib import Path



class PluginLoader:


    def __init__(
        self,
        manager
    ):

        self.manager = manager



    def load_plugins(
        self,
        folder="plugins"
    ):


        plugin_path = Path(
            folder
        )


        if not plugin_path.exists():

            return



        for file in plugin_path.glob(
            "*_plugin.py"
        ):


            spec = importlib.util.spec_from_file_location(
                file.stem,
                file
            )


            if spec is None:

                continue



            module = importlib.util.module_from_spec(
                spec
            )


            spec.loader.exec_module(
                module
            )



            if hasattr(
                module,
                "plugin"
            ):


                self.manager.register(
                    module.plugin
                )