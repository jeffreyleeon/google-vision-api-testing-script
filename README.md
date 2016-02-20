#Getting Started

## Enable Google Vision API
- Follow the [Getting Start doc of Google Cloud Vision API](https://cloud.google.com/vision/docs/getting-started) and enable API, billing and get credentials

## Create payload for image

- ```python script.py```, recognize image.jpg file and export payload to image.json
- TODO: Better support ```python script.py [input] [output]```

## Curl Google Vision API
- ```curl -v -k -s -H "Content-Type: application/json" https://vision.googleapis.com/v1/images:annotate?key=BROWSER_KEY --data-binary @REQUEST_FILENAME```
- TODO: Better curl itself in script...