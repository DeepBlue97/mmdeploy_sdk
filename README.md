# mmdeploy_sdk
Integrate the MMDeploy and other tasks like MMDetection, MMClassification, etc.


How to support new model to deploy?

torch to onnx:

1. print ops of torch
2. find out which ops is not supported by torch.onnx.export method
3. 

## Successfully support HyperTaskCascade(HTC) onnx export and TensorRT infer

2022.4.26

- modify `mmdet/models/roi_heads/htc_roi_head.py` in mmdetection
1. add _mask_forward() function
2. use int type not tensor for shape of adaptive_avg_pool2d

- touch `mmdeploy/codebase/mmdet/models/roi_heads/htc_roi_head.py` and override `mmdet.models.roi_heads.htc_roi_head.HybridTaskCascadeRoIHead.simple_test` in mmdeploy

