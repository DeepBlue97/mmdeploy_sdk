python \
tools/deploy.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-520x520-568x568.py \
../mmdetection/configs/mask_rcnn/mask_rcnn_r50_fpn_1x_el24.py \
../mmdetection/work_dirs/mask_rcnn_r50_fpn_1x_el24/latest.pth \
../mmdetection/data/el24/train2017/02Admxpy_qths_EL_20200F64FD_90_2_EL-KXD.png \
--work-dir work_dirs/mask_rcnn_r50_fpn_1x_el24_fp32 \
--dump-info \
--device cuda:0 \
