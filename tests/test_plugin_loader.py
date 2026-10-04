from plugins.manager import PluginManager
from plugins.loader import PluginLoader



def test_plugin_loader():


    manager = PluginManager()


    loader = PluginLoader(
        manager
    )


    loader.load_plugins()


    assert manager is not None