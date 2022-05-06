2060s

python .\tools\train.py `
configs\htc\htc_r50_fpn_1x_el.py `
--cfg-options data.samples_per_gpu=1 data.workers_per_gpu=0 `
optimizer.lr=0.002 `


node 1

resnet 50  单卡 ok

python ./tools/train.py \
configs/htc/htc_r50_fpn_1x_el.py \
--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \

resnet 50  ok

./tools/dist_train.sh \
configs/htc/htc_r50_fpn_1x_el.py \
8 \
--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \
opencv_num_threads=1 \


resnet 101  ok

./tools/dist_train.sh \
configs/htc/htc_r101_fpn_20e_el.py \
8 \
--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \

resnext 101   not ok

./tools/dist_train.sh \
configs/htc/htc_x101_64x4d_fpn_16x1_20e_el.py \
8 \
--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \