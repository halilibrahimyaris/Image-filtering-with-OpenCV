import cv2
import numpy as np

img = cv2.imread("Adsiz.jpg")
meanBlurKernel = np.ones((3, 3), np.float32)/9
meanBlur = cv2.filter2D(src=img, kernel=meanBlurKernel, ddepth=-1)
horizontalStack = np.concatenate((img,meanBlur), axis=1)

cv2.imwrite("Output.jpg", horizontalStack)
cv2.imshow("OpencvOdev", horizontalStack)

cv2.waitKey(0)

cv2.destroyAllWindows()