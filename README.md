# Mnist_Classifier_WebIntegration
#  MNIST Digit Classifier Web App (Django + Keras)

This project is a web application that predicts handwritten digits (0–9) using a trained deep learning model on the MNIST dataset. It is built using **Django** for the web backend and TensorFlow/Keras for digit classification.
##  Features

- Upload a handwritten digit image (PNG/JPG)
- Preprocesses image to match MNIST format (28x28 grayscale)
- Uses a `.keras` trained model for prediction
- Displays predicted digit and class probabilities
- Clean and responsive web interface

---

 Tech Stack

- Frontend: HTML, CSS (custom styling)
- Backend: Django (Python)
- ML Model:TensorFlow/Keras (`Sequential` model trained on MNIST)
- Image Processing: Pillow, NumPy

---

#How It Works

1. **Upload Image:** User uploads a handwritten digit image.
2. **Preprocessing:** Image is resized to 28x28 pixels, converted to grayscale, normalized, and reshaped.
3. **Prediction:** The image is passed to the loaded `.keras` model.
4. **Output:** The predicted digit and probabilities for all classes are shown.

---
