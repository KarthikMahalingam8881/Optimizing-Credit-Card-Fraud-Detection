
# Credit Card Fraud Detection

This project is focused on building a robust credit card fraud detection system using various machine learning and deep learning models. The goal is to identify fraudulent transactions with high accuracy, ensuring financial institutions can reduce losses and enhance security measures.

---

## Project Overview

### Objectives

1. Analyze and preprocess imbalanced credit card transaction data.
2. Explore and visualize patterns in fraudulent and non-fraudulent transactions.
3. Build and evaluate classification models to detect fraudulent transactions.
4. Compare multiple approaches, including Random Forest, SVM, Neural Networks, and PyTorch-based models.

### Dataset Description

- **Dataset Size**: ~284,000 transactions.
- **Features**: 30 anonymized features (V1-V28), Time, Amount, and Class.
- **Target Variable**: 
  - `Class`: 0 = Non-fraudulent, 1 = Fraudulent.
- **Imbalance**: Only 0.17% of transactions are fraudulent.

---

## Workflow

### 1. Data Exploration and Visualization

- **Class Imbalance**: Severe imbalance with a majority of transactions being non-fraudulent.
- **Feature Correlation**: Analyzed feature relationships using heatmaps and pairwise plots.
- **Temporal Analysis**: Explored fraud trends across different times of the day.
- **Transaction Amounts**: Compared fraud vs. non-fraud distributions.

### 2. Data Preprocessing

- Handled missing data by using interpolation techniques.
- Normalized transaction amounts to standardize input features.
- Created additional features, such as `Hour` from the `Time` variable, for temporal insights.

### 3. Modeling Approaches

#### a. Random Forest Classifier
- Feature importance analysis for model interpretability.
- Achieved **[85.3%]**.

#### b. Support Vector Machine (SVM)
- Evaluated performance with a radial basis kernel.
- Accuracy: **[80%]**.

#### c. Neural Networks
- Developed deep learning models using TensorFlow and PyTorch.
- Included techniques like dropout layers to prevent overfitting.
- Performance: **[96%]**.

### 4. Evaluation Metrics

- Used metrics such as **ROC-AUC Score**, **Accuracy**, and **Confusion Matrix** to evaluate models.
- Focused on minimizing false negatives, which have a significant business impact.

---

# Team Members
- Karthik Mahalingam
- Ankitha Dongerkerry Pai

---

## Tools and Libraries

- **Programming Language**: Python
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, `scikit-learn`, `TensorFlow`, `PyTorch`, `XGBoost`, `LightGBM`.
- **Visualization**: `Plotly`, `Matplotlib`, `Seaborn`.

---

## Key Results

1. **Random Forest**: Identified as the most effective model for this dataset due to its ability to handle class imbalance.
2. **Neural Networks**: Provided high precision but required more computational resources.
3. **Feature Importance**:
   - Key features: `V4`, `V12`, `Amount`, `V17`.

---

## Business Impact

### Problem Addressed
Credit card fraud causes significant financial losses, damages brand trust, and leads to operational inefficiencies in dispute resolution.

### Value Delivered
1. **Fraud Mitigation**:
   - Reduced false negatives to identify fraud early and prevent unauthorized transactions.
2. **Cost Efficiency**:
   - Decreased operational costs related to manual review of flagged transactions.
3. **Customer Trust**:
   - Enhanced customer trust through proactive fraud detection, leading to improved brand loyalty.
4. **Scalability**:
   - The models are scalable for real-time implementation in transaction monitoring systems.

---

## Recommendations

1. **Short-Term**:
   - Deploy Random Forest for immediate fraud detection.
   - Monitor model performance regularly to ensure accuracy with new data.

2. **Long-Term**:
   - Transition to deep learning models for larger datasets.
   - Integrate the model with real-time systems for live fraud detection.
   - Regularly retrain models to adapt to evolving fraud patterns.

---

## How to Run the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/credit-card-fraud-detection.git

## Future Work
1. Incorporate additional data sources, such as IP addresses and transaction locations.
2. Implement ensemble models for enhanced performance.
3. Explore explainable AI methods to improve model transparency.
