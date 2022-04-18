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

fp32 test

python `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox\yolox_nano_8x8_300e_coco_person_only.py
--model E:\workspace\win10\lab_mmdeploy\work_dir_fp32\end2end.engine `
--out result_fp32.pickle
--show-dir show_dir_fp32
--device cuda:0


fp16 test

python `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox\yolox_nano_8x8_300e_coco_person_only.py
--model E:\workspace\win10\lab_mmdeploy\work_dir_fp16\end2end.engine `
--out result_fp16.pickle
--show-dir show_dir_fp16
--device cuda:0

int8 test

python `
E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt-int8_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox\yolox_nano_8x8_300e_coco_person_only.py
--model E:\workspace\win10\lab_mmdeploy\work_dir_int8\end2end.engine `
--out result_int8.pickle
--show-dir show_dir_int8
--device cuda:0
