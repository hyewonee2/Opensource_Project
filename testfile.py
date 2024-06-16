<<<<<<< HEAD
print("this is a test file")
#test
=======
from PIL import Image
import numpy as np
import pytesseract

filename = 'sample3.png'
img = np.array(Image.open(filename))
text = pytesseract.image_to_string(img)
print(text)
>>>>>>> a3c6ead (first commit)
