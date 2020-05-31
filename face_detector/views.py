from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import urllib
import json
import numpy as np
import cv2

# Create your views here.
@csrf_exempt
def detect(request):
    data = {"success": False}

    if request.method == 'POST':
        if request.FILES.get("image", None) is not None:
            image = _grab_image( stream=request.FILES["image"])
        
        else:
            url = request.POST.get("url", None)

            if url is None:
                data = {'error': "No url Provided"}
                return JsonResponse(data)

            image = _grab_image(url=url)
        data["success"] = True

    return JsonResponse(data)

def _grab_image(path=None, stream=None, url=None):
    print("Test")
    if path is not None:
        image = cv2.imread(path)
    else:
        if url is not None:
            resp = urllib.urlopen(url)
            data = resp.read()

        elif stream is not None:
            data = stream.read()
        image = np.asarray(bytearray(data), dtype='uint8')
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
    