
htc: mmdeploy v0.4.0 did not support htc

fp32

linux:
```
python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344.py \
../mmdetection/configs/solo/decoupled_solo_r50_fpn_3x_coco.py \
../mmdetection/work_dirs/decoupled_solo_r50_fpn_3x_coco/epoch_1.pth \
../mmdetection/data/coco/test2017/000000581429.jpg \
--work-dir work_dirs/decoupled_solo_r50_fpn_3x_coco_fp32 \
--dump-info \
--device cuda:0 \
```
