
转换命令：

# 双2060S

htc: mmdeploy v0.4.0 did not support htc

fp32 mmdeploy v4

```
python `
E:/workspace\win10\lab_mmdeploy_v4\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\configs\htc\htc_r50_fpn_1x_coco.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\checkpoints\epoch_1_htc.pth `
E:\workspace\win10\lab_mmdeploy_v4/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy_v4/work_dir_htc_fp32 `
--dump-info `
--device cuda:0 `
```

fp32 v3

```
python `
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\htc\htc_r50_fpn_1x_coco.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\epoch_1_htc.pth `
E:\workspace\win10\lab_mmdeploy/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir_htc_fp32 `
--dump-info `
--device cuda:0 `
```

yolox

fp32
```
python `
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth `
E:\workspace\win10\lab_mmdeploy/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir_fp32 `
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

# DELL G15

fp32
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

# ubuntu 3060 12g

fp32 
```

python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344.py \
../mmdetection/configs/htc/htc_r50_fpn_1x_coco.py \
../mmdetection/work_dirs/htc_r50_fpn_1x_coco/latest.pth \
../mmdetection/data/coco/val2017/000000009769.jpg \
--work-dir work_dir_htc_r50_fpn_1x_coco_fp32 \
--dump-info \
--device cuda:0 \

```