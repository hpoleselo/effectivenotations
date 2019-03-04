import cv2
import numpy as np

# mouse callback function
def cb_draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # img, loc, n sei, cor (BGR), n sei
        cv2.circle(img,(x,y), 100,(255, 0, 0), -1)

# Create a black image and window to that image
img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

# Binding the mouse callback to the image we created
cv2.setMouseCallback('image', cb_draw_circle)

while(1):
    cv2.imshow('image',img)
    # q to quit, adjust
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
