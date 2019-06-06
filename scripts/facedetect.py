import cv2
import matplotlib.pyplot as plt
import numpy as np
cap = cv2.VideoCapture(0)
i = 0
template = cv2.imread('/home/crazyr/catkin_ws/src/lzrobot/scripts/test1.jpg',0)
print template.shape
w, h = template.shape[::-1]
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

while(1):
    ret, frame = cap.read()
    img_gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow("capture",img_gray)
    for meth in methods:
        method = eval(meth)
        res = cv2.matchTemplate(img_gray, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        a= str(max_val)
        if a>str(140):
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:               
                top_left = max_loc
                bottom_right = (top_left[0] + w, top_left[1] + h)
                cv2.rectangle(img_gray, top_left, bottom_right, 255, 2)       
                plt.imshow(img_gray, cmap='gray')
                a=str(a)
                plt.title('Access Admitted'), plt.xticks([]), plt.yticks([])         
                plt.show()
                break
    if cv2.waitKey(1) &0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
