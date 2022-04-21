import time
import os

os.environ['path'] = r'E:\workspace\win10\lab_mmdeploy\cuda\bin;' + os.environ['path']

import torch
from mmdeploy.apis import build_task_processor
from mmdeploy.utils import get_input_shape, load_config

"""
infer more faster then "from mmdeploy.apis import inference_model"
"""

# FP16  successful with: win10 2060s torch182 mmcv146 mmdet2.22.0-peter_custom
# model_cfg = r'E:\workspace\win10\lab_mmdeploy_v4\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py'
# deploy_cfg = r'E:\workspace\win10\lab_mmdeploy_v4\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt_dynamic-320x320-1344x1344.py'
model_cfg = r'E:\workspace\win10\lab_mmdeploy_v3\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py'
deploy_cfg = r'E:\workspace\win10\lab_mmdeploy_v3\mmdeploy\configs\mmdet\instance-seg\instance-seg_tensorrt_dynamic-320x320-1344x1344.py'
backend_files = [r'E:\workspace\win10\lab_mmdeploy\work_dir_mask_rcnn_fp32\end2end.engine']

img = r'E:\workspace\win10\lab_mmdeploy\el.png'
device = 'cuda:0'

deploy_cfg, model_cfg = load_config(deploy_cfg, model_cfg)

task_processor = build_task_processor(model_cfg, deploy_cfg, device)
model = task_processor.init_backend_model(backend_files)

input_shape = get_input_shape(deploy_cfg)

model_inputs, _ = task_processor.create_input(img, input_shape)

with torch.no_grad():

    t1 = time.time()
    img_num = 10
    print('start infer ...')
    for i in range(img_num):

        result = task_processor.run_inference(model, model_inputs)
    print(img_num / (time.time()-t1), ': img/s')

# print(result)
print('finish infer.')