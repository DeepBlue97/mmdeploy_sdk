"""

Entry file of el classification.

step1: prepare AI model and infer
step2: post process
step3: rule engine

"""
from argparse import ArgumentParser
import os

from mmdet.apis import inference_detector

import sys
print(sys.path)
sys.path.append("../")
from prepare_model import get_model
from mmdeploy_sdk.infer.prepare_task_processor import get_task_processor


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--model_cfg', help='model cfg',
                        default='configs/yolox/yolox_l_8x8_300e_coco_person_only.py')
    parser.add_argument('--deploy_cfg', help='model cfg',
                        default='../mmdeploy/configs/mmdet/detection/detection_tensorrt_dynamic-320x320-1344x1344.py')
    parser.add_argument('--use_trt', action='store_true', help='infer by TensorRT backend')
    parser.add_argument('--trt_engine', help='trt engine name',
                        default='../mmdeploy/work_dir_yolox_l_8x8_300e_coco_person_only/end2end.engine')
    parser.add_argument('--checkpoint', help='trt engine name',
                        default='./work_dirs/yolox_l_8x8_300e_coco_person_only/latest.pth')
    parser.add_argument('--thr', help='threshold value', default=0.7)
    parser.add_argument('--image_folders', help='image_folders')

    # parser.add_argument(
    #     '--device', default='cuda:0', help='Device used for inference')
    args = parser.parse_args()

    return args


def main():

    args = parse_args()

    model = get_model(
        config_file=args.model_cfg, 
        checkpoint_file=args.checkpoint
    )

    image_folders = [args.image_folders]
    for image_folder in image_folders:
        for image in os.listdir(image_folder):
            result = inference_detector(model, os.path.join(image_folder, image))
            print(result)


if __name__ == "__main__":
    main()
