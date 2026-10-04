"""
ONNX Runtime Provider Selector
"""


from .gpu_manager import GPUManager



class RuntimeProvider:


    def __init__(self):

        self.gpu = GPUManager()



    def get(self):


        if self.gpu.has_cuda():

            return [
                "CUDAExecutionProvider",
                "CPUExecutionProvider"
            ]


        return [
            "CPUExecutionProvider"
        ]