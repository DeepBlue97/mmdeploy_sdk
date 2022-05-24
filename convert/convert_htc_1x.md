
转换命令：

# 双2060S

htc: mmdeploy v0.4.0 did not support htc

fp32

win32:
```
python `
tools/deploy.py `
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py `
../mmdetection/configs/htc/htc_r50_fpn_1x_el.py `
../mmdetection/work_dirs/htc_r50_fpn_1x_el/latest.pth `
../mmdetection/data/el/train2017/01Aap_EL_20109BECAE_90_3_EL-KXD.png `
--work-dir work_dirs/htc_r50_fpn_1x_el_fp32 `
--dump-info `
--device cuda:0 `
```

linux:
```
python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r50_fpn_1x_el.py \
../mmdetection/work_dirs/htc_r50_fpn_1x_el/latest.pth \
../mmdetection/data/el/train2017/01Aap_EL_20109BECAE_90_3_EL-KXD.png \
--work-dir work_dirs/htc_r50_fpn_1x_el_fp32 \
--dump-info \
--device cuda:0 \
```