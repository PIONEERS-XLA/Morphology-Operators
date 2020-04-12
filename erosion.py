import cv2
import numpy as np

input_image = cv2.imread('./assets/img/j.png', cv2.IMREAD_GRAYSCALE)
se = cv2.imread('./assets/img/se2.png', cv2.IMREAD_GRAYSCALE)
print(input_image.shape)
for i in range(se.shape[0]):
    for j in range(se.shape[1]):
        if se[i, j] > 0:
            se[i, j] = 255

cv2.imshow('original', input_image)
cv2.waitKey(0)

def _erosion(inp, se):
    out = np.ones(inp.shape, dtype=inp.dtype)
    for i1 in range(inp.shape[0]):
        for j1 in range(inp.shape[1]):
            flag = 0
            for i2 in range(se.shape[0]):
                for j2 in range(se.shape[1]):

                    if se[i2, j2] != 0:
                        if i1 + i2 < inp.shape[0] and j1+j2 < inp.shape[1]:
                            if inp[i1 + i2, j1 + j2] == 0:
                                out[i1, j1] = 0
                                flag = 1
                                break
                if flag == 1:
                    break
            if flag == 0:
                out[i1, j1] = 255
    return out

out = _erosion(input_image, se)
cv2.imshow('k', out)
cv2.waitKey(0)


