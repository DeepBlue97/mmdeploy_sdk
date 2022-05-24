# 双2060S

resnet18 

fp32

```

python `
tools/deploy.py `
configs/mmcls/classification_tensorrt_static-32x32.py `
../mmclassification/configs/resnet/resnet18_8xb16_cifar10.py `
../mmclassification/work_dirs/resnet18_8xb16_cifar10/epoch_46.pth `
../dog32x32.png `
--work-dir work_dir_resnet18_8xb16_cifar10_fp32 `
--dump-info `
--device cuda:0 `

```
remenber add topk to model config:
topk = (1, 5)
