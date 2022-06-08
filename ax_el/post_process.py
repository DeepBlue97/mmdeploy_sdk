"""

Convert result of AI model to rule condition.

"""


def convert_rcnn_result_to_el_rule_condition(result: list):
    """
    Convert result of rcnn series, which contains bbox and masks to rule condition.

    Args:
        result: list, which has two elements. Element 0 contains bbox and confidence; element 1 contains masks. Both
            of them were sorted by category index.

    Returns:
        defects: list, list of defect.
            defect: dict, rule condition for rule engine.
                category: str, category name, e.g. DS.
                area: float, area of defect, which unit is pixel^2.
                length: float, length of defect, which unit is pixel.
                grayscale: float, which range is [0, 100], and 0 is white while 100 is black.
                image_shape: tuple, height and width of image, e.g. (520, 520).

    """
    defects = []

    bboxs = result[0]
    masks = result[1]


    category = None
    area = None
    length = None
    grayscale = None
    image_shape = None

    defect = {
        "category": category,
        "area": area,
        "length": length,
        "grayscale": grayscale,
        "image_shape": image_shape,
    }
    defects.append(defect)

    return defects
