

# ubuntu 3060 12g

#export PATH=/home/peter/Downloads/TensorRT-8.2.3.0/lib:$PATH
export CUDNN_DIR=/home/peter/Downloads/cuda
export LD_LIBRARY_PATH=$CUDNN_DIR/lib64:$LD_LIBRARY_PATH
export TENSORRT_DIR=/home/peter/Downloads/TensorRT-8.2.3.0
export LD_LIBRARY_PATH=$TENSORRT_DIR/lib:$LD_LIBRARY_PATH
export LD_LIBRARY_PATH=$TENSORRT_DIR/targets/x86_64-linux-gnu/lib:$LD_LIBRARY_PATH
# set env for onnxruntime
export ONNXRUNTIME_DIR=/home/peter/workspace/fork/onnxruntime-linux-x64-1.8.1
export LD_LIBRARY_PATH=$ONNXRUNTIME_DIR/lib:$LD_LIBRARY_PATH
