"""
AI Optimization Recommendation Engine
"""


from .image_analyzer import ImageAnalyzer



class AIOptimization:


    def __init__(self):

        self.analyzer = ImageAnalyzer()



    def recommend(
        self,
        image
    ):


        analysis = self.analyzer.analyze(
            image
        )


        quality = 85


        if analysis["pixels"] > 8000000:

            quality = 80



        resize = None


        if analysis["width"] > 2048:


            resize = {

                "width":2048,

                "height":
                    int(
                        image.height
                        *
                        2048
                        /
                        image.width
                    ),

                "keep_ratio":True

            }



        return {

            "format":"WEBP",

            "quality":quality,

            "resize":resize,

            "analysis":analysis

        }