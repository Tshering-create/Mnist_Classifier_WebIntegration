from django.shortcuts import render
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Load the saved MNIST model once
model = load_model('mnist_digit_classifier.keras')

# Preprocessing function
def preprocess_image(image):
    image = image.convert('L').resize((28, 28))  # Grayscale, resize
    img_array = np.array(image).astype('float32').reshape(1, 784) / 255.0

    return img_array

# Main view
def index(request):
    prediction = None
    probs = []

    if request.method == 'POST' and request.FILES.get('digit'):
        try:
            image = Image.open(request.FILES['digit'])
            processed = preprocess_image(image)
            result = model.predict(processed)[0]
            prediction = int(np.argmax(result))
            probs = result
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render(request, 'predictor/index.html', {
        'prediction': prediction,
        'probs': probs,
    })

