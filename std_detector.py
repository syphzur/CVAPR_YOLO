import torch
import sys
import os.path
import filetype

if len(sys.argv) <= 1:
    print('Please pass image path as first argument')
else:
    # Image
    img_path = os.path.join(os.getcwd(), sys.argv[1])

    if os.path.exists(img_path):
        if not filetype.is_image(img_path):
            print(f"{img_path} is not a valid path")
        else: 
            # Model
            model = torch.hub.load('ultralytics/yolov5', 'custom', './training_results/weights/best.pt')
            # Inference
            results = model(img_path)
            # Results
            results.show()
    else:
        print('Please pass image path as first argument')
