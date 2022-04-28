
双2060S

fp32 
```
python tools/deploy.py `
configs/mmdet/detection/detection_tensorrt_dynamic-320x320-1344x1344.py `
../mmdetection/configs/yolox/yolox_l_8x8_300e_coco_person_only.py `
../mmdetection/work_dirs/yolox_l_8x8_300e_coco_person_only/best_bbox_mAP_epoch_296_large.pth `
../mmdetection/demo/person.jpg `
--work-dir work_dir_yolox_l_8x8_300e_coco_person_only `
--dump-info `
--device cuda:0 `
```
