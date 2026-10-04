from pathlib import Path

from core.image_loader import ImageLoader
from core.metadata_manager import MetadataManager



PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_remove_metadata():

    image_path = (
        PROJECT_ROOT
        /
        "assets"
        /
        "test"
        /
        "sample.jpg"
    )


    image = ImageLoader(
        str(image_path)
    ).load()


    manager = MetadataManager()


    result = manager.process(
        image,
        {
            "privacy_mode": True
        }
    )


    assert result.size == image.size