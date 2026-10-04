from pathlib import Path


from core.image_loader import ImageLoader
from ai.optimization_ai import AIOptimization



PROJECT_ROOT = Path(__file__).resolve().parents[1]



def test_ai_optimization():


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


    optimizer = AIOptimization()


    result = optimizer.recommend(
        image
    )


    assert "format" in result

    assert "quality" in result