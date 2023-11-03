#!/bin/env python3
import torch
import sys

def main(file):
    weights = file
    model = torch.load(str(weights[0] if isinstance(weights, list) else weights), map_location='cpu')
    model1 = model['ema' if model.get('ema') else 'model']
    model2 = model1.float().fuse().model.state_dict()

    for k,v in model2.items():
        if 'anchor' in k:
            print(v.numpy().flatten().tolist())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("python ./export_anchors.py yolov5s_weights_file")
    main(sys.argv[1])