# Credit-Card-Fraud-Detection-Code
This project focuses on building and evaluating machine learning models to detect fraudulent credit card transactions. The goal is to identify fraudulent transactions from a dataset using various algorithms and compare their performance.

# Table of Contents
- Project Overview
- Team Members
- Dataset
- Dependencies
- Results
- Source Code
- Acknowledgements

# Project Overview
Credit card fraud is a significant problem in financial institutions. This project implements machine learning techniques to detect fraud in credit card transactions. The primary objectives are to preprocess the data, build and evaluate different classification models, and determine the best-performing model.

# Team Members
- Karthik Mahalingam
- Ankitha Dongerkerry Pai
  
# Dataset
The dataset used in this project is a publicly available credit card transaction dataset, which contains transactions made by European cardholders in September 2013. The dataset consists of 284,807 transactions, where 492 are frauds. The dataset is highly imbalanced, with the positive class (frauds) accounting for only 0.172% of all transactions.

- Features: The dataset contains 30 features, including the 'Time' and 'Amount' of the transactions, as well as 28 anonymized features labeled V1 to V28.
- Target: The 'Class' column indicates whether the transaction is fraudulent (1) or not (0).

# Dependencies
- Python 3.6 or higher
- Jupyter Notebook
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Imbalanced-learn

# Results
The notebook evaluates multiple machine learning models, including Logistic Regression, Decision Trees, Random Forests, and Gradient Boosting. The performance of these models is compared based on metrics like precision, recall, F1-score, and ROC-AUC.

