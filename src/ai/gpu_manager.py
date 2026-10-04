"""
GPU Manager

Detect available acceleration hardware.
"""


class GPUManager:


    def __init__(self):

        self.cuda_available = False

        self.providers = []

        self.detect()



    def detect(self):

        try:

            import onnxruntime as ort


            self.providers = (
                ort.get_available_providers()
            )


            if (
                "CUDAExecutionProvider"
                in self.providers
            ):

                self.cuda_available = True



        except Exception:

            self.providers = []

            self.cuda_available = False



    def has_cuda(self):

        return self.cuda_available



    def get_providers(self):

        return self.providers