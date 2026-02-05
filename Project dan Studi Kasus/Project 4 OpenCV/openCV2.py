import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

if not cap.isOpened():
    print("Error: Kamera tidak terdeteksi!")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Tidak dapat membaca frame!")
        break

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)
    pixel_center_hsv = hsv_frame[cy, cx]
    hue_value = pixel_center_hsv[0]
    saturation_value = pixel_center_hsv[1]
    brightness_value = pixel_center_hsv[2]

    color = "UNDEFINED"
    if saturation_value > 50 and brightness_value > 50:
        if (hue_value >= 0 and hue_value <= 5) or (hue_value >= 170 and hue_value <= 179):
            color = "RED"
        elif hue_value >= 6 and hue_value <= 22:
            color = "ORANGE"
        elif hue_value >= 23 and hue_value <= 33:
            color = "YELLOW"
        elif hue_value >= 34 and hue_value <= 78:
            color = "GREEN"
        elif hue_value >= 79 and hue_value <= 131:
            color = "BLUE"
        elif hue_value >= 132 and hue_value <= 170:
            color = "VIOLET"

    cv2.putText(frame, f"Color: {color}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 255, 255), 3)

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()