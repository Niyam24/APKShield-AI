import json
import joblib
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent

MODEL = joblib.load(BASE_DIR / "models" / "apk_classifier.pkl")
ENCODER = joblib.load(BASE_DIR / "models" / "label_encoder.pkl")

with open(BASE_DIR / "all_features.json", "r") as f:
    ALL_FEATURES = json.load(f)


def create_feature_vector(apk_info):

    permissions = set()

    for permission in apk_info["permissions"]:
        permissions.add(permission.split(".")[-1])

    vector = []

    for feature in ALL_FEATURES:

        if feature in permissions:
            vector.append(1)

        else:
            vector.append(0)

    return np.array(vector).reshape(1, -1)


def predict(apk_info):

    X = create_feature_vector(apk_info)

    prediction = MODEL.predict(X)[0]

    confidence = MODEL.predict_proba(X)[0].max()

    label = ENCODER.inverse_transform([prediction])[0]

    return {
        "prediction": label,
        "confidence": float(confidence)
    }