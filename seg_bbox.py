import cv2
import numpy as np


seg_mask = cv2.imread("20231214-162339_cloth_masked.png")
print(seg_mask.shape)
segmented = np.where(seg_mask == 0)

bbox = 0,0,0,0

print(len(segmented[0]))
x_min = int(np.min(segmented[1]))
x_max = int(np.max(segmented[1]))
y_min = int(np.min(segmented[0]))
y_max = int(np.max(segmented[0]))

bbox = x_min, x_max, y_min, y_max
print(bbox)
og_img = cv2.imread("20231214-162337org_img.png")
clth = og_img[y_min:y_max, x_min:x_max]
