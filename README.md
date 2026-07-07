# 🛡️ APKShield AI

An AI-powered Android Malware Detection Platform that performs **static APK analysis** using **Machine Learning**. APKShield AI extracts features from Android applications using **Androguard** and classifies them as **Benign** or **Malicious** using an **XGBoost** model trained on the **Drebin-215 dataset**.

---

## 🚀 Features

- 📂 Upload Android APK files
- 🤖 AI-powered malware detection
- ⚡ Static APK analysis using Androguard
- 🔐 SHA-256 fingerprint generation
- 📦 APK metadata extraction
- 📱 Target SDK & Minimum SDK detection
- 📊 XGBoost Machine Learning classifier
- 📈 Prediction confidence score
- 🛡 Risk assessment dashboard
- 📋 Android permission analysis

---

## 🖼️ Screenshots

### Dashboard



```
images/dashboard.png
```

### Malware Analysis

> Add your analysis result screenshot here.

```
images/analysis.png
```

---

## 🏗️ System Architecture

```
          Android APK
                │
                ▼
      Feature Extraction
        (Androguard)
                │
                ▼
     215 Feature Vector
                │
                ▼
      XGBoost Classifier
                │
                ▼
     Malware Prediction
                │
                ▼
      Streamlit Dashboard
```

---

## 🧠 Machine Learning Model

- **Algorithm:** XGBoost
- **Dataset:** Drebin-215
- **Features:** 215
- **Validation Accuracy:** 98.59%

---

## 📦 APK Information Extracted

- Package Name
- APK Size
- Target SDK
- Minimum SDK
- SHA-256 Hash
- Activities
- Services
- Receivers
- Providers
- Android Permissions

---

## 🛠️ Tech Stack

- Python
- Streamlit
- XGBoost
- Scikit-learn
- Androguard
- NumPy
- Joblib

---

## 📁 Project Structure

```
APKShield-AI
│
├── app.py
├── feature_extractor.py
├── predictor.py
├── requirements.txt
├── README.md
├── all_features.json
│
├── models
│   ├── apk_classifier.pkl
│   └── label_encoder.pkl
│
├── static
│   └── style.css
│
├── uploads
│
└── temp
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Niyam24/APKShield-AI.git
```

Move into the project

```bash
cd APKShield-AI
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 📋 How It Works

1. Upload an Android APK.
2. APKShield extracts static features using Androguard.
3. A 215-dimensional feature vector is generated.
4. The trained XGBoost model classifies the APK.
5. The dashboard displays:
   - Prediction (Benign/Malicious)
   - Confidence Score
   - APK Metadata
   - SHA-256 Hash
   - Risk Assessment

---

## 🎯 Future Improvements

- PDF security reports
- Detection history
- Dangerous permission highlighting
- Risk score visualization
- API call analysis
- Batch APK scanning

---

## 👨‍💻 Author

**Niyam Maakan**

GitHub: https://github.com/Niyam24

---

## 📄 License

This project is intended for educational and research purposes.
