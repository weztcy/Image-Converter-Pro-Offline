"""
Application Settings Manager

Store user preferences locally.
"""

import json

from pathlib import Path



SETTINGS_PATH = (
    Path.home()
    /
    ".image_converter_pro_settings.json"
)



DEFAULT_SETTINGS = {

    "default_format": "WEBP",

    "webp_mode": "lossy",

    "webp_quality": 85,

    "default_output": "",

    "theme": "dark"

}



class SettingsManager:


    def __init__(self):

        self.settings = {}

        self.load()



    def load(self):

        if SETTINGS_PATH.exists():

            with open(
                SETTINGS_PATH,
                "r"
            ) as file:

                self.settings = json.load(file)

        else:

            self.settings = DEFAULT_SETTINGS.copy()



    def save(self):

        with open(
            SETTINGS_PATH,
            "w"
        ) as file:

            json.dump(
                self.settings,
                file,
                indent=4
            )



    def get(
        self,
        key
    ):

        return self.settings.get(
            key
        )



    def set(
        self,
        key,
        value
    ):

        self.settings[key] = value

        self.save()