def capture_left():
    import cv2

    key = cv2. waitKey(1)
    webcam = cv2.VideoCapture(2)
    while True:
        try:
            check, frame = webcam.read()
            # print(check) #prints true as long as the webcam is running
            # print(frame) #prints matrix values of each framecd
            # cv2.imshow("Capturing", frame)
            # key = cv2.waitKey(1)
            cv2.imwrite(filename='images/left_side.jpg', img=frame)
            webcam.release()
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            break
        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break
