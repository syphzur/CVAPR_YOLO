## Requirements
---
- Install required vesion of [Python](https://www.python.org/) (3.8 or later).
- Clone this repository.
```shell
git clone https://github.com/syphzur/CVAPR_YOLO.git
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
## Transfer learning
---
- To use transfer learning modify the ```train.py``` script provided in YOLOv5 repository to freeze all backbone layers. 
```
freeze = ['model.%s.' % x for x in range(10)] 
```
- To train the network use modified script with proper path to dataset.yaml file.
```
python train.py --batch 48 --weights yolov5m.pt --data ../dataset.yaml --epochs 50 --cache --img 512
```
## Inference
---
- To run inference use provided ```detector.py``` script. It can be used with variety of sources: webcam (0 as parameter), image, video, directory or even a YouTube video.
```
python detector.py 'https://youtu.be/NUsoVlDFqZg'
python detector.py 0 #webcam
python detector.py 0 image.jpg
python detector.py 0 directiory_with_images
```
## Dataset
---
Dataset was downloaded from [Kaggle](https://www.kaggle.com/aditya276/face-mask-dataset-yolo-format) and modified to YOLOv5 format.
