# 🥭 Mango Leaf Disease Detection Web App
<img width="800" alt="App Screenshot"
     src="https://github.com/user-attachments/assets/27f11eb2-c29b-4305-8d1e-dad4f63d79e2" />


A deep learning–based web application that detects **mango leaf diseases** from uploaded images using a **Convolutional Neural Network (CNN)** built with **TensorFlow** and deployed using **Flask**.

This project demonstrates the integration of **AI + Web Development** for smart agriculture.

---

## 🚀 Features

- 📸 Upload a mango leaf image
- 🧠 CNN-based disease prediction
- 📊 Prediction confidence score
- 🖼️ Uploaded image preview
- 🎨 Mango-themed modern UI
- ⚡ Fast inference with TensorFlow

---

## 🦠 Diseases Detected

The model classifies the following mango leaf conditions:

- Anthracnose  
- Bacterial Canker  
- Cutting Weevil  
- Die Back  
- Healthy  
- Powdery Mildew  
- Sooty Mould  

---

## 🛠️ Tech Stack

### Machine Learning
- TensorFlow / Keras  
- NumPy  
- PIL (Image Processing)

### Web Development
- Flask (Python backend)  
- HTML5  
- CSS3  
- JavaScript

### Tools
- VS Code  
- Git & GitHub  
- Google Colab (model training)

---

## 📂 Project Structure

mango-leaf-disease-detection/
│
├── app.py # Flask backend
├── mango_disease_model.keras # Trained CNN model
├── templates/
│ └── index.html # Frontend UI
├── static/
│ └── .gitkeep # Static assets folder
├── .gitignore
└── README.md


---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/mango-leaf-disease-detection.git
cd mango-leaf-disease-detection
2️⃣ Create and activate a virtual environment

Windows

python -m venv venv
venv\Scripts\activate


Mac / Linux

python -m venv venv
source venv/bin/activate

3️⃣ Install dependencies
pip install flask tensorflow pillow numpy

4️⃣ Run the Flask application
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000/


Upload a mango leaf image and get disease prediction instantly 
