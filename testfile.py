import tkinter as tk
import pytesseract as pt
from PIL import Image
import cv2
import numpy as np

pt.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 이미지 파일 경로 설정
image_path = r'C:\Users\venus\Downloads\nut_test3.jpg'

custom_config = r'--oem 1 --psm 3'


try:
    image = Image.open(image_path)
    print("이미지를 성공적으로 열었습니다.")
except FileNotFoundError:
    print("이미지 파일을 찾을 수 없습니다. 경로를 확인하세요.")
    exit()

def preprocess_image(image):
    # 이미지를 numpy 배열로 변환
    img = np.array(image)

    # 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 가우시안 블러 적용
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 대비 조정 (CLAHE: Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    contrast = clahe.apply(blurred)

    # PIL 이미지로 다시 변환
    processed_image = Image.fromarray(contrast)
    return processed_image

# 이미지 전처리
processed_image = preprocess_image(image)

# 전처리된 이미지로 OCR 수행
try:
    text = pt.image_to_string(processed_image, lang='kor')
    if text.strip():  # 텍스트가 비어 있지 않은지 확인
        print("OCR 결과:")
        print(text)
    else:
        print("OCR 결과가 비어 있습니다.")
except Exception as e:
    print("OCR 수행 중 오류 발생:", e)