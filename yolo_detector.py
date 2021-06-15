import subprocess
import sys

if len(sys.argv) <= 1:
    print('Please pass one argument')
else:
    proc = subprocess.Popen("python ./yolov5/detect.py --source " + sys.argv[1] + " --weights ./training_results/weights/best.pt", stdout=subprocess.PIPE)
    out, err = proc.communicate()
    print(out, err, proc.returncode)