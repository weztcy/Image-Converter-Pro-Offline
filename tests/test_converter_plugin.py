from pathlib import Path

from core.image_loader import ImageLoader
from core.converter import ImageConverter



PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_converter_plugin_loading():


    input_file = (
        PROJECT_ROOT
        /
        "assets"
        /
        "test"
        /
        "sample.jpg"
    )


    image = ImageLoader(
        str(input_file)
    ).load()


    converter = ImageConverter(
        image,
        str(input_file)
    )


    assert converter.plugin_manager is not None