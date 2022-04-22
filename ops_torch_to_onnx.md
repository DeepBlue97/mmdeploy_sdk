| Description | pytorch             | onnx     |
| ---------   | ------------------- | ------------------- |
| Index       | [n]                 | Gather   |
| Concat      | torch.cat()         | Concat   |
| Squeeze     | torch.squeeze()     | squeeze  |
| RNN         |                     | Gemm     |
| Slice       |  [:4]               | Slice    |
| Cast        |  tensor.float()     | Cast     |
| Repeat      |  [:4]               | ConstantOfShape->Expand    |
