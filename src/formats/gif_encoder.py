"""
GIF Encoder
"""

from .base_encoder import BaseEncoder



class GIFEncoder(BaseEncoder):


    def encode(
        self,
        image,
        output_path,
        settings=None
    ):

        settings = settings or {}


        keep_animation = settings.get(
            "animation",
            False
        )


        if (
            keep_animation
            and getattr(
                image,
                "is_animated",
                False
            )
        ):

            frames = []


            for frame in range(
                image.n_frames
            ):

                image.seek(
                    frame
                )


                frames.append(
                    image.copy()
                )


            first_frame = frames[0]


            first_frame.save(
                output_path,
                "GIF",
                save_all=True,
                append_images=frames[1:],
                loop=0,
                duration=image.info.get(
                    "duration",
                    100
                )
            )


        else:

            image.save(
                output_path,
                "GIF"
            )


        return output_path