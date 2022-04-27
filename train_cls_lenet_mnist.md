2060s

```
单卡
python tools/train.py `
configs/lenet/lenet5_mnist.py `


--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \

```
