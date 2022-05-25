"""
Compare trt model with torch model relatively and absolutely.
"""
from infer.prepare_task_processor import get_task_processor

def compare_relative():

    pass


def compare_absolutely():

    pass

def main():
    input_shape, task_processor = get_task_processor()
    


# def get_task_processor(model_cfg: Union[str, mmcv.Config],
#          deploy_cfg: Union[str, mmcv.Config],
#          model: Union[str, Sequence[str], BaseTask],
#          img: Union[str, np.ndarray],
#          device: str,
#          backend: Optional[Backend] = None,
#          output_file: Optional[str] = None,
#          show_result: bool = False,
#          score_thr: float = 0.3,
#          ):
#     deploy_cfg, model_cfg = load_config(deploy_cfg, model_cfg)

#     from mmdeploy.apis.utils import build_task_processor
#     task_processor = build_task_processor(model_cfg, deploy_cfg, device)

#     input_shape = get_input_shape(deploy_cfg)
#     if backend is None:
#         backend = get_backend(deploy_cfg)

#     if isinstance(model, str):
#         model = [model]

#     if isinstance(model, (list, tuple)):
#         assert len(model) > 0, 'Model should have at least one element.'
#         assert all([isinstance(m, str) for m in model]), 'All elements in the \
#             list should be str'

#         if backend == Backend.PYTORCH:
#             model = task_processor.init_pytorch_model(model[0])
#         else:
#             model = task_processor.init_backend_model(model)

#     # model_inputs, _ = task_processor.create_input(img, input_shape)

#     # with torch.no_grad():
#     #     result = task_processor.run_inference(model, model_inputs)[0]

#     # task_processor.visualize(
#     #     image=img,
#     #     model=model,
#     #     result=result,
#     #     output_file=output_file,
#     #     window_name=backend.value,
#     #     show_result=show_result,
#     #     score_thr=score_thr,
#     # )
#     return input_shape, task_processor


