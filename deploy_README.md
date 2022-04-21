注意点：

1. Python 3.7 !! + vs2019
2. 使用系统公用的（非conda安装）CUDA 11.1最新版
3. 使用 pip安装pytorch 1.8.2 即可，如果设置了pip镜像源则会有加速效果，  （1.8.0好像安装mmcv-full==1.4.0时会失败）
4. opencv env: $env:path = "D:\workspace\deep_learning\mmdeploy_yolox\opencv\build;" + $env:path
5. 2060s成功转换推理fp32; 3060失败，可能还不支持30系显卡
6. 安装成功案例：conda torch1.8.2 + py37 + mmdeploy v0.3.0 + pip install mmcv1.4.0  = successful! 不需要删除conda中的cudatoolkit（系统cuda为11.1）


编译SDK：

```

cd $env:MMDEPLOY_DIR
mkdir build -ErrorAction SilentlyContinue
cd build
cmake .. -G "Visual Studio 16 2019" -A x64 -T v142 `
  -DMMDEPLOY_BUILD_SDK=ON `
  -DMMDEPLOY_TARGET_DEVICES="cuda" `
  -DMMDEPLOY_TARGET_BACKENDS="trt" `
  -DMMDEPLOY_CODEBASES="mmdet" `
  -Dpplcv_DIR="$env:PPLCV_DIR/pplcv-build/install/lib/cmake/ppl" `
  -DTENSORRT_DIR="$env:TENSORRT_DIR" `
  -DCUDNN_DIR="$env:CUDNN_DIR"

cmake --build . --config Release -- /m
cmake --install . --config Release

```