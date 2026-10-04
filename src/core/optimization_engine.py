"""
Smart Compression Optimization Engine

Analyze image characteristics
and recommend export settings.

Supports:
- Basic optimization
- AI optimization fallback
"""


from PIL import ImageStat


from ai.optimization_ai import AIOptimization



class OptimizationEngine:


    def __init__(self):

        self.ai_optimizer = AIOptimization()



    def analyze(
        self,
        image
    ):

        stat = ImageStat.Stat(
            image.convert("RGB")
        )


        brightness = (
            sum(stat.mean)
            /
            3
        )


        return {

            "brightness": brightness,

            "width": image.width,

            "height": image.height,

            "has_alpha": (
                image.mode == "RGBA"
            )

        }



    def basic_recommend(
        self,
        image,
        output_format="WEBP"
    ):


        analysis = self.analyze(
            image
        )


        recommendation = {


            "format": output_format,


            "quality": 85

        }



        if analysis["has_alpha"]:


            recommendation["mode"] = (
                "lossless"
            )


            recommendation["quality"] = 90



        else:


            recommendation["mode"] = (
                "lossy"
            )


            if analysis["width"] > 3000:


                recommendation["quality"] = 75



            elif analysis["width"] > 1500:


                recommendation["quality"] = 80



            else:


                recommendation["quality"] = 85



        return recommendation



    def recommend(
        self,
        image,
        output_format="WEBP"
    ):


        try:

            ai_result = (
                self.ai_optimizer
                .recommend(
                    image
                )
            )


            if ai_result:

                ai_result["format"] = (
                    output_format
                )


                return ai_result



        except Exception:

            pass



        return self.basic_recommend(
            image,
            output_format
        )