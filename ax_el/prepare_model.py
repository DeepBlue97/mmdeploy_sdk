from mmdet.apis import init_detector


def get_model(config_file: str, checkpoint_file: str):
    """
    build the model from a config file and a checkpoint file

    Args:
        config_file:
        checkpoint_file:

    Returns:

    """
    model = init_detector(config_file, checkpoint_file, device='cuda:0')

    return model
