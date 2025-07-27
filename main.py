import cv2

# import the Haar cascade classifier model
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml") # type: ignore

# access computer's webcam 
webcam = cv2.VideoCapture(0)    # 0 = default camera


# helper function: detect faces and add bounding box to video frames
def detect_faces_video(vid):
    # greyscale for better processing
    greyscale_vid = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    # find faces
    faces = face_classifier.detectMultiScale(
        greyscale_vid,
        scaleFactor=1.1,
        minNeighbors=10,
        minSize=(40,40)
    )
    # cycle through each face, add bounding box
    for (x, y, h, w) in faces:
        cv2.putText(vid, "Face", (x, int( y - 20 )), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), cv2.LINE_AA)
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces
        

# loop to capture video from webcam, run capture through function, then display results to screen
while True:
    # read frames from video capture
    result, video_frame = webcam.read()
    # break if frame isn't read successfully
    if result is False:
        break
    
    # process frame
    faces = detect_faces_video(video_frame)
    
    # show results
    cv2.imshow("Face detection result", video_frame)
    
    # keyboard interrupt
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# release resources, close windows
webcam.release()
cv2.destroyAllWindows()
    
