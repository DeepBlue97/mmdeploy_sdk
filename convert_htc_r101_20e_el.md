
# ubuntu 3060 12g

fp32


```

python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
../mmdetection/work_dirs/htc_r101_fpn_20e_el/epoch_20.pth \
../mmdetection/work_dirs/htc_r101_fpn_20e_el/03AEL_2030E3EDFD_90_3_EL-KXD.png \
--work-dir work_dirs/htc_r101_fpn_20e_el_fp32 \
--dump-info \
--device cuda:0 \

```

4-16batch
```
python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit_4-16batch.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
../mmdetection/work_dirs/htc_r101_fpn_20e_el/epoch_20.pth \
../mmdetection/work_dirs/htc_r101_fpn_20e_el/03AEL_2030E3EDFD_90_3_EL-KXD.png \
--work-dir work_dirs/htc_r101_fpn_20e_el_4-16batch_fp32 \
--dump-info \
--device cuda:0 \
```

fp16
```
python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt-fp16_dynamic-320x320-1344x1344_8bit_4batch.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
../mmdetection/work_dirs/htc_r101_fpn_20e_el/epoch_20.pth \
../mmdetection/work_dirs/htc_r101_fpn_20e_el/03AEL_2030E3EDFD_90_3_EL-KXD.png \
--work-dir work_dirs/htc_r101_fpn_20e_el_4_16batch_fp16 \
--dump-info \
--device cuda:0 \
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
