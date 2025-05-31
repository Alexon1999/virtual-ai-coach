# virtual-ai-coach

un système de suivi d’exercices avec votre webcam:

1. Capturer le flux vidéo de la caméra.

2. Estimer la posture (pose estimation) du corps humain en temps réel.

3. Définir pour chaque exercice (squat, fente, pompes, etc.) des critères quantitatifs (angles articulaires, positions relatives, phases de mouvement).

4. Détecter la transition entre phase excentrique et phase concentrique pour compter le nombre de répétitions.

5. Évaluer si la forme (le « form ») est correcte à chaque répétition, en comparant les angles et positions mesurés à des seuils définis.

6. Retourner un feedback visuel et/ou audio si l’exécution est incorrecte, ou afficher le décompte des répétitions réussies.

7. Enregistrer les données (nombre de reps, timestamps, taux de réussite) pour un suivi longitudinal.