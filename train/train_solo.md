linux single gpu

python ./tools/train.py \
configs/solo/decoupled_solo_r50_fpn_3x_coco.py \
--cfg-options data.samples_per_gpu=1 data.workers_per_gpu=2 \


linux 2 gpus

./tools/dist_train.sh \
configs/solo/decoupled_solo_r50_fpn_3x_coco.py \
2 \
--cfg-options data.samples_per_gpu=1 data.workers_per_gpu=1 \


node 1

./tools/dist_train.sh \
configs/solo/solo_r50_fpn_1x_coco.py \
8 \
--cfg-options data.samples_per_gpu=8 data.workers_per_gpu=4 \
