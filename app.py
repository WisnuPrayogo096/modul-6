from flask import Flask, request, render_template, jsonify
import tensorflow as tf
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import io
from datetime import datetime
import time

app = Flask(__name__)

# Load the pre-trained models
model_cnn = load_model('models/model_cnn.h5')
model_mobilenetv2 = load_model('models/model_netv2.h5')
model_resnet = load_model('models/model_resnet50.h5')

def preprocess_image(image, target_size):
    if image.mode != "RGB":
        image = image.convert("RGB")
    image = image.resize(target_size)
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    image = image / 255.0  # Normalization
    return image

def predict_image(model, processed_image):
    start_time = time.time()  # Start time before prediction
    prediction = model.predict(processed_image).tolist()
    end_time = time.time()  # End time after prediction
    prediction_time = end_time - start_time  # Calculate prediction time

    predicted_class = np.argmax(prediction)
    class_labels = ['rock', 'paper', 'scissors']

    # Combine all four types of response
    response = {
        'message': f"Predicted label is : {class_labels[predicted_class]} | Accuracy : {prediction[0][predicted_class] * 100:.2f}%",
        'prediction_time': f" | Prediction Time : {prediction_time:.2f} seconds",
        'predicted_class': class_labels[predicted_class]
    }

    return response

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        file = request.files["file"]
        image = Image.open(io.BytesIO(file.read()))
        processed_image = preprocess_image(image, target_size=(150, 150))

        # Choose the model based on the user's selection
        model_name = request.form.get("model")
        if model_name == "cnn":
            response = predict_image(model_cnn, processed_image)
        elif model_name == "resnet":
            response = predict_image(model_resnet, processed_image)
        elif model_name == "mobilenetv2":
            response = predict_image(model_mobilenetv2, processed_image)
        else:
            response = {'error': 'Invalid model selection'}

        # Save the processed image with the predicted class as part of the filename
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"predicted_image_{timestamp}_{response['predicted_class']}.png"
        image.save(f"static/{filename}")

        response['predicted_image'] = filename

        return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
