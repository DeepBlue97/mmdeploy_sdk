import time

import numpy as np
import torch
from mmdeploy.apis import build_task_processor
from mmdeploy.utils import get_input_shape, load_config
from mmdet.apis import inference_detector, init_detector

"""
infer more faster then "from mmdeploy.apis import inference_model"
"""

# FP16  successful with: win10 2060s torch182 mmcv146 mmdet2.22.0-peter_custom
model_cfg = 'mmdetection/configs/htc/htc_r50_fpn_1x_el.py'
deploy_cfg = 'mmdeploy/configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py'
device = 'cuda:0'
backend_files = ['mmdeploy/work_dirs/htc_r50_fpn_1x_el_fp32/end2end.engine']
checkpoint = 'mmdetection/work_dirs/htc_r50_fpn_1x_el/latest.pth'
img = 'mmdeploy/data/el/train2017/01Aap_EL_20109BECAE_90_3_EL-KXD.png'


# pytorch backend
model_torch = init_detector(model_cfg, checkpoint, device='cuda:0')


print('start load config ...')
deploy_cfg, model_cfg = load_config(deploy_cfg, model_cfg)

print('start build engine ...')
task_processor = build_task_processor(model_cfg, deploy_cfg, device)
model = task_processor.init_backend_model(backend_files)

input_shape = get_input_shape(deploy_cfg)

model_inputs, _ = task_processor.create_input(img, input_shape)

print('start infer ...')
with torch.no_grad():

    result = task_processor.run_inference(model, model_inputs)[0]
    # print(result) # [[43个], [43个]]
    result_torch = inference_detector(model_torch, img)

    # del bbox which Confidence < 0.01
    result_del_bbox_count = 0
    for cls_idx, cls in enumerate(result[0]):
        if len(cls):
            for bbox_idx, bbox in enumerate(cls):
                if bbox[4] < 0.01:  # 置信度大于0.01才参与计算
                    np.delete(result[0][cls_idx], bbox_idx)
                    # result[0][cls_idx].remove(bbox)
                    result_del_bbox_count += 1

    result_torch_del_bbox_count = 0
    for cls_idx, cls in enumerate(result_torch[0]):
        if len(cls):
            for bbox_idx, bbox in enumerate(cls):
                if bbox[4] < 0.01:  # 置信度大于0.01才参与计算
                    np.delete(result_torch[0][cls_idx], bbox_idx)
                    # result_torch[0][cls_idx].remove(bbox)
                    result_torch_del_bbox_count += 1

    print("result_del_bbox_count: ", result_del_bbox_count)
    print("result_torch_del_bbox_count: ", result_torch_del_bbox_count)
    
    for cls_idx, cls in enumerate(result[0]):
        if len(cls):
            for bbox_idx, bbox in enumerate(cls):
                if bbox[4] > 0.01:  # 置信度大于0.01才参与计算
                    print(bbox-result_torch[0][cls_idx][bbox_idx])

print('finish infer')

result_sub = []
