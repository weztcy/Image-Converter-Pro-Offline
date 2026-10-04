from plugins.manager import PluginManager
from plugins.loader import PluginLoader



def test_official_plugins():


    manager = PluginManager()


    loader = PluginLoader(
        manager
    )


    loader.load_plugins()


    assert manager is not None