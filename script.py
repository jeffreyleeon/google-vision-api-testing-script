import base64
import json
import os
import requests

IMAGE_NAME = 'image.jpg'
# Feature types: https://cloud.google.com/vision/docs/concepts#types_of_vision_api_requests
FEATURE_TYPE = 'LABEL_DETECTION'

GOOGLE_VISION_API_CREDENTIAL = os.getenv('GOOGLE_VISION_API_CREDENTIAL', '')

def _get_encoded_image(image_file):
  return base64.b64encode(image_file.read())


def _create_payload_for_image(image_file):
  encoded_image = _get_encoded_image(image_file)
  payload = {
    'requests':[
      {
        'image':{
          'content': encoded_image
        },
        'features':[
          {
            'type': FEATURE_TYPE,
            'maxResults': 1
          }
        ]
      }
    ]
  }
  return payload


def _get_vision_api_url():
  if len(GOOGLE_VISION_API_CREDENTIAL):
    return 'https://vision.googleapis.com/v1/images:annotate?key={}'.format(GOOGLE_VISION_API_CREDENTIAL)
  else:
    return ''


def _analyse_image(payload):
  headers = {
    'content-type': 'application/json'
  }
  url = _get_vision_api_url()
  
  data = json.dumps(payload)
  res = requests.post(
    url=url,
    data=data,
    headers=headers
    )
  return res.text


with open(IMAGE_NAME, 'rb') as image_file:
  payload = _create_payload_for_image(image_file)
  result = _analyse_image(payload)
  print(result)

