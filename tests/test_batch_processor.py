from pathlib import Path

from core.batch_processor import BatchProcessor


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_batch_processing():

    processor = BatchProcessor()


    files = [
        PROJECT_ROOT / "assets" / "test" / "sample.jpg"
    ]


    output_folder = (
        PROJECT_ROOT
        / "assets"
        / "test"
        / "output"
    )


    result = processor.process_files(
        files,
        output_folder,
        "WEBP"
    )


    assert len(
        result["success"]
    ) == 1