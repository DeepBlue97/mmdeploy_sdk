# Overview of Profilers

- NVVP: Visual Profiler
- nvprof: the command-line profiler
- Nsight Systems: A system-wide perfomance analysis tool
- Nsight Compute: An interactive kernel profiler for CUDA applications

Note that Visual Profiler and nvprof will be deprecated in a future CUDA release
We strongly recommend you transfer to Nsight Systems and Nsight Compute.

# Nsight Systems

## Overview

System-wide application algorithm tuning
- Focus on the application's algorithm - a unique perspective
Locate optimization opportunities
- See gaps of unused CPU and GPU time
Balance your workload across multiple CPUs and GPUs
- CPU algorithms, utilization, and thread state
- GPU streams, kernels, memory transfers, etc
Support for Linux & Windows, x86-64 & Tegra. Host only for Mac

## Key Features

Compute
- CUDA API: kernel launch and execution correlation
- Libraries: cuBLAS, cuDNN, TensorRT
- OpenACC

Graphics
- Vulkan, OpenGL, DX11, DX12, DXR, V-sync

OS Thread state and CPU utilization, pthread, file I/O, etc.
User annotations API(NVTX)
