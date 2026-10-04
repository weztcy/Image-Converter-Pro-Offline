"""
Plugin Base Interface
"""


class BasePlugin:


    name = "base"



    def initialize(self):

        pass



    def process(
        self,
        image,
        settings
    ):

        return image