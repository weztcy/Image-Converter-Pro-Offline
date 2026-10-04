"""
Image Converter Engine
"""


from pathlib import Path


from formats.encoder_manager import EncoderManager


from .resize_engine import ResizeEngine
from .image_edit_engine import ImageEditEngine
from .optimization_engine import OptimizationEngine
from .metadata_manager import MetadataManager
from .watermark_engine import WatermarkEngine
from .history_manager import HistoryManager


from ai.background_remover import BackgroundRemover


from plugins.manager import PluginManager
from plugins.loader import PluginLoader




class ImageConverter:


    def __init__(
        self,
        image,
        input_path=None
    ):


        self.image = image

        self.input_path = input_path



        self.encoder_manager = EncoderManager()

        self.resize_engine = ResizeEngine()

        self.edit_engine = ImageEditEngine()

        self.optimizer = OptimizationEngine()

        self.metadata_manager = MetadataManager()

        self.watermark_engine = WatermarkEngine()

        self.history_manager = HistoryManager()

        self.background_remover = BackgroundRemover()



        # Plugin System

        self.plugin_manager = PluginManager()


        self.plugin_loader = PluginLoader(
            self.plugin_manager
        )


        self.plugin_loader.load_plugins()




    def convert(
        self,
        output_path,
        output_format,
        settings=None
    ):


        settings = settings or {}



        output_path = Path(
            output_path
        )



        image = self.image.copy()



        # ==================================
        # Optimization
        # ==================================

        if settings.get(
            "auto_optimize",
            False
        ):


            try:


                recommendation = (

                    self.optimizer.recommend(

                        image,

                        output_format

                    )

                )


                settings.update(
                    recommendation
                )


            except Exception:

                pass



        # ==================================
        # Image Editing
        # ==================================


        if "crop" in settings:


            image = self.edit_engine.crop(

                image,

                settings["crop"]

            )



        if "rotate" in settings:


            image = self.edit_engine.rotate(

                image,

                settings["rotate"]

            )



        if settings.get(
            "flip_horizontal",
            False
        ):


            image = self.edit_engine.flip_horizontal(
                image
            )



        if settings.get(
            "flip_vertical",
            False
        ):


            image = self.edit_engine.flip_vertical(
                image
            )



        # ==================================
        # Resize
        # ==================================

        resize_data = None



        # New UI format

        if settings.get(
            "resize",
            False
        ):


            resize_data = {

                "width":
                    settings.get(
                        "width",
                        image.width
                    ),


                "height":
                    settings.get(
                        "height",
                        image.height
                    ),


                "keep_ratio":
                    settings.get(
                        "keep_ratio",
                        True
                    )

            }



        # Old format compatibility

        elif isinstance(
            settings.get("resize"),
            dict
        ):


            resize_data = settings["resize"]




        if resize_data:


            image = self.resize_engine.resize_by_pixel(

                image,

                resize_data["width"],

                resize_data["height"],

                resize_data.get(

                    "keep_ratio",

                    True

                )

            )



        # ==================================
        # Metadata
        # ==================================


        image = self.metadata_manager.process(

            image,

            settings

        )



        # ==================================
        # Background Removal
        # ==================================


        if settings.get(
            "remove_background",
            False
        ):


            try:


                image = (

                    self.background_remover

                    .remove_background(

                        image

                    )

                )


            except Exception:


                pass



        # ==================================
        # Watermark
        # ==================================


        watermark = settings.get(
            "watermark"
        )



        if isinstance(
            watermark,
            dict
        ):


            watermark_type = watermark.get(

                "type",

                "text"

            )



            try:


                if watermark_type == "text":


                    image = self.watermark_engine.apply_text(

                        image,

                        watermark.get(
                            "text",
                            ""
                        ),

                        watermark

                    )



                elif watermark_type == "image":


                    image = self.watermark_engine.apply_image(

                        image,

                        watermark["path"],

                        watermark

                    )


            except Exception:


                pass




        # ==================================
        # Plugin Processing
        # ==================================


        image = self.plugin_manager.process(

            image,

            settings

        )



        # ==================================
        # Encode
        # ==================================


        encoder = self.encoder_manager.get_encoder(

            output_format

        )



        result = encoder.encode(

            image,

            str(output_path),

            settings

        )



        result = Path(
            result
        )



        # ==================================
        # History
        # ==================================


        try:


            self.history_manager.record(

                self.input_path
                if self.input_path
                else "",


                result,


                output_format,


                "success"

            )


        except Exception:


            pass



        return result