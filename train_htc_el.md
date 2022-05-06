2060s

python .\tools\train.py `
configs\htc\htc_r50_fpn_1x_el.py `
--cfg-options data.samples_per_gpu=1 data.workers_per_gpu=0 `
optimizer.lr=0.002 `


node 1

./tools/dist_train.sh \
configs/htc/htc_r50_fpn_1x_el.py \
8 \
--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \
