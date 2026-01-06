from flask import Flask, render_template, request
import tensorflow as tf
import numpy as np
from PIL import Image

# -----------------------------------
# Create Flask App
# -----------------------------------
app = Flask(__name__)

# -----------------------------------
# Load Trained Model (.keras file)
# -----------------------------------
model = tf.keras.models.load_model("mango_disease_model.keras")

# -----------------------------------
# Class names (MUST match training order exactly)
# -----------------------------------
class_names = [
    'Anthracnose',
    'Bacterial_Canker',
    'Cutting_Weevil',
    'Die_Back',
    'Healthy',
    'Powdery_Mildew',
    'Sooty_Mould'
]

# -----------------------------------
# Home Route
# -----------------------------------
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    confidence = None
    image_url = None

    if request.method == "POST":
        file = request.files["image"]

        # Save image temporarily
        image_path = "static/uploaded_image.jpg"
        file.save(image_path)
        image_url = image_path

        img = Image.open(image_path).convert("RGB")

        img_array = tf.keras.preprocessing.image.img_to_array(img)
        img_array = tf.expand_dims(img_array, axis=0)

        predictions = model.predict(img_array)
        predicted_index = np.argmax(predictions[0])

        prediction = class_names[predicted_index]
        confidence = round(100 * np.max(predictions[0]), 2)

    return render_template(
        "index.html",
        prediction=prediction,
        confidence=confidence,
        image_url=image_url
    )


# -----------------------------------
# Run Flask App
# -----------------------------------
if __name__ == "__main__":
    app.run(debug=True)
