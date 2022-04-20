# mmdeploy_sdk
Integrate the MMDeploy and other tasks like MMDetection, MMClassification, etc.


How to support new model to deploy?

torch to onnx:

1. print ops of torch
2. find out which ops is not supported by torch.onnx.export method
3. 