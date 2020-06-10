import cv2

# Selecting the video device
cam = cv2.VideoCapture(0)

while True:
    # Fetching frames
    ret, frame = cam.read()

    # Showing frames in a window
    cv2.imshow('akhilesh', frame)

    # Exit by pressing 'q' key
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
