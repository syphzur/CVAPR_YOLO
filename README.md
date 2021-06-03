## How to use prepared project
---
- Install required vesion of [Python](https://www.python.org/) (3.8 or later).
- Clone this repository.
```shell
https://github.com/syphzur/CVAPR_YOLO.git
cd ./CVAPR_YOLO
```
- Clone [YOLOv5](https://github.com/ultralytics/yolov5) repository.
```
git clone https://github.com/ultralytics/yolov5.git
cd ./yolov5
```
- Install required dependencies.
```
pip install -r requirements.txt
```
- To train network use script provided in YOLOv5 repository with proper path to dataset.yaml file.
```
python train.py --batch 24 --weights yolov5m.pt --data ../dataset.yaml --epochs 50 --cache --img 512
```
