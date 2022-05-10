fp32 test success!

python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
--model work_dirs/htc_r101_fpn_20e_el_fp32/end2end.engine \
--out work_dirs/htc_r101_fpn_20e_el_fp32/result.pickle \
--device cuda:0 \
--show-dir work_dirs/htc_r101_fpn_20e_el_fp32/show \


python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
--model work_dirs/htc_r101_fpn_20e_el_fp32/end2end.engine \
--out work_dirs/htc_r101_fpn_20e_el_fp32/result.pickle \
--device cuda:0 \
--speed-test \
--log2file work_dirs/htc_r101_fpn_20e_el_fp32/result.log \
--show-dir work_dirs/htc_r101_fpn_20e_el_fp32/show \

python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit_4batch.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
--model work_dirs/htc_r101_fpn_20e_el_4batch_fp32/end2end.engine \
--out work_dirs/htc_r101_fpn_20e_el_4batch_fp32/result.pickle \
--device cuda:0 \
--speed-test \
--log2file work_dirs/htc_r101_fpn_20e_el_4batch_fp32/result.log \
--show-dir work_dirs/htc_r101_fpn_20e_el_4batch_fp32/show \

python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit_4-16batch.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
--model work_dirs/htc_r101_fpn_20e_el_4-16batch_fp32/end2end.engine \
--device cuda:0 \
--out work_dirs/htc_r101_fpn_20e_el_4-16batch_fp32/result.pickle \
--speed-test \
--log2file work_dirs/htc_r101_fpn_20e_el_4-16batch_fp32/result.log \
--show-dir work_dirs/htc_r101_fpn_20e_el_4-16batch_fp32/show \

fp16

python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt-fp16_dynamic-320x320-1344x1344_8bit_4batch.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
--model work_dirs/htc_r101_fpn_20e_el_4_16batch_fp16/end2end.engine \
--device cuda:0 \
--out work_dirs/htc_r101_fpn_20e_el_4_16batch_fp16/result.pickle \
--speed-test \
--log2file work_dirs/htc_r101_fpn_20e_el_4_16batch_fp16/result.log \
--show-dir work_dirs/htc_r101_fpn_20e_el_4_16batch_fp16/show \
