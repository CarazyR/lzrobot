#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
img=cv2.imread('image1.png',0)
cv2.imshow('image',img)
k=cv2.waitKey(0)
if k==27:    #等待 ESC 键
    cv2.destoryAllWindows()
elif k==ord('s'): #等待 's' 键来保存和退出
    cv2.imwrite('messigray.png',img)
    cv2.destoryAllWindows()
