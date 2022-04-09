def left():
    from count import counter
    from image_capture_left import capture_left
    from save_prediction_left import save_left

    import cv2
    from vehicle_detector import VehicleDetector

    capture_left()
    img ="images/left_side.jpg"

    c = counter(img)

    save_left()
    return c

