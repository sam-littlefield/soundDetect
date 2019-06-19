import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# Image we want to search
img_rgb = cv.imread('./ImageInImage/assets/imageWithCog.png')
# Make image grey to remove some variation
img_grey = cv.cvtColor(img_rgb, cv.COLOR_BGR2GRAY)
# Image we want to find
template = cv.imread('./ImageInImage/assets/cog.png',0)
# Match grey image to template
w, h = template.shape[::-1]
res = cv.matchTemplate(img_grey,template,cv.TM_CCOEFF_NORMED)
# Set rules for what counts as a match
threshold = 0.8
loc = np.where( res >= threshold)
# Draw red box around the item we think matches
for pt in zip(*loc[::-1]):
    cv.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
# Write image with red box to file
cv.imwrite('./ImageInImage/assets/foundCog.png',img_rgb)
