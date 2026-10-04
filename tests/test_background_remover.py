from pathlib import Path


from core.image_loader import ImageLoader
from ai.background_remover import BackgroundRemover



PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_background_remover():


    image_file = (
        PROJECT_ROOT
        /
        "assets"
        /
        "test"
        /
        "sample.jpg"
    )


    image = ImageLoader(
        str(image_file)
    ).load()


    remover = BackgroundRemover()


    result = remover.remove_background(
        image
    )


    assert result.mode == "RGBA"