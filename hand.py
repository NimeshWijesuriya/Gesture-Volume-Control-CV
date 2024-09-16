import cv2
import mediapipe as mp
import time
import handTrackingModule as htm

pTime = 0
cTime = 0
cap = cv2.VideoCapture(0)  # Capture video from the default camera
detector = htm.handDetector()

while True:
        success, img = cap.read()
        if not success:
            break
        
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])  # Print details of landmark with id 4 (e.g., thumb tip)
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)
        
        # Show the resulting image
        cv2.imshow("Image", img)

        # Exit when 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
cap.release()
cv2.destroyAllWindows()
