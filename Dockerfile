# # Gunakan image Python sebagai dasar
# FROM python:3.8

# # Instal OpenCV dan libGL
# RUN pip install opencv-python-headless
# RUN apt-get update && apt-get install -y libgl1-mesa-glx

# # Salin kode Anda ke direktori /app di dalam container
# WORKDIR /app
# COPY face_detection.py /app/

# # Salin file haarcascade_frontalface_default.xml ke dalam direktori /app di dalam container
# COPY haarcascade_frontalface_default.xml /app/

# # Perintah yang akan dijalankan saat container dimulai
# CMD ["python", "face_detection.py"]

# Gunakan image Python sebagai dasar
FROM python:3.8

# Instal OpenCV dan libGL
RUN pip install opencv-python-headless
RUN apt-get update && apt-get install -y libgl1-mesa-glx

# Menyalin kode ke direktori /app di dalam container
WORKDIR /app
COPY upvideo.py /app/

# Menyalin file haarcascade_frontalface_default.xml ke dalam direktori /app di dalam container
COPY haarcascade_frontalface_default.xml /app/

# Perintah yang akan dijalankan saat container dimulai
CMD ["python", "upvideo.py"]
