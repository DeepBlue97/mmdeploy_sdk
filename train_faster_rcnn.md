python .\tools\train.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\faster_rcnn\faster_rcnn_r50_fpn_1x_coco.py `
--cfg-options data.samples_per_gpu=1 data.workers_per_gpu=1 `


linux 3060

python ./tools/train.py \
/home/peter/workspace/fork/mmdetection/configs/mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py \
--cfg-options data.samples_per_gpu=1 data.workers_per_gpu=1 \