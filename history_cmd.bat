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
