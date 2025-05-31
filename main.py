import cv2
import mediapipe as mp
import numpy as np

# Initialisation
CAMERA_INDEX = 0
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(
    static_image_mode=False,       # détection en continu
    model_complexity=1,            # complexité moyenne (0 = lite, 1 = full)
    enable_segmentation=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(CAMERA_INDEX)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Conversion BGR → RGB pour MediaPipe
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Optionnel : rendre image non-écrasable pour accélérer
    image_rgb.flags.writeable = False

    results = pose.process(image_rgb)  # calcul des landmarks

    # Remettre l'image en écrasable
    image_rgb.flags.writeable = True
    image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

    if results.pose_landmarks:
        # Dessiner les landmarks sur l'image
        mp_drawing.draw_landmarks(
            image_bgr,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            mp_drawing.DrawingSpec(color=(0,255,0), thickness=2, circle_radius=2),
            mp_drawing.DrawingSpec(color=(255,0,0), thickness=2, circle_radius=2)
        )

    cv2.imshow("Pose Detection", image_bgr)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
pose.close()
