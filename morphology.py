import cv2 as cv
import numpy as np

def dilation(X, B):
    result = np.full(X.shape, 255)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            if X[i][j] == 255: #Nếu pixel này màu trắng thì bỏ qua
                continue
            for m in range(B.shape[0]):
                for n in range(B.shape[1]):
                    if B[m][n] == 255:  #Nếu pixel này màu trắng thì bỏ qua
                        continue
                    p = (i + m, j + n)
                    # Nếu ra khỏi viền ảnh thì bỏ qua
                    if p[0] < 0 or p[1] < 0:
                        continue
                    if p[0] >= result.shape[0] or p[1] >= result.shape[1]:
                        continue
                    #gán vào kết quả
                    result[p[0]][p[1]] = 0
    return result

def erosion(X, B):
    result = np.full(X.shape, 255)
    for i in range(X.shape[0]):
        for j in range(X.shape[1]):
            check = False
            for m in range(B.shape[0]):
                for n in range(B.shape[1]):
                    if B[m][n] == 255:  #Nếu pixel này màu trắng thì bỏ qua
                        continue

                    pos = (i + m, j + n) #lưu giá trị p + b
                    # Nếu ra khỏi viền ảnh thì bỏ qua
                    if pos[0] < 0 or pos[1] < 0:
                        continue
                    if pos[0] >= result.shape[0] or pos[1] >= result.shape[1]:
                        continue
                    #gán vào kết quả
                    if X[pos[0]][pos[1]] != 0:
                        check = True
            if check:
                continue
            else:
                result[i][j] = 0
    return result


def opening(X, B):
    result = erosion(X, B)
    result = dilation(result, B)
    return result


def closing(X, B):
    result = dilation(X, B)
    result = erosion(result, B)
    return result

X = cv.imread('b.jpg', cv.IMREAD_GRAYSCALE)
ret, X = cv.threshold(X,120,255,cv.THRESH_BINARY)

#mảng B màu đen
B = np.array([[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

cv.imshow("input", X)
cv.waitKey(0)

#output = dilation(X, B)
#output = erosion(X, B)
output = closing(X, B)
cv.imwrite("out.jpg", output)

TMP = cv.imread('out.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('output', TMP)

cv.waitKey(0)