注意点：

1. windows 11 系统， vs2019 community版
2. 使用系统公用的（非conda安装）CUDA 11.1最新版
3. 使用 pip安装pytorch 1.8.2 即可，如果设置了pip镜像源则会有加速效果，  （1.8.0好像安装mmcv-full==1.4.0时会失败）
4. opencv env: $env:path = "D:\workspace\deep_learning\mmdeploy_yolox\opencv\build;" + $env:path
5. 2060s成功转换推理fp32; 3060失败，可能还不支持30系显卡


转换命令：

双2060S

mask rcnn

fp32 mmdeploy v4

```
python `
E:\workspace\win10\lab_mmdeploy_v4\mmdeploy/tools/deploy.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt_dynamic-320x320-1344x1344.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py `
E:\workspace\win10\lab_mmdeploy_v4\mmdetection\checkpoints\mask_rcnn_epoch_12.pth `
E:\workspace\win10\lab_mmdeploy_v4/demo.jpg `
--work-dir E:\workspace\win10\lab_mmdeploy_v4/work_dir_mask_rcnn_fp32 `
--dump-info `
--device cuda:0 `
```
