import cv2
import pytesseract
from PIL import Image
import numpy as np

# img = cv2.imread('C:/Users/liuli/PycharmProjects/data_detail/2021home_e/quarter1/month1/2.PNG')
# img2gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# img2var = cv2.Laplacian(img2gray, cv2.CV_64F).var()
# cv2.namedWindow('GreyModeOpen', cv2.WINDOW_NORMAL)
# cv2.imshow('GreyModeOpen', img)
# cv2.waitKey(0)

# words = pytesseract.image_to_string(Image.open('./2021home_e/quarter1/month1/1.PNG'), lang='chi_sim')
# print(words)


def custom_blur_demo(image):
    kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], np.float32)  # 锐化
    dst = cv2.filter2D(image, -1, kernel=kernel)
    words = pytesseract.image_to_string(dst, lang='chi_sim')
    print(words)
    cv2.imshow("custom_blur_demo", dst)


src = cv2.imread("./2021home_e/quarter1/month1/1.PNG ")
cv2.namedWindow("input image", cv2.WINDOW_AUTOSIZE)
cv2.imshow("input image", src)
custom_blur_demo(src)
# words = pytesseract.image_to_string(Image.open(src), lang='chi_sim')

cv2.waitKey(0)
cv2.destroyAllWindows()
