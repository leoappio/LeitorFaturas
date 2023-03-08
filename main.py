import pytesseract
import cv2
from pdf2image import convert_from_path


pdf_pages = convert_from_path('./pdf/faturaAbPlast.pdf',poppler_path=r'C:\\poppler-22.12.0\\Library\bin')

for i in range(len(pdf_pages)):
    pdf_pages[i].save('./images/page_'+str(i)+'.jpg', 'JPEG')

image = cv2.imread('./images/page_0.jpg')

cropped_image = image[150:950, 770:1700]

#cropped_image = cv2.imread('dados_faturamento_celesc.png')

#cv2.imshow("cropped", cropped_image)

#cv2.waitKey(0)
#cv2.destroyAllWindows()

config_tessaract = '--tessdata-dir tessdata --psm 11'

#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files\Tesseract-OCR\\tesseract.exe'
text = pytesseract.image_to_string(cropped_image, lang='por', config=config_tessaract)

print(text)