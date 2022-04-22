
win32

python .\tools\train.py `
E:\workspace\win10\lab_mmdeploy\mmdetection\configs\cascade_rcnn\cascade_mask_rcnn_r50_fpn_1x_coco.py `
--cfg-options data.samples_per_gpu=1 data.workers_per_gpu=0 `

linux 3060

python ./tools/train.py \
/home/peter/workspace/fork/mmdetection/configs/cascade_rcnn/cascade_mask_rcnn_r50_fpn_1x_coco.py \
--cfg-options data.samples_per_gpu=2 data.workers_per_gpu=2 \
optimizer.lr=0.002 \

