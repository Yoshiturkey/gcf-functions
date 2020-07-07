import requests
import os
from google.cloud import vision

def hello_gcs(event, context):
    """Triggered by a change to a Cloud Storage bucket.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    file = event
    filename = file['name']
    bucket_name = os.environ.get('BUCKET_NAME')
    source = "gs://{}/{}".format(bucket_name, filename)
    
    client = vision.ImageAnnotatorClient()
    
    response = client.annotate_image({
        "image": { "source": {"image_uri": source}},
        "features": [{"type": vision.enums.Feature.Type.LABEL_DETECTION}]
    })
    
    print(response)
    
   
