import cv2

# Sélectionnez l'index de la caméra (0, 1, etc.). Ajustez-le si nécessaire.
CAMERA_INDEX = 0
cap = cv2.VideoCapture(CAMERA_INDEX)

if not cap.isOpened():
    print("Erreur : impossible d'ouvrir la caméra")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Affichage du flux en couleur
    cv2.imshow("Flux Obsbot", frame)

    # Quitter sur la touche 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
