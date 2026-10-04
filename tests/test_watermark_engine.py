from pathlib import Path

from core.image_loader import ImageLoader
from core.watermark_engine import WatermarkEngine



PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_text_watermark():


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



    engine = WatermarkEngine()



    result = engine.apply_text(
        image,
        "TEST WATERMARK",
        {
            "position": "center",
            "opacity": 120,
            "font_size": 30
        }
    )


    assert result.size == image.size