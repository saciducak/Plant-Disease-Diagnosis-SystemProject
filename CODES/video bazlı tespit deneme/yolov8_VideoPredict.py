import cv2
from roboflow import Roboflow

rf = Roboflow(api_key="gGsQ42EvK9CktMAILWyO")
project = rf.workspace().project("domates_tespit")
model = project.version(1).model

job_id, signed_url, expire_time = model.predict_video(
    "DJI_0021.MP4",
    fps=5,
    prediction_type="batch-video",
)

results = model.poll_until_video_results(job_id)

# Videoyu aç
cap = cv2.VideoCapture("DJI_0021.MP4")

# Videoyu işleyin
while True:
    ret, frame = cap.read()
    if not ret:
        break

    # İşlenmiş sonuçları her bir kare üzerinde kullanın ve tahminleri çizin
    for prediction in results['frames']:
        # Tahminlerdeki her bir nesne için
        for obj in prediction['objects']:
            # Nesneyi kareye çizin
            x, y, w, h = obj['bbox']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(frame, obj['class'], (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Her kareyi ekranda gösterin
    cv2.imshow('Frame', frame)
    
    # Çıkış için q tuşuna basılmasını bekleyin
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
