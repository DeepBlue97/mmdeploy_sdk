

ubuntu 3060 12g

cascade_mask_rcnn_r50_fpn_1x_coco
```
python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344.py \
/home/peter/workspace/fork/mmdetection/configs/cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco.py \
/home/peter/workspace/fork/mmdetection/work_dirs/cascade_mask_rcnn_r50_fpn_1x_coco/latest.pth \
/home/peter/workspace/fork/mmdetection/data/coco/val2017/000000009769.jpg \
--work-dir work_dir_cascade_mask_rcnn_r50_fpn_1x_coco_fp32 \
--dump-info \
--device cuda:0 \

```

