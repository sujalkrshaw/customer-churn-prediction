# 💎 Customer Churn Prediction Dashboard

## 🚀 Overview

This project is an **end-to-end Machine Learning system** that predicts whether a customer is likely to churn.
It combines **data science, model deployment, and a modern dashboard UI** to simulate a real-world business solution used in industries like telecom, SaaS, fintech, and e-commerce.

---

## 🎯 Objective

* Predict customer churn probability
* Identify high-risk customers
* Provide actionable insights for retention strategies
* Build a production-like ML + UI system

---

## 🧠 Key Features

✅ Machine Learning Model (Logistic Regression)
✅ Real-time prediction via Streamlit dashboard
✅ Risk classification (Low / Medium / High)
✅ KPI cards (Probability, Risk Level, Segment)
✅ Visual Risk Meter
✅ Key churn factors explanation
✅ Clean and modern dark UI

---

## 🏗️ Project Architecture

```
Customer-Churn-Prediction/
│
├── models/
│   ├── churn_model.pkl
│   ├── scaler.pkl
│
├── outputs/
│   ├── confusion_matrix.png
│   
│   
│
├── src/
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Tech Stack

* **Python**
* **Pandas, NumPy**
* **Scikit-learn**
* **Streamlit**
* **Joblib**
* **Matplotlib**

---

## 📊 Machine Learning Workflow

1. Data Generation (Synthetic Dataset)
2. Data Preprocessing & Encoding
3. Train-Test Split (Stratified)
4. Feature Scaling
5. Model Training (Logistic Regression)
6. Evaluation:

   * Accuracy
   * Confusion Matrix
   * ROC Curve
7. Model Saving (`.pkl`)
8. Deployment via Streamlit UI

---

## ▶️ How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/your-username/customer-churn-prediction.git
cd customer-churn-prediction
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Train Model

```bash
python main.py
```

### 4. Run Dashboard

```bash
streamlit run app.py
```

---

## 📈 Output Features

* Churn Probability (%)
* Risk Level (Low / Medium / High)
* Customer Segment (Stable / At Risk)
* Risk Meter (Visual)
* Key Risk Factors:

  * Low tenure
  * High charges
  * No tech support
  * Monthly contract

---

## 💡 Business Impact

This system helps companies:

* Reduce customer churn
* Improve retention strategies
* Increase customer lifetime value (LTV)
* Optimize marketing efforts

---

## 🧪 Sample Insight

> Customers with **low tenure + high monthly charges + no support services** show significantly higher churn probability.

---

## 📸 Screenshots

(Add your screenshots here)

---

## 📌 Future Improvements

* Use real-world dataset (Telco churn dataset)
* Deploy with FastAPI backend
* Add authentication system
* Cloud deployment (AWS / Render / Streamlit Cloud)
* Advanced models (XGBoost, LightGBM)

---

## 👨‍💻 Author

**Sujal Shaw**
Aspiring Data Scientist | Machine Learning Enthusiast

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
