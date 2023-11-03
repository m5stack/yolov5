# ENVIRONMENT INIT
```bash
pip install -r requirements.txt
```

# GET YOLOV5S WEIGHTS
```bash
mkdir weights
wget -P weights https://github.com/ultralytics/yolov5/releases/download/v6.2/yolov5s.pt
```

# DOWN DATASETS
```bash
mkdir -p datasets/rubbish
wget -P datasets https://github.com/Abandon-ht/coco_rubbish_dataset/archive/refs/heads/main.zip
unzip -d datasets/rubbish datasets/coco_rubbish_dataset-main.zip
```

# TRAIN
```bash
# train
python train.py --data data/rubbish.yaml --cfg models/yolov5s.yaml --weights weights/yolov5s.pt --batch-size -1 --epoch 20

# detect
python detect.py --source datasets/rubbish/images/IMG_20210311_213716.jpg --weights ./runs/train/exp/weights/best.pt
```

# EXPORT ONNX MODULE
```bash
python export.py --include onnx --opset 11 --weights ./runs/train/exp/weights/best.pt ax620
```

will be save onnx module in ./runs/train/exp/weights/best.onnx.

over!