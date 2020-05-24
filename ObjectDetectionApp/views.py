from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import base64
import os
# Create your views here.

@csrf_exempt
def launch(request):
    return render(request, 'ObjectDetectionApp/index.html')

@csrf_exempt
def objectDetectionAlgo(request):
    imageData = request.POST['text']
    imageData = imageData.split(',')[1]

    with open('image.jpeg', "wb") as fh:
        fh.write(base64.b64decode(imageData))

    path = 'image.jpeg'
    objectDetectionAlgoInternal(path)

    return HttpResponse('Success', content_type="text/plain")

def objectDetectionAlgoInternal(path):
    from imageai.Detection import ObjectDetection
    import cv2

    data = cv2.imread(path)

    cv2.imwrite('imageTemp.jpeg', data)

    execution_path = os.getcwd()

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(execution_path, "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, "imageTemp.jpeg"),
                                                 output_image_path=os.path.join(execution_path, "imageNew.jpeg"))

    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"])

    return

def result(request):
    return render(request, 'ObjectDetectionApp/result.html')

@csrf_exempt
def getCode(request):
    with open("imageNew.jpeg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    os.remove('image.jpeg')  # deleting files
    os.remove('imageNew.jpeg')  # deleting files
    os.remove('imageTemp.jpeg')  # deleting files

    return HttpResponse(encoded_string, content_type="text/plain")