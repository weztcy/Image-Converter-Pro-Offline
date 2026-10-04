from pathlib import Path

from core.image_loader import ImageLoader
from core.converter import ImageConverter


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_jpg_to_webp():

    input_file = (
        PROJECT_ROOT
        / "assets"
        / "test"
        / "sample.jpg"
    )

    output_file = (
        PROJECT_ROOT
        / "assets"
        / "test"
        / "output"
        / "result_test.webp"
    )


    image = ImageLoader(
        str(input_file)
    ).load()


    converter = ImageConverter(
        image
    )


    output = converter.convert(
        str(output_file),
        "WEBP"
    )


    assert output.exists()