from mmdeploy.apis import inference_model

model_cfg = r'D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py'

# deploy_cfg = r'D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py'
# backend_files = [r'D:\workspace\deep_learning\mmdeploy_yolox\work_dir_fp16\end2end.engine']

deploy_cfg = r'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py'
backend_files = [r'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\work_dir_fp32\end2end.engine']

img = r'D:\workspace\deep_learning\mmdeploy_yolox_cu111_torch182_mmcv146\demo.jpg'
device = 'cuda:0'
result = inference_model(model_cfg, deploy_cfg, backend_files, img=img, device=device)

print(result)




