"""
Preset Manager

Store conversion presets locally.
"""


import json

from pathlib import Path



PRESET_FILE = (

    Path.home()

    /

    ".image_converter_presets.json"

)



class PresetManager:



    def __init__(self):

        self.presets = {}

        self.load()



    def load(self):

        if PRESET_FILE.exists():

            with open(
                PRESET_FILE,
                "r"
            ) as file:

                self.presets = json.load(
                    file
                )

        else:

            self.presets = {}



    def save(self):

        with open(
            PRESET_FILE,
            "w"
        ) as file:

            json.dump(
                self.presets,
                file,
                indent=4
            )



    def create(
        self,
        name,
        settings
    ):

        self.presets[name] = settings

        self.save()



    def get(
        self,
        name
    ):

        return self.presets.get(
            name
        )



    def delete(
        self,
        name
    ):

        if name in self.presets:

            del self.presets[name]

            self.save()



    def list_presets(self):

        return list(
            self.presets.keys()
        )