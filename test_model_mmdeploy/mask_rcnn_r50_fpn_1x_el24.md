
python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-520x520-568x568.py \
../mmdetection/configs/mask_rcnn/mask_rcnn_r50_fpn_1x_el24.py \
--model work_dirs/mask_rcnn_r50_fpn_1x_el24_fp32/end2end.engine \
--metrics bbox segm \
--show \
--device cuda:0 \
--log2file work_dirs/mask_rcnn_r50_fpn_1x_el24_fp32/test/result.log \
--speed-test \
--warmup 10 \
--show-dir work_dirs/mask_rcnn_r50_fpn_1x_el24_fp32/test/show \
--out work_dirs/mask_rcnn_r50_fpn_1x_el24_fp32/test/result.pickle \
--log-interval 100 \
