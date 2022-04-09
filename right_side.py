def right():
    from count import counter
    from image_capture_right import capture_right
    from save_prediction_right import save_right

    import cv2
    from vehicle_detector import VehicleDetector

    capture_right()
    img ="images/right_side.jpg"

    c = counter(img)

    save_right()

    return c