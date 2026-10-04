"""
Base Encoder

Parent class for all format encoders.
"""


class BaseEncoder:


    def encode(
        self,
        image,
        output_path,
        settings=None
    ):

        raise NotImplementedError(
            "Encoder must implement encode method"
        )