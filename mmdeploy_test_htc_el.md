fp32 test success!

python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
--model work_dirs/htc_r101_fpn_20e_el_fp32/end2end.engine \
--out work_dirs/htc_r101_fpn_20e_el_fp32/result.pickle \
--device cuda:0 \
