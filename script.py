import base64
import json

IMAGE_NAME = 'image.jpg'
OUTPUT_FILE_NAME = 'image.json'
# Feature types: https://cloud.google.com/vision/docs/concepts#types_of_vision_api_requests
FEATURE_TYPE = 'LABEL_DETECTION'


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


def _output_payload(payload):
  with open(OUTPUT_FILE_NAME, 'w') as f:
    json.dump(payload, f, ensure_ascii=True)


with open(IMAGE_NAME, 'rb') as image_file:
    payload = _create_payload_for_image(image_file)
    _output_payload(payload)
