2060s


lenet5 pubgpos

```

python `
tools/deploy.py `
configs/mmcls/classification_tensorrt_static-32x32.py `
../mmclassification/configs/lenet/lenet5_pubgpos.py `
../mmclassification\work_dirs\pubgpos/epoch_5.pth `
../dog32x32.png `
--work-dir work_dir_lenet5_pubgpos_fp32 `
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
