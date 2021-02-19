import pytesseract
import cv2
import math

def scanShape(filePath, shape):
  # Load file from original path
  img_cv2 = cv2.imread(filePath)
  img_rgb = cv2.cvtColor(img_cv2, cv2.COLOR_BGR2RGB)
  # extract specific portion of the image
  (min_x, min_y, max_x, max_y) = shape.vertices()
  min_x = math.floor(min_x)
  min_y = math.floor(min_y)
  max_x = math.ceil(max_x)
  max_y = math.ceil(max_y)
  img_shape = img_rgb[min_y:max_y, min_x:max_x]
  # process image shape with tesseract   
  result = pytesseract.image_to_string(img_shape).strip()
  shape.value = result
  # return scanned text
  return result 