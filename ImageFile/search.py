import pytesseract
from PIL import Image
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

# 이미지 파일 경로
image_path = 'path_to_your_image_file.jpg'

# 이미지 열기
image = Image.open(image_path)

# 이미지에서 텍스트 추출
extracted_text = pytesseract.image_to_string(image)

# 키워드 리스트
keywords = ["달걀", "우유", "밀", "콩", "땅콩"]

# 추출된 텍스트를 단어 리스트로 분리
words_in_text = extracted_text.split()

# 유사도 임계값 설정 (예: 80 이상인 경우를 유사한 단어로 간주)
similarity_threshold = 80

# 유사한 단어 찾기
found_keywords = set()
for keyword in keywords:
    # 각 키워드에 대해 가장 유사한 단어 찾기
    best_match = process.extractOne(keyword, words_in_text, scorer=fuzz.ratio)
    if best_match and best_match[1] >= similarity_threshold:
        found_keywords.add(keyword)

# 결과 출력
if found_keywords:
    print(f"Found keywords: {', '.join(found_keywords)}")
else:
    print("No keywords found.")
