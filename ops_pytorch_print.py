from mmdet.apis import init_detector


config = r'D:\workspace\fork\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py'
checkpoint = r'D:\workspace\fork\mmdetection\checkpoints\best_bbox_mAP_epoch_299.pth'

config = r'E:\workspace\win10\lab_mmdeploy\mmdetection\configs\mask_rcnn\mask_rcnn_r50_fpn_1x_coco.py'
checkpoint = r'E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\mask_rcnn_epoch_12.pth'

config = r'E:\workspace\win10\lab_mmdeploy\mmdetection\configs\htc\htc_r50_fpn_1x_coco.py'
checkpoint = r'E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\epoch_1_htc.pth'


model = init_detector(config, checkpoint=None, device='cuda:0', cfg_options=None)

print(model)
