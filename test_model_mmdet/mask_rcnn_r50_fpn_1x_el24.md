
python tools/test.py \
configs/mask_rcnn/mask_rcnn_r50_fpn_1x_el24.py \
work_dirs/mask_rcnn_r50_fpn_1x_el24/latest.pth \
--work-dir work_dirs/mask_rcnn_r50_fpn_1x_el24/test/ \
--gpu-id 0 \
--eval bbox segm \
--show \
--show-score-thr 0.3 \
--tmpdir work_dirs/mask_rcnn_r50_fpn_1x_el24/test/tmp \
--show-dir work_dirs/mask_rcnn_r50_fpn_1x_el24/test/show/ \

