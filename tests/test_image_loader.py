from pathlib import Path

from core.image_loader import ImageLoader


def test_loader_class_exists():

    loader = ImageLoader(
        "sample.jpg"
    )

    assert loader.file_path.name == "sample.jpg"