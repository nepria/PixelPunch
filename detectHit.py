from FindingBallons import*

def detectHit(img, bboxs):
    img = cropImage(img, 100)
    imgBallonList = splitBallons(img, bboxs)
    showBallons(imgBallonList)
    return img

def splitBallons(img, bboxs):

    imgBallonList = []
    for b in bboxs:
        x1,y1,x2,y2 = b[0], b[1], b[0]+b[2], b[1]+b[3]
        imgBallonList.append(img[y1:y2, x1:x2])  
    return imgBallonList

def showBallons(imgBallonList):
    for x, im in enumerate(imgBallonList):
        cv2.imshow(str(x), im)

def findBallInBallon(imgBallonList):
    img = imgBallonList[0]
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.GaussianBlur(img, (5, 5), 5, 0)

    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=20, maxRadius =60)
    if type(circles).__name__ != 'NoneType':
        circles = np.unit16(np.around(circles))
        for c in circles[0,:]:
            cv2.circle(img, (c[0], c[1], c[2], (255, 0, 255), 2))
    imgBallonList[0] = img
    return imgBallonList