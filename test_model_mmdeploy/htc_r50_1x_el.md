fp32 test success!

python tools/test.py \
configs/mmdet/instance-seg/instance-seg_tensorrt_dynamic-320x320-1344x1344_8bit.py \
../mmdetection/configs/htc/htc_r50_fpn_1x_el.py \
--model work_dirs/htc_r50_fpn_1x_el_fp32/end2end.engine \
--metrics bbox segm \
--show \
--device cuda:0 \
--log2file work_dirs/htc_r50_fpn_1x_el_fp32/test/result.log \
--speed-test \
--warmup 10 \
--show-dir work_dirs/htc_r50_fpn_1x_el_fp32/test/show \
--out work_dirs/htc_r50_fpn_1x_el_fp32/test/result.pickle \
--log-interval 100 \


 parser.add_argument('deploy_cfg', help='Deploy config path')
    parser.add_argument('model_cfg', help='Model config path')
    parser.add_argument(
        '--model', type=str, nargs='+', help='Input model files.')
    parser.add_argument('--out', help='output result file in pickle format')
    parser.add_argument(
        '--format-only',
        action='store_true',
        help='Format the output results without perform evaluation. It is'
        'useful when you want to format the result to a specific format and '
        'submit it to the test server')
    parser.add_argument(
        '--metrics',
        type=str,
        nargs='+',
        help='evaluation metrics, which depends on the codebase and the '
        'dataset, e.g., "bbox", "segm", "proposal" for COCO, and "mAP", '
        '"recall" for PASCAL VOC in mmdet; "accuracy", "precision", "recall", '
        '"f1_score", "support" for single label dataset, and "mAP", "CP", "CR"'
        ', "CF1", "OP", "OR", "OF1" for multi-label dataset in mmcls')
    parser.add_argument('--show', action='store_true', help='show results')
    parser.add_argument(
        '--show-dir', help='directory where painted images will be saved')
    parser.add_argument(
        '--device', help='device used for conversion', default='cpu')
    parser.add_argument(
        '--cfg-options',
        nargs='+',
        action=DictAction,
        help='override some settings in the used config, the key-value pair '
        'in xxx=yyy format will be merged into config file. If the value to '
        'be overwritten is a list, it should be like key="[a,b]" or key=a,b '
        'It also allows nested list/tuple values, e.g. key="[(a,b),(c,d)]" '
        'Note that the quotation marks are necessary and that no white space '
        'is allowed.')
    parser.add_argument(
        '--metric-options',
        nargs='+',
        action=DictAction,
        help='custom options for evaluation, the key-value pair in xxx=yyy '
        'format will be kwargs for dataset.evaluate() function')
    parser.add_argument(
        '--log2file',
        type=str,
        help='log evaluation results and speed to file',
        default=None)
    parser.add_argument(
        '--speed-test', action='store_true', help='activate speed test')
    parser.add_argument(
        '--warmup',
        type=int,
        help='warmup before counting inference elapse, require setting '
        'speed-test first',
        default=10)
    parser.add_argument(
        '--log-interval',
        type=int,
        help='the interval between each log, require setting '
        'speed-test first',
        default=100)