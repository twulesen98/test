import pytesseract
from PIL import Image
import cv2
 
img = cv2.imread("./app/jit.jpeg",cv2.IMREAD_COLOR)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
gray = cv2.bilateralFilter(gray, 11, 17, 17) 
text = pytesseract.image_to_string(gray, 'jpn')
print(text)
