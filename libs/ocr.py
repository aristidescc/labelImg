import pytesseract
import cv2
import math
import os
import sys
import libs.utils

tesseract_cmd = 'tesseract'

if sys.platform=='win32':
  tesseract_cmd = 'tesseract.exe'
  
pytesseract.pytesseract.tesseract_cmd = os.path.join(libs.utils.base_path(), "tesseract", 'bin', tesseract_cmd)

if os.getenv("TESSERACT_CMD") is not None:
   pytesseract.pytesseract.tesseract_cmd = os.getenv("TESSERACT_CMD") 

def scanShape(filePath, shape):
  # Load file from original path
  img_cv2 = cv2.imread(filePath)
  img_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
  #gray = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2GRAY)
  #blur = cv2.GaussianBlur(gray, (9,9), 0)
  #thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,30)
  
  # extract specific portion of the image
  (min_x, min_y, max_x, max_y) = shape.vertices()
  min_x = math.floor(min_x)
  min_y = math.floor(min_y)
  max_x = math.ceil(max_x)
  max_y = math.ceil(max_y)
  img_shape = img_rgb[min_y:max_y, min_x:max_x]
  # process image shape with tesseract   
  custom_options = r'--psm 10 --psm 6 --oem 3'
  result = pytesseract.image_to_string(img_shape, lang='spa', config=custom_options).strip()
  shape.value = result
  # return scanned text
  return result 