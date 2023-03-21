import requests
import os

from django.core.files import File

OCR_API_TOKEN_HEADER=os.environ.get("OCR_API_TOKEN_HEADER")
OCR_API_ENDPOINT=os.environ.get("OCR_API_ENDPOINT")

def extract_text_via_ocr_service(file_obj: File=None):
    # get image
    data = {}
    if OCR_API_ENDPOINT is None:
        print(OCR_API_ENDPOINT)
        return data
    if OCR_API_TOKEN_HEADER is None:
        print(OCR_API_TOKEN_HEADER)
        return data
    if file_obj is None:
        print(file_obj)
        return data
    headers={
        "Authorization": f"Bearer {OCR_API_TOKEN_HEADER}"
    }
    # send image through HTTP POST

    # return dict
    with file_obj.open('rb') as f:
        r = requests.post(OCR_API_ENDPOINT, files={'file': f}, headers=headers)
        if r.status_code in range(200, 299):
            data = r.json()
    return data
