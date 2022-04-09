
def counter(img):
    import cv2
    import numpy as np
    from vehicle_detector import VehicleDetector
    vd = VehicleDetector()

    img = cv2.imread(img)
    vehicle_boxes = vd.detect_vehicles(img)
    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

    vehicle_count = len(vehicle_boxes)

    return vehicle_count

