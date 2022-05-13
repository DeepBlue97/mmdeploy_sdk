sudo sh -c 'echo 2 >/proc/sys/kernel/perf_event_paranoid'


/home/peter/miniconda3/envs/mmlab/bin/python /home/peter/workspace/fork/mmdeploy/tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r101_fpn_20e_el.py \
--model work_dirs/htc_r101_fpn_20e_el_fp32/end2end.engine \
--device cuda:0 \

