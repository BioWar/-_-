import numpy as np 
import cv2 as cv
import pytesseract

def get_image_text(path, lang='ukr'):
    img = cv.imread(path)
    resized = cv.resize(img, None, fx=2, fy=2, interpolation = cv.INTER_CUBIC)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.threshold(img, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)[1]
    kernel = np.ones((1, 1), np.uint8)
    img = cv.dilate(img, kernel, iterations=1)
    img = cv.erode(img, kernel, iterations=1)
    img = cv.GaussianBlur(img, (5, 5), 0)
    result = pytesseract.image_to_string(img, lang=lang)
    return result
