def save_left():
    import cv2
    from vehicle_detector import VehicleDetector
    # Load Veichle Detector
    vd = VehicleDetector()
    img = cv2.imread('images/left_side.jpg')

    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)
    for box in vehicle_boxes:
        x, y, w, h = box

        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 3)

        cv2.putText(img, "Vehicles: " + str(vehicle_count), (20, 50), 0, 2, (100, 200, 0), 3)
    cv2.imwrite('predictions/left_prediction.jpg', img)