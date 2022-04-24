

转换命令：

双2060S

lenet: have not deploy convert, it seems pointless

fp32 
```
python `
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmcls\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmclassification\configs\lenet/lenet_mnist.py `
E:\workspace\win10\lab_mmdeploy\mmclassification\work_dirs\mnist\latest.pth `
E:\workspace\win10\lab_mmdeploy/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir_lenet_fp32 `
--dump-info `
--device cuda:0 `
```

yolox

fp32
```
python `
E:\workspace\win10\lab_mmdeploy_v4\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
E:\workspace\win10\lab_mmdeploy_v4/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy_v4/work_dir_fp32 `
--dump-info `
--device cuda:0 `
```
fp16
```
python `
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
E:\workspace\win10\lab_mmdeploy/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir_fp16 `
--dump-info `
--device cuda:0 `
```

int8  校准数据集默认为验证集
```
python `
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt-int8_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
E:\workspace\win10\lab_mmdeploy/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir_int8 `
--dump-info `
--device cuda:0 `
```

DELL G15

yolox_tiny_8x8_300e_coco_person_only fp32 
```
python `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdeploy/tools/deploy.py `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdetection\configs\yolox/yolox_tiny_8x8_300e_coco_person_only.py `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdetection\checkpoints\yolox_tiny_coco_person_only_299e.pth `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3/demo.jpg `
--work-dir D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3/work_dir_yolox_tiny_person_only_fp32 `
--dump-info `
--device cuda:0 `
```
yolox_large_8x8_300e_coco_person_only fp32 
```
python `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdeploy/tools/deploy.py `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdetection\configs\yolox/yolox_l_8x8_300e_coco_person_only.py `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3\mmdetection\checkpoints\yolox_large_coco_person_only_e296.pth `
D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3/demo.jpg `
--work-dir D:\workspace\deep_learning\lab_mmdeploy_condatorch_v3/work_dir_yolox_large_person_only_fp32 `
--dump-info `
--device cuda:0 `
```


fp32 mmdeploy_yolox_cu111_torch182_mmcv146
```
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

