#import the required libraries including OpenCV
import cv2
from codedeepai import writeVideo

vid = "football-video.mp4"
savePath = "./output.mp4"
capture = cv2.VideoCapture(vid)
# initialise write Video object. Notice since we do not have the video frame yet, we have not
#passed the same. Which means writer object will be created when we start saving.
vw = writeVideo(savePath, capture)

while(True):
	# Capture frame-by-frame
	ret, currentframe = capture.read()
	if currentframe is not None:
		#notice that we are passing the current frame now so video writer
		#object will be initiated when the writing begins. Also in this case
		#we start saving from 10 Seconds onwards until video complete
		saved = vw.save(currentframe, 10000,-1)
		if not saved :
			print ("Video not saved!")
		#display video stream
		cv2.imshow('frame',currentframe)
	else:
		break
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	
#clean up
vw.release()
cv2.destroyAllWindows()
