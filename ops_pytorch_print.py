import imp
from mmdet.apis import init_detector


config = r'D:\workspace\fork\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py'
checkpoint = r'D:\workspace\fork\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth'

model = init_detector(config, checkpoint=None, device='cuda:0', cfg_options=None)

print(model)
