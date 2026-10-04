from plugins.manager import PluginManager



class TestPlugin:


    def process_image(
        self,
        image,
        settings
    ):

        return image



def test_plugin_manager():


    manager = PluginManager()


    plugin = TestPlugin()


    manager.register(
        plugin
    )


    result = manager.process(
        "image",
        {}
    )


    assert result == "image"