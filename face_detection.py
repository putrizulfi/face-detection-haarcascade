import cv2

# Inisialisasi cascade classifier untuk deteksi wajah
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Inisialisasi video capture dari webcam
cap = cv2.VideoCapture(0)

# Inisialisasi variabel untuk menghitung wajah yang terdeteksi
face_count = 0

while True:
    # Baca frame dari video capture
    ret, frame = cap.read()

    # Konversi frame ke grayscale (diperlukan untuk deteksi wajah)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Deteksi wajah dalam frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # Gambar kotak di sekitar wajah yang terdeteksi
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    # Hitung jumlah wajah yang terdeteksi
    face_count = len(faces)

    # Tampilkan jumlah wajah yang terdeteksi
    cv2.putText(frame, f'Jumlah Wajah Terdeteksi: {face_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Tampilkan frame hasil dengan wajah yang terdeteksi
    cv2.imshow('Face Detection', frame)

    # Keluar dari loop jika tombol 'q' ditekan
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup video capture dan jendela tampilan
cap.release()
cv2.destroyAllWindows()
