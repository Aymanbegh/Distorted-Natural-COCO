# from pycocotools.coco import COCO
from coco import COCO
from COCOevals import COCOevals
import argparse


def coco_eval(args):
    cocoGt = COCO(args.gt_json)
    cocoDt = cocoGt.loadRes(args.pred_json)
    cocoEval = COCOevals(cocoGt, cocoDt, args.eval_type)
    cocoEval.evaluate()
    cocoEval.accumulate()
    cocoEval.summarize()



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate segm/bbox/keypoints in COCO format.')
    parser.add_argument('gt_json', type=str, help="COCO format segmentation/detection/keypoints ground truth json file")
    parser.add_argument('pred_json', type=str, help="COCO format segmentation/detection/keypoints prediction json file")
    parser.add_argument('eval_type', type=str, choices=['segm', 'bbox', 'keypoints'], help="Evaluation type")
    args = parser.parse_args()
    # gt_json = "C:/Users/beghd/OneDrive/Bureau/Json file/coco_rain2017/annotations/instances_default.json"
    # pred_json = "./results/coco_results.json"
    # eval_type="bbox"
    # coco_eval(gt_json,pred_json,eval_type)
    coco_eval(args)
