from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import json
import base64

from .image_processor import processor, face_drawer

class IndexView(TemplateView):
    template_name = 'index.html'


class UploadView(TemplateView):
    template_name = 'upload.html'


@csrf_exempt
def upload_reception(request):
    data = json.loads(request.body)
    data_url = data['screenshot']
 
    screenshot_bytes = base64.b64decode(data_url.split(',')[1])

    with open('screenshot.png', 'wb') as f:
        f.write(screenshot_bytes)
    
    face_drawer()

    film_actor = processor()

    print(film_actor)

    if film_actor is not None:

        with open("faces.png", "rb") as image_file:
            image_data = image_file.read()

            # Encode the image data as base64
            encoded_image = base64.b64encode(image_data).decode("utf-8")


        with open('data.json') as json_file:
            data = json.load(json_file)   
            for actor in data['actors']:
                if actor["name"] == film_actor:
                    response = {
                                "name":actor['real_name'],
                                "dob":actor['dob'],
                                "maritial_status":actor['maritial_status'],
                                "description":actor["description"],
                                "movies":actor["movies"],
                                "image":encoded_image

                    }
                
                    return JsonResponse(response, safe=False)


    else:
        return JsonResponse(None, safe=False)
    
    return JsonResponse(response, safe=False)








