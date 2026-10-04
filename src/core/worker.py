"""
Worker Processor

Execute queued conversion jobs.
"""


from .image_loader import ImageLoader
from .converter import ImageConverter



class Worker:


    def __init__(self):

        self.results = {
            "success": [],
            "failed": []
        }



    def process(
        self,
        job
    ):

        try:

            image = ImageLoader(
                job["input"]
            ).load()



            converter = ImageConverter(
                image,
                job["input"]
            )



            settings = job.get(
                "settings",
                {}
            )



            # Backward compatibility
            # Support old job format:
            #
            # {
            #     "quality": 80
            # }

            if "quality" in job:

                settings["quality"] = job["quality"]



            result = converter.convert(
                job["output"],
                job["format"],
                settings
            )



            self.results["success"].append(
                str(result)
            )



        except Exception as error:


            self.results["failed"].append(
                {
                    "file": job["input"],
                    "error": str(error)
                }
            )


        return self.results