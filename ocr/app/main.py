from typing import Optional

from fastapi import FastAPI
import uvicorn


app = FastAPI()

import pytesseract
from PIL import Image
import cv2
 
 
img = cv2.imread("./app/jit.jpeg",cv2.IMREAD_COLOR)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.bilateralFilter(gray, 11, 17, 17) 
 
text = pytesseract.image_to_string(gray, 'jpn')


@app.get("/")
def read_root():
    return {"TWU LE SEN A18MJ0158": text}

if __name__ == '__main__':
	uvicorn.run(app, port=8000, host="0.0.0.0")
