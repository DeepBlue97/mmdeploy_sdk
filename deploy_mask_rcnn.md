
转换命令：

双2060S

mask rcnn

fp32 mmdeploy v4

```
python `
E:\workspace\win10\lab_mmdeploy_v4\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\checkpoints\mask_rcnn_epoch_12.pth `
E:\workspace\win10\lab_mmdeploy_v4/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy_v4/work_dir_mask_rcnn_fp32 `
--dump-info `
--device cuda:0 `
```

fp16 mmdeploy v3

```
python `
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt-fp16_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\mask_rcnn_epoch_12.pth `
E:\workspace\win10\lab_mmdeploy/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir_mask_rcnn_fp16 `
--dump-info `
--device cuda:0 `
```

int8 mmdeploy v3

```
python `
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt-int8_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\mask_rcnn_epoch_12.pth `
E:\workspace\win10\lab_mmdeploy/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir_mask_rcnn_int8 `
--dump-info `
--device cuda:0 `
```