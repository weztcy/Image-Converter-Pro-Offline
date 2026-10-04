"""
Metadata Manager

Handle image metadata operations.

Features:
- Keep metadata
- Remove metadata
- Remove GPS information
- Privacy mode
"""


from PIL import Image



class MetadataManager:


    def extract(self, image):
        """
        Extract image metadata.
        """

        return image.info.copy()



    def remove_all(self, image):
        """
        Remove all metadata.

        Create clean image copy.
        """

        clean_image = Image.new(
            image.mode,
            image.size
        )


        if hasattr(
            image,
            "get_flattened_data"
        ):

            clean_image.putdata(
                list(
                    image.get_flattened_data()
                )
            )

        else:

            clean_image.putdata(
                list(
                    image.getdata()
                )
            )


        return clean_image



    def remove_gps(self, metadata):
        """
        Remove GPS EXIF data.

        Placeholder for EXIF GPS handling.
        """

        if "exif" not in metadata:

            return metadata


        return metadata



    def process(
        self,
        image,
        settings=None
    ):

        """
        Process metadata based on settings.

        Settings example:

        {
            "keep_metadata": True,
            "remove_gps": True,
            "privacy_mode": True
        }
        """


        settings = settings or {}


        keep_metadata = settings.get(
            "keep_metadata",
            False
        )


        privacy_mode = settings.get(
            "privacy_mode",
            False
        )


        if privacy_mode:

            return self.remove_all(
                image
            )


        if not keep_metadata:

            return self.remove_all(
                image
            )


        return image