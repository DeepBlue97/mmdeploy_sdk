python tools/test.py \
${DEPLOY_CFG} \
${MODEL_CFG} \
--model ${BACKEND_MODEL_FILES} \
[--out ${OUTPUT_PKL_FILE}] \
[--format-only] \
[--metrics ${METRICS}] \
[--show] \
[--show-dir ${OUTPUT_IMAGE_DIR}] \
[--show-score-thr ${SHOW_SCORE_THR}] \
--device ${DEVICE} \
[--cfg-options ${CFG_OPTIONS}] \
[--metric-options ${METRIC_OPTIONS}]
[--log2file work_dirs/output.txt]

ax double 2060s

fp32 test success!

python tools\test.py `
configs\mmdet\instance-seg\instance-seg_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py `
--model E:\workspace\win10\lab_mmdeploy_v4\work_dir_mask_rcnn_fp32\end2end.engine `
--out result_mask_rcnn_fp32.pickle `
--device cuda:0 `
