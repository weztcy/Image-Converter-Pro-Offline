from ai.gpu_manager import GPUManager
from ai.runtime_provider import RuntimeProvider



def test_gpu_manager():


    gpu = GPUManager()


    assert isinstance(
        gpu.has_cuda(),
        bool
    )



def test_runtime_provider():


    provider = RuntimeProvider()


    result = provider.get()


    assert len(result) >= 1