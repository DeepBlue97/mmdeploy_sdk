fp32 test success!

python tools/test.py `
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py `
../mmdetection/configs/htc/htc_r50_fpn_1x_el.py `
--model work_dirs/htc_r50_fpn_1x_el_fp32/end2end.engine `
--device cuda:0 `
--speed-test `
--show-dir work_dirs/htc_r50_fpn_1x_el_fp32/show `
--out work_dirs/htc_r50_fpn_1x_el_fp32/result.pickle `

python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r50_fpn_1x_el.py \
--model work_dirs/htc_r50_fpn_1x_el_fp32/end2end.engine \
--device cuda:0 \
--speed-test \
--show-dir work_dirs/htc_r50_fpn_1x_el_fp32/show \
--out work_dirs/htc_r50_fpn_1x_el_fp32/result.pickle \
