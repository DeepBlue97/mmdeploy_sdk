conda install pytorch torchvision torchaudio cudatoolkit=11.1 -c pytorch-lts -c conda-forge

conda install pytorch torchvision torchaudio -c pytorch-lts -c conda-forge

pip install mmcv-full -f https://download.openmmlab.com/mmcv/dist/cu111/torch1.8/index.html

E:\workspace\win10\lab_mmdeploy\mmdeploy\build\csrc\backend_ops\tensorrt>"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6\bin\nvcc.exe" 
-gencode=arch=compute_52,code=\"sm_52,compute_52\" 
-gencode=arch=compute_60,code=\"sm_60,compute_60\" 
-gencode=arch=compute_61,code=\"sm_61,compute_61\" 
-gencode=arch=compute_70,code=\"sm_70,compute_70\" 
-gencode=arch=compute_72,code=\"sm_72,compute_72\" 
-gencode=arch=compute_75,code=\"sm_75,compute_75\" 
-gencode=arch=compute_80,code=\"sm_80,compute_80\" 
-gencode=arch=compute_86,code=\"sm_86,compute_86\" 
-gencode=arch=compute_52,code=\"sm_52,compute_52\" 
-gencode=arch=compute_60,code=\"sm_60,compute_60\" 
-gencode=arch=compute_61,code=\"sm_61,compute_61\" 
-gencode=arch=compute_70,code=\"sm_70,compute_70\" 
-gencode=arch=compute_72,code=\"sm_72,compute_72\" 
-gencode=arch=compute_75,code=\"sm_75,compute_75\" 
-gencode=arch=compute_80,code=\"sm_80,compute_80\" 
-gencode=arch=compute_86,code=\"sm_86,compute_86\" 
-gencode=arch=compute_52,code=\"sm_52,compute_52\" 
-gencode=arch=compute_60,code=\"sm_60,compute_60\" 
-gencode=arch=compute_61,code=\"sm_61,compute_61\" 
-gencode=arch=compute_70,code=\"sm_70,compute_70\" 
-gencode=arch=compute_72,code=\"sm_72,compute_72\" 
-gencode=arch=compute_75,code=\"sm_75,compute_75\" 
-gencode=arch=compute_80,code=\"sm_80,compute_80\" 
-gencode=arch=compute_86,code=\"sm_86,compute_86\" 
--use-local-env -ccbin "C:\Program Files\Microsoft Visual Studio\2022\Enterprise 
  \VC\Tools\MSVC\14.31.31103\bin\HostX64\x64" 
  -x cu   
  -IE:\workspace\win10\lab_mmdeploy\mmdeploy\csrc\backend_ops\tensorrt\common -I"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6\include" -IE:\softw 
  are\TensorRT8221\include -I\include -I"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.6\include"     --keep-dir x64\Debug  -maxrregcount=0  --machine 64 --compile -cudart static -std=c++17 -Xcompiler 
  ="/EHsc /wd4819,/wd4828 /wd4819,/wd4828 /wd4819,/wd4828 /wd4819,/wd4828 /wd4819,/wd4828 /wd4819,/wd4828 -Zi -Ob0" -g  -D_WINDOWS -DTHRUST_IGNORE_DEPRECATED_CPP_DIALECT=1 -D"CMAKE_INTDIR=\"Debug\"" -D_MBCS -D 
  WIN32 -D_WINDOWS -DTHRUST_IGNORE_DEPRECATED_CPP_DIALECT=1 -D"CMAKE_INTDIR=\"Debug\"" -Xcompiler "/EHsc /W3 /nologo /Od /Fdmmdeploy_tensorrt_ops_obj.dir\Debug\mmdeploy_tensorrt_ops_obj.pdb /FS /Zi /RTC1 /MDd  
  /GR" -o mmdeploy_tensorrt_ops_obj.dir\Debug\sortScoresPerImage.obj "E:\workspace\win10\lab_mmdeploy\mmdeploy\csrc\backend_ops\tensorrt\batched_nms\sortScoresPerImage.cu"

  
python \
E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py \
E:\workspace\win10\lab_mmdeploy\mmdeploy/configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344.py \
E:\workspace\win10\lab_mmdeploy\mmdetection/configs/mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py \
E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\mask_rcnn_r50_fpn_1x_coco_20200205-d4b0c5d6.pth \
E:\workspace\win10\lab_mmdeploy\mmdetection/demo/demo.jpg \
--work-dir E:\workspace\win10\lab_mmdeploy/work_dir \
--dump-info \
--device cuda:0 \

