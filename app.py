import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/churn_model.pkl")
scaler = joblib.load("models/scaler.pkl")

st.set_page_config(layout="wide")

# -----------------------------
# CUSTOM CSS (PREMIUM DARK UI)
# -----------------------------
st.markdown("""
<style>
.stApp {
    background-color: #0b1120;
    color: white;
}
h1, h2, h3 {
    color: #facc15;
}
.block-container {
    padding: 2rem;
}
div[data-testid="stSidebar"] {
    background-color: #020617;
}
button[kind="primary"] {
    background-color: #facc15;
    color: black;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("## 💎 Intelligence Hub")
    st.write("Advanced ML-based churn prediction system.")
    st.write("⚙️ Engine: ML Model")
    st.write("📊 Status: Active")

# -----------------------------
# HEADER
# -----------------------------
st.markdown("## 💎 Executive Churn Intelligence")

col1, col2 = st.columns([2, 1])

# -----------------------------
# LEFT PANEL
# -----------------------------
with col1:
    st.markdown("### 📋 Customer Profile")

    tab1, tab2, tab3 = st.tabs(["Personal Info", "Service Details", "Billing & Contract"])

    with tab1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        partner = st.selectbox("Partner", ["Yes", "No"])
        senior = st.selectbox("Senior Citizen", [0, 1])
        dependents = st.selectbox("Dependents", ["Yes", "No"])

    with tab2:
        phone = st.selectbox("Phone Service", ["Yes", "No"])
        internet = st.selectbox("Internet Service", ["DSL", "Fiber", "None"])
        tech = st.selectbox("Tech Support", ["Yes", "No"])
        security = st.selectbox("Online Security", ["Yes", "No"])

    with tab3:
        tenure = st.slider("Tenure (Months)", 0, 72)
        monthly = st.number_input("Monthly Charges ($)", 0, 500)
        contract = st.selectbox("Contract Type", ["Monthly", "Yearly"])

    predict_btn = st.button("🚀 Generate Risk Assessment")

# -----------------------------
# RIGHT PANEL
# -----------------------------
with col2:
    st.markdown("### 📊 Analytical Output")

    if predict_btn:
        # Encode inputs
        tech_val = 1 if tech == "Yes" else 0
        contract_val = 0 if contract == "Monthly" else 1

        # Feature order (must match training)
        features = np.array([[tenure, monthly, tech_val, contract_val]])

        # Scale
        features_scaled = scaler.transform(features)

        # Predict
        prob = model.predict_proba(features_scaled)[0][1]
        percentage = round(prob * 100, 2)

        # -----------------------------
        # KPI CARDS
        # -----------------------------
        kpi1, kpi2, kpi3 = st.columns(3)

        with kpi1:
            st.metric("Churn Probability", f"{percentage}%")

        with kpi2:
            if prob > 0.7:
                risk = "High"
            elif prob > 0.4:
                risk = "Medium"
            else:
                risk = "Low"
            st.metric("Risk Level", risk)

        with kpi3:
            segment = "At Risk" if prob > 0.5 else "Stable"
            st.metric("Customer Segment", segment)

        # -----------------------------
        # RISK TITLE
        # -----------------------------
        if prob > 0.7:
            st.markdown("## 🔴 High Risk Customer")
        elif prob > 0.4:
            st.markdown("## 🟡 Medium Risk Customer")
        else:
            st.markdown("## 🟢 Low Risk Customer")

        # -----------------------------
        # RISK METER
        # -----------------------------
        st.markdown("### Risk Meter")
        st.progress(prob)
        st.caption("0% = Safe | 100% = High Risk")

        # -----------------------------
        # STATUS MESSAGE
        # -----------------------------
        if prob > 0.7:
            st.error("Immediate retention action required!")
        elif prob > 0.4:
            st.warning("Monitor this customer closely.")
        else:
            st.success("Customer is stable.")

        # -----------------------------
        # WHY CHURN
        # -----------------------------
        st.markdown("### 🔍 Key Risk Factors")

        reasons = []

        if tenure < 20:
            reasons.append("Low tenure (new customer)")
        if monthly > 300:
            reasons.append("High monthly charges")
        if tech_val == 0:
            reasons.append("No tech support")
        if contract_val == 0:
            reasons.append("Monthly contract (low commitment)")

        if reasons:
            for r in reasons:
                st.write(f"- {r}")
        else:
            st.write("No major risk factors detected")