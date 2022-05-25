from typing import Optional, Sequence, Union

import torch
import numpy as np
import mmcv

from mmdeploy.codebase import BaseTask
from mmdeploy.utils import Backend, get_backend, get_input_shape, load_config


def get_task_processor(model_cfg: Union[str, mmcv.Config],
                       deploy_cfg: Union[str, mmcv.Config],
                       model: Union[str, Sequence[str], BaseTask],
                       device: str,
                       backend: Optional[Backend] = None,
                       ):
    deploy_cfg, model_cfg = load_config(deploy_cfg, model_cfg)

    from mmdeploy.apis.utils import build_task_processor
    task_processor = build_task_processor(model_cfg, deploy_cfg, device)

    input_shape = get_input_shape(deploy_cfg)
    if backend is None:
        backend = get_backend(deploy_cfg)

    if isinstance(model, str):
        model = [model]

    if isinstance(model, (list, tuple)):
        assert len(model) > 0, 'Model should have at least one element.'
        assert all([isinstance(m, str) for m in model]), 'All elements in the \
            list should be str'

        if backend == Backend.PYTORCH:
            model = task_processor.init_pytorch_model(model[0])
        else:
            model = task_processor.init_backend_model(model)

    return input_shape, task_processor