python  E:\workspace\win10\lab_mmdeploy\mmdeploy/tools/deploy.py  E:\workspace\win10\lab_mmdeploy\mmdeploy/configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344.py  E:\workspace\win10\lab_mmdeploy\mmdetection/configs/mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py  E:\workspace\win10\lab_mmdeploy\mmdetection\checkpoints\mask_rcnn_r50_fpn_1x_coco_20200205-d4b0c5d6.pth  E:\workspace\win10\lab_mmdeploy\mmdetection/demo/demo.jpg  --work-dir E:\workspace\win10\lab_mmdeploy/work_dir  --dump-info --device cuda:0 

# mmdeploy 评估
python tools/test.py `
    E:\workspace\win10\lab_mmdeploy\mmdeploy/configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344.py `
    E:\workspace\win10\lab_mmdeploy\mmdetection/configs/mask_rcnn/mask_rcnn_r50_fpn_1x_coco.py `
    --model E:\workspace\win10\lab_mmdeploy/work_dir/end2end.engine `
    --out out_cuda0.pkl `
    --device cuda:0 `


yolox nano coco person only
fp16
python tools/test.py `
    D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\configs\mmdet\detection\detection_tensorrt-fp16_dynamic-320x320-1344x1344.py `
    D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
    --out out_cuda0.pkl `
    --model D:\workspace\deep_learning\mmdeploy_yolox\work_dir_fp16\end2end.engine `
    --device cuda:0 `

yolox nano coco person only
fp32
python tools/test.py `
    D:\workspace\deep_learning\mmdeploy_yolox\mmdeploy\configs\mmdet\detection\detection_tensorrt_dynamic-320x320-1344x1344.py `
    D:\workspace\deep_learning\mmdeploy_yolox\mmdetection\configs\yolox/yolox_nano_8x8_300e_coco_person_only.py `
    --out out_cuda0.pkl `
    --model D:\workspace\deep_learning\mmdeploy_yolox\work_dir_fp32\end2end.engine `
    --device cuda:0 `


python tools/test.py `
  --work-dir
  --out
  --gpu-id


optional arguments:
  -h, --help            show this help message and exit
  --work-dir WORK_DIR   the directory to save the file containing evaluation metrics
  --out OUT             output result file in pickle format
  --fuse-conv-bn        Whether to fuse conv and bn, this will slightly increasethe inference speed
  --gpu-ids GPU_IDS [GPU_IDS ...]
                        (Deprecated, please use --gpu-id) ids of gpus to use (only applicable to non-distributed training)
  --gpu-id GPU_ID       id of gpu to use (only applicable to non-distributed testing)
  --format-only         Format the output results without perform evaluation. It isuseful when you want to format the result to a specific format and submit it to the test server
  --eval EVAL [EVAL ...]
                        evaluation metrics, which depends on the dataset, e.g., "bbox", "segm", "proposal" for COCO, and "mAP", "recall" for PASCAL VOC
  --show                show results
  --show-dir SHOW_DIR   directory where painted images will be saved
  --show-score-thr SHOW_SCORE_THR
                        score threshold (default: 0.3)
  --gpu-collect         whether to use gpu to collect results.
  --tmpdir TMPDIR       tmp directory used for collecting results from multiple workers, available when gpu-collect is not specified
  --cfg-options CFG_OPTIONS [CFG_OPTIONS ...]
                        override some settings in the used config, the key-value pair in xxx=yyy format will be merged into config file. If the value to be overwritten is a list, it should be like key="[a,b]" or key=a,b It also allows
                        nested list/tuple values, e.g. key="[(a,b),(c,d)]" Note that the quotation marks are necessary and that no white space is allowed.
  --options OPTIONS [OPTIONS ...]
                        custom options for evaluation, the key-value pair in xxx=yyy format will be kwargs for dataset.evaluate() function (deprecate), change to --eval-options instead.
  --eval-options EVAL_OPTIONS [EVAL_OPTIONS ...]
                        custom options for evaluation, the key-value pair in xxx=yyy format will be kwargs for dataset.evaluate() function
  --launcher {none,pytorch,slurm,mpi}
                        job launcher
  --local_rank LOCAL_RANK