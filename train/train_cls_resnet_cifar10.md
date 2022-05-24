2060s

```
单卡
python `
tools/train.py `
configs/resnet/resnet18_8xb16_cifar10.py `

tools/dist_train.sh `
configs/resnet/resnet18_8xb16_cifar10.py `
2 `
--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \

```

node 1

多卡：报错无权限
./tools/dist_train.sh \
configs/resnet/resnet18_8xb16_cifar10.py \
8 \
--cfg-options data.samples_per_gpu=10 data.workers_per_gpu=4 \
optimizer.lr=0.002 \

单卡
python \
./tools/train.py \
configs/resnet/resnet18_8xb16_cifar10.py \
--cfg-options data.samples_per_gpu=100 data.workers_per_gpu=4 \
