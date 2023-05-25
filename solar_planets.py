import cv2
img=cv2.imread("solar-system.jpg")
cv2.putText(img, "Sol", (100,80), cv2.FONT_HERSHEY_COMPLEX, 2, (0,0,255))
cv2.putText(img, "Mercurio", (110,250), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,255))
cv2.putText(img, "Venus", (190,180), cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,255))
cv2.putText(img, "Tierra", (280,270), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,0,0))
cv2.putText(img, "Marte", (370,170), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0))
cv2.putText(img, "Jupiter", (530,350), cv2.FONT_HERSHEY_COMPLEX, 1.2, (255,255,255))
cv2.putText(img, "Saturno", (740,120), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,0))
cv2.putText(img, "Urano", (950,300), cv2.FONT_HERSHEY_COMPLEX, 0.9, (205,100,200))
cv2.putText(img, "Neptuno", (1100,150), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255))

cv2.imwrite("Solar_systemwithname.jpg",img)

cv2.imshow("mostrar imagen", img)

cv2.waitKey(0)