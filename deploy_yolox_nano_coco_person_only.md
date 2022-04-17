注意点：

1. windows 11 系统， vs2019 community版
2. 使用系统公用的（非conda安装）CUDA 11.1最新版
3. 使用 conda安装pytorch 1.8.2， 然后pip uninstall cudatoolkit（切记！！） （1.8.0好像安装mmcv-full==1.4.0时会失败）
4. opencv env: $env:path = "D:\workspace\deep_learning\mmdeploy_yolox\opencv\build;" + $env:path


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

转换命令：


```

python `
D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy/tools/deploy.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
D:\workspace\deep_learning\mmdeploy_yolox/demo.jpg `
--work-dir D:\workspace\deep_learning\mmdeploy_yolox/work_dir_fp32 `
--dump-info `
--device cuda:0 `

python `
D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\mmdeploy/tools/deploy.py `
D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146/demo.jpg `
--work-dir D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146/work_dir_fp32 `
--dump-info `
--device cuda:0 `

```

fp16，耗时较长
```

python `
D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy/tools/deploy.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
D:\workspace\deep_learning\mmdeploy_yolox/demo.jpg `
--work-dir D:\workspace\deep_learning\mmdeploy_yolox/work_dir_fp16 `
--dump-info `
--device cuda:0 `

```

int8
```

python `
D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy/tools/deploy.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\configs\mmdet\detection\detection_tensorrt-int8_dynamic-320x320-1344x1344.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
D:\workspace\deep_learning\mmdeploy_yolox/demo.jpg `
--work-dir D:\workspace\deep_learning\mmdeploy_yolox/work_dir `
--dump-info `
--device cuda:0 `

```

测试引擎
```
python tools/test.py `
    E:\workspace\win10\lab_mmdeploy\mmdeploy/configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344.py `
    E:\workspace\win10\lab_mmdeploy\mmdetection/configs/mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py `
    --model E:\workspace\win10\lab_mmdeploy/work_dir_fp32/end2end.engine `
    --out out_cuda0.pkl `
    --device cuda:0 `

```

