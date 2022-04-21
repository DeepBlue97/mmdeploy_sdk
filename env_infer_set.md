DELL G15

"""
失败的一次：推理时过很久，然后没报错退出。
$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox\TensorRT-8.2.3.0\lib;' + $env:path
$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox\cuda\lib\x64;' + $env:path
$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox\cuda\bin;' + $env:path
$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\build\bin\Release;' + $env:path


$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\TensorRT-8.2.3.0\lib;' + $env:path
$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\cuda\lib\x64;' + $env:path
$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\cuda\bin;' + $env:path
$env:path = 'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\mmdeploy\build\bin\Release;' + $env:path


onnx

$env:ONNXRUNTIME_DIR = "$pwd\onnxruntime-win-x64-1.8.1"
$env:path = "$env:ONNXRUNTIME_DIR\lib;" + $env:path


ppl

cd ppl.cv
$env:PPLCV_DIR = "$pwd"


"""


import os

os.environ['path'] = r'E:\workspace\win10\lab_mmdeploy\cuda\bin;' + os.environ['path']
