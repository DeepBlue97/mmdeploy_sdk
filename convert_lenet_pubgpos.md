2060s


lenet5 mnist

```

python `
tools/deploy.py `
configs/mmcls/classification_tensorrt_static-32x32-8bit.py `
../mmclassification/configs/lenet/lenet5_mnist.py `
../mmclassification\work_dirs\mnist/epoch_5.pth `
../dog32x32_8bit.png `
--work-dir work_dir_lenet5_mnist_fp32 `
--dump-info `
--device cuda:0 `

```

lenet5 pubgpos

```

python `
tools/deploy.py `
configs/mmcls/classification_tensorrt_static-32x32.py `
../mmclassification/configs/lenet/lenet5_pubgpos.py `
../mmclassification/work_dirs/lenet5_pubgpos/epoch_46.pth `
../dog32x32.png `
--work-dir work_dir_lenet5_pubgpos_fp32 `
--dump-info `
--device cuda:0 `

```

DELL G15 not ok

```
python tools/deploy.py `
configs\mmcls\classification_tensorrt_static-32x32.py `
..\mmclassification\configs\lenet\lenet5_pubgpos.py `
..\mmclassification\work_dirs\pubgpos\latest.pth `
./demo.jpg `
--work-dir work_dir_lenet_pubgpos_fp32 `
--dump-info `
--device cuda:0 `
```
