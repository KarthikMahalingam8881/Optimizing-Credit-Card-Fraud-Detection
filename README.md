
# 💳 Credit Card Fraud Detection Project

## 1️⃣ Business Problem
Credit card fraud is a major concern for financial institutions, leading to billions of dollars in annual losses. Fraudulent transactions must be detected in real-time to prevent losses while minimizing disruptions to legitimate transactions. The key challenge is that fraud cases are extremely rare (highly imbalanced dataset), making detection difficult.

## 2️⃣ Objective
The goal was to develop a machine learning pipeline that accurately detects fraudulent transactions while balancing key trade-offs:

- **Minimizing False Negatives**: To ensure that fraudulent transactions are not missed.
- **Reducing False Positives**: To avoid unnecessary declines of legitimate transactions.
- **Providing Interpretable Insights**: So financial institutions can take proactive fraud prevention measures.

### Key evaluation metrics:
- **Recall (Sensitivity)**: Measures how many fraudulent transactions are correctly identified.
- **Precision**: Ensures flagged transactions are actually fraud.
- **F1-Score**: Balances precision and recall.
- **AUC-ROC Score**: Evaluates how well the model distinguishes fraud from non-fraud.
- **Business Metrics**: Includes fraud savings and false positive rate.

## 3️⃣ Data Preprocessing and Feature Engineering

### 📌 Data Cleaning
- Removed duplicate transactions to ensure unbiased model training.
- Checked for and handled missing values to maintain data integrity.

### 📌 Handling Outliers
- Used **Interquartile Range (IQR)** to identify extreme values in fraudulent transactions.
- Instead of removing them, I **flagged them as a new feature** (**Fraudulent_Outlier_Flag**).
- This helped the model learn high-value fraudulent transaction patterns.

### 📌 Exploratory Data Analysis (EDA)
- **Transaction Timing Analysis**: Fraudulent transactions had distinct time patterns.
- **Distribution of Transaction Amounts**: Fraudulent transactions showed higher variance in amounts.
- **Correlation Analysis**: Identified key variables impacting fraud detection.

### 📌 Feature Engineering
Created new features to improve fraud detection:
- **Interaction Features**: (Amount * V20, V17 * V12, etc.) captured complex fraud patterns.
- **Statistical Features**: (Z_Amount, Rolling_Mean_Amount) helped standardize and track unusual spending.
- **Flag Variables**: (High_V3_Flag, Low_V20_Flag) identified unusual transaction behaviors.

## 4️⃣ Model Development

### 📌 Machine Learning Models Used
#### **Random Forest (Best Model)**
- Trained with **SMOTE** to handle class imbalance.
- Achieved high fraud detection accuracy while reducing false positives.
- **AUC-ROC Score**: 0.98.

#### **XGBoost**
- Used for comparison and deeper fraud insights.
- Performed well but slightly less interpretable than Random Forest.

#### **SVM and Anomaly Detection Models**
- Explored **Isolation Forest and One-Class SVM** for anomaly detection.
- Helped in identifying patterns but not as effective for large-scale classification.

### 📌 Hyperparameter Tuning
- Used **Halving Random Search CV** for optimizing Random Forest parameters.
- This reduced training time while improving model performance.

## 5️⃣ Results and Business Impact

### 📌 Key Metrics and Outcomes
| Metric | Value |
|--------|------|
| **Total Fraudulent Amount Flagged** | **$20,551.38** |
| **Actual Fraudulent Amount Detected** | **$10,502.43** |
| **Savings Percentage** | **51.10%** |
| **False Positive Rate** | **0.24%** |
| **Fraud Detection Rate Improvement** | **25% over baseline** |

### 📌 Feature Importance Analysis
- **Top fraud-driving features** included **V4, V14, V12, and Amount_Time_V14**.
- **Interaction terms** improved the model’s fraud detection ability.

### 📌 Financial Impact
- By **reducing false positives**, the model minimizes disruptions to legitimate customers.
- **Improved fraud detection** translates to **millions in potential savings** for financial institutions.
- The insights from **feature importance** provide **actionable fraud prevention strategies**.

### 📌 Problem Addressed
Credit card fraud causes significant financial losses, damages brand trust, and leads to operational inefficiencies in dispute resolution.

### 📌 Value Delivered
  1. **Fraud Mitigation**:
     - Reduced false negatives to identify fraud early and prevent unauthorized transactions.
  2. **Cost Efficiency**:
     - Decreased operational costs related to manual review of flagged transactions.
  3. **Customer Trust**:
     - Enhanced customer trust through proactive fraud detection, leading to improved brand loyalty.
  4. **Scalability**:
     - The models are scalable for real-time implementation in transaction monitoring systems.

## 6️⃣ Recommendations

1. **Short-Term**:
   - Deploy Random Forest for immediate fraud detection.
   - Monitor model performance regularly to ensure accuracy with new data.

2. **Long-Term**:
   - Transition to deep learning models for larger datasets.
   - Integrate the model with real-time systems for live fraud detection.
   - Regularly retrain models to adapt to evolving fraud patterns.

## 7️⃣ Future Work
1. Incorporate additional data sources, such as IP addresses and transaction locations.
2. Implement ensemble models for enhanced performance.
3. Explore explainable AI methods to improve model transparency.
 
## 8️⃣ Conclusion
This project successfully built a highly accurate fraud detection system that balances fraud detection with minimal disruptions to real customers. By leveraging **advanced machine learning techniques, feature engineering, and anomaly detection**, the model enhances existing fraud prevention systems. The approach provides **scalable, interpretable, and financially valuable solutions** for the banking industry.

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/credit-card-fraud-detection.git


