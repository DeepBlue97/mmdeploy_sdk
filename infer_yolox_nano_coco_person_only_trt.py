from mmdeploy.apis import inference_model

model_cfg = r'D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py'

# DELL G15 FP32 FP16
# deploy_cfg = r'D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py'
# backend_files = [r'D:\workspace\deep_learning\mmdeploy_yolox\work_dir_fp16\end2end.engine']

# DELL G15 FP32
# deploy_cfg = r'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py'
# backend_files = [r'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\work_dir_fp32\end2end.engine']

# ax double 2060S 
# FP32  successful with: win10 2060s torch182 mmcv146 mmdet2.22.0-peter_custom
model_cfg = r'E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py'
deploy_cfg = r'E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py'
backend_files = [r'E:\workspace\win10\lab_mmdeploy\work_dir_fp32\end2end.engine']
# FP16  successful with: win10 2060s torch182 mmcv146 mmdet2.22.0-peter_custom
model_cfg = r'E:\workspace\win10\lab_mmdeploy\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py'
deploy_cfg = r'E:\workspace\win10\lab_mmdeploy\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py'
backend_files = [r'E:\workspace\win10\lab_mmdeploy\work_dir_fp16\end2end.engine']

img = r'E:\workspace\win10\lab_mmdeploy\demo.jpg'
device = 'cuda:0'
result = inference_model(model_cfg, deploy_cfg, backend_files, img=img, device=device)

print(result)




