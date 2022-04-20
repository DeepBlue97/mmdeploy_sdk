import time

import torch
from mmdeploy.apis import build_task_processor
from mmdeploy.utils import get_input_shape, load_config

"""
infer more faster then "from mmdeploy.apis import inference_model"
"""

# FP16  successful with: win10 2060s torch182 mmcv146 mmdet2.22.0-peter_custom
model_cfg = r'E:\workspace\win10\lab_mmdeploy_v4\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py'
deploy_cfg = r'E:\workspace\win10\lab_mmdeploy_v4\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py'
device = 'cuda:0'
backend_files = [r'E:\workspace\win10\lab_mmdeploy_v4\work_dir_fp32\end2end.engine']
img = r'E:\workspace\win10\lab_mmdeploy_v4\demo.jpg'

print('start load config ...')
deploy_cfg, model_cfg = load_config(deploy_cfg, model_cfg)

print('start build engine ...')
task_processor = build_task_processor(model_cfg, deploy_cfg, device)
model = task_processor.init_backend_model(backend_files)

input_shape = get_input_shape(deploy_cfg)

model_inputs, _ = task_processor.create_input(img, input_shape)

print('start infer ...')
with torch.no_grad():

    t1 = time.time()
    img_num = 100
    for i in range(img_num):

        result = task_processor.run_inference(model, model_inputs)
    print(img_num / (time.time()-t1), ': img/s')

# print(result)
print('finish infer')