from feature_extractor import extract_features

apk = "uploads/test.apk"

info = extract_features(apk)

print(info)