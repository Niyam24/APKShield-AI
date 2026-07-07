print("Program started")

from feature_extractor import extract_features
from predictor import predict

print("Imports successful")

apk = "uploads/test.apk"

print("Extracting features...")
info = extract_features(apk)

print(info)

print("Running prediction...")
result = predict(info)

print(result)

print("Finished")