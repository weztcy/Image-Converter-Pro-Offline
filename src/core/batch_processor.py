"""
Batch Processing Engine

Responsible for:
- Processing multiple images
- Managing conversion jobs
- Collecting results
"""


from pathlib import Path


from .image_loader import ImageLoader
from .converter import ImageConverter
from .rename_engine import RenameEngine




class BatchProcessor:
    """
    Handle multiple image conversion.
    """


    SUPPORTED_EXTENSIONS = {

        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".bmp",
        ".gif",
        ".tiff",
        ".heic",
        ".heif",
        ".avif",

    }



    def __init__(self):

        self.results = {

            "success": [],

            "failed": []

        }


        self.rename_engine = RenameEngine()



    def reset_results(self):

        self.results = {

            "success": [],

            "failed": []

        }



    def get_images_from_folder(
        self,
        folder_path
    ):


        folder = Path(
            folder_path
        )


        images = []


        for file in folder.iterdir():


            if (

                file.is_file()

                and

                file.suffix.lower()

                in self.SUPPORTED_EXTENSIONS

            ):


                images.append(
                    file
                )


        return images



    def process_files(
        self,
        files,
        output_folder,
        output_format="WEBP",
        settings=None,
        rename_template="{name}",
        reset=True
    ):


        if reset:

            self.reset_results()



        settings = settings or {}



        output_folder = Path(
            output_folder
        )


        output_folder.mkdir(
            parents=True,
            exist_ok=True
        )



        for index, file in enumerate(
            files,
            start=1
        ):


            try:


                image = ImageLoader(
                    str(file)
                ).load()



                converter = ImageConverter(
                    image,
                    str(file)
                )



                filename = self.rename_engine.generate(
                    file,
                    output_format,
                    rename_template,
                    index
                )



                output_file = (

                    output_folder

                    /

                    filename

                )



                converter.convert(
                    str(output_file),
                    output_format,
                    settings
                )



                self.results["success"].append(

                    str(output_file)

                )



            except Exception as error:


                self.results["failed"].append(

                    {

                        "file": str(file),

                        "error": str(error)

                    }

                )



        return self.results