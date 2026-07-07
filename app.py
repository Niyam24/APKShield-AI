import streamlit as st
import joblib
from pathlib import Path

from feature_extractor import extract_features
from predictor import predict

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="APKShield AI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_DIR = Path(__file__).parent

MODELS_DIR = BASE_DIR / "models"

UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

MODEL_PATH = MODELS_DIR / "apk_classifier.pkl"
ENCODER_PATH = MODELS_DIR / "label_encoder.pkl"

# ==========================================
# LOAD MODEL
# ==========================================

model_loaded = False

try:

    joblib.load(MODEL_PATH)
    joblib.load(ENCODER_PATH)

    model_loaded = True

except:

    model_loaded = False


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🛡 APKShield AI")

    st.caption("AI Powered Android Malware Scanner")

    st.divider()

    if model_loaded:
        st.success("🟢 AI Engine Online")
    else:
        st.error("🔴 AI Engine Offline")

    st.divider()

    st.subheader("Model")

    st.write("**Algorithm**")
    st.write("XGBoost")

    st.write("**Validation Accuracy**")
    st.write("98.59%")

    st.write("**Dataset**")
    st.write("Drebin-215")

    st.write("**Samples**")
    st.write("7259 APKs")

    st.divider()

    st.subheader("About")

    st.write(
        """
APKShield AI performs static malware analysis
using Machine Learning and Androguard.

Version **1.0**
"""
    )


# ==========================================
# HEADER
# ==========================================

st.title("🛡 APKShield AI")

st.markdown(
"""
### AI Powered Android Malware Detection Platform

Upload an Android APK and let APKShield AI perform
static malware analysis using Machine Learning.
"""
)

st.divider()
# ==========================================
# MAIN LAYOUT
# ==========================================

left, right = st.columns([2,1])

# ==========================================
# LEFT PANEL
# ==========================================

with left:

    st.subheader("📂 Upload APK")

    uploaded_file = st.file_uploader(
        "Choose an Android APK",
        type=["apk"]
    )

    apk_path = None

    if uploaded_file is not None:

        apk_path = UPLOAD_DIR / uploaded_file.name

        with open(apk_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        st.success(f"✅ {uploaded_file.name} uploaded successfully.")

    analyze = st.button(
        "🔍 Analyze APK",
        use_container_width=True
    )

    if analyze:

        if uploaded_file is None:

            st.warning("Please upload an APK first.")

        else:

            with st.spinner("Analyzing APK..."):

                progress = st.progress(0)

                progress.progress(15)

                info = extract_features(str(apk_path))

                progress.progress(55)

                if "error" in info:

                    st.error(info["error"])

                else:

                    result = predict(info)

                    progress.progress(100)

                    prediction = result["prediction"]
                    confidence = result["confidence"] * 100

                    if str(prediction).upper().startswith("B"):

                        st.success("🟢 BENIGN")

                        risk = "LOW"

                        recommendation = (
                            "This APK appears safe based on the current "
                            "machine learning analysis."
                        )

                    else:

                        st.error("🔴 MALICIOUS")

                        risk = "HIGH"

                        recommendation = (
                            "Potential malware detected. "
                            "Avoid installing this APK."
                        )

                    st.metric(
                        "Confidence",
                        f"{confidence:.2f}%"
                    )

                    st.divider()

                    st.subheader("📦 APK Information")

                    c1, c2 = st.columns(2)

                    with c1:

                        st.metric(
                            "Package",
                            info["package"]
                        )

                        st.metric(
                            "Target SDK",
                            info["target_sdk"]
                        )

                        st.metric(
                            "Minimum SDK",
                            info["min_sdk"]
                        )

                    with c2:

                        st.metric(
                            "APK Size",
                            f'{info["apk_size"]:.2f} MB'
                        )

                        st.metric(
                            "Activities",
                            len(info["activities"])
                        )

                        st.metric(
                            "Services",
                            len(info["services"])
                        )

                    st.divider()

                    st.subheader("🔒 SHA-256")

                    st.code(info["sha256"])

                    st.divider()

                    st.subheader("⚠ Risk Assessment")

                    st.write(f"**Risk Level:** {risk}")

                    st.info(recommendation)

                    with st.expander("View Permissions"):

                        for permission in info["permissions"]:

                            st.write("•", permission)
 # ==========================================
# RIGHT PANEL
# ==========================================

with right:

    st.subheader("🖥 System Status")

    if model_loaded:
        st.success("🟢 AI Engine Online")
    else:
        st.error("🔴 AI Engine Offline")

    st.metric("Model", "XGBoost")
    st.metric("Validation Accuracy", "98.59%")
    st.metric("Dataset", "Drebin-215")
    st.metric("Training Samples", "7,259")
    st.metric("Feature Count", "215")

    st.divider()

    st.subheader("🛡 Detection Engine")

    st.success("✔ Static Analysis")
    st.success("✔ Manifest Inspection")
    st.success("✔ Permission Analysis")
    st.success("✔ Feature Vector Generation")
    st.success("✔ Machine Learning Classification")
    st.success("✔ SHA-256 Fingerprinting")

    st.divider()

    st.subheader("⚡ Supported Analysis")

    st.write("• APK Metadata")
    st.write("• Android Permissions")
    st.write("• Activities")
    st.write("• Services")
    st.write("• Broadcast Receivers")
    st.write("• Content Providers")
    st.write("• SDK Information")
    st.write("• SHA-256 Hash")

st.divider()

# ==========================================
# FOOTER
# ==========================================

st.markdown("### 🔍 Analysis Pipeline")

st.code(
"""
APK Upload
     ↓
Androguard Feature Extraction
     ↓
215-Dimensional Feature Vector
     ↓
XGBoost Malware Classifier
     ↓
Risk Assessment
     ↓
Security Recommendation
"""
)

st.caption(
    "APKShield AI • Built using Streamlit, Androguard, XGBoost and the Drebin Dataset."
)                           