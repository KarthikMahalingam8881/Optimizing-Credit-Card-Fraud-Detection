# Credit-Card-Fraud-Detection-Code
# Energy-consumption-forecasting
# Final Project - CSE 572 Data Mining

## Project Overview
This project is part of the CSE 572 Data Mining course. The objective is to apply data mining techniques to a given dataset and analyze the results. The project involves preprocessing the data, training a machine learning model, evaluating its performance, and visualizing the results.

## Team Members
- Karthik Mahalingam
- Prasuk Jain
- Vedanth Prasanna Bharadwaj
- Pratik Dnyaneshwar Kale

## Requirements
- Python 3.11.5
- Jupyter Notebook
- NumPy
- Pandas
- Matplotlib
- Scikit-learn
- PyTorch

## Usage
1. Open the `FinalProject-CSE572-DataMining.ipynb` notebook in Jupyter.
2. Follow the steps in the notebook to preprocess the data, train the model, and evaluate its performance.
3. The notebook includes visualizations to help understand the results.

## Project Structure
- `FinalProject-CSE572-DataMining.ipynb`: Jupyter Notebook containing the code and analysis.
- `data/`: Directory containing the dataset (except electricity.csv, other dataset are included in the repository).
- `models/`: Directory to save trained models(not included in the repository).
- `results/`: Directory to save the results and visualizations (not included in the repository).

## Key Functions and Classes
- `preprocess_data()`: Function to preprocess the data.
- `train_epoch()`: Function to train the model for one epoch.
- `evaluate()`: Function to evaluate the model.
- `plot_results()`: Function to plot the training and testing losses.

## Data Preprocessing
The data preprocessing step includes handling missing values, encoding categorical variables, and splitting the data into training and testing sets.

## Model Training
A PyTorch model is trained using the training data. The model's performance is evaluated on the test data, and the losses are plotted to visualize the training process.

## Scikit-learn Models
In addition to the PyTorch model, several Scikit-learn models are also trained and evaluated. These models include:
- Logistic Regression
- Random Forest
- Support Vector Machine (SVM)
- Gradient Boosting

## Key Features
- Comprehensive data preprocessing pipeline.
- Training and evaluation of multiple machine learning models.
- Visualization of training and testing losses.
- Comparison of model performance using various metrics.
- Saving and loading trained models for future use.
  
## Evaluation
The model's performance is evaluated using appropriate metrics, and the results are visualized for better understanding.

## Results
The results of the model training and evaluation are plotted using Matplotlib to provide insights into the model's performance.

## Contributing
If you wish to contribute to this project, please fork the repository and submit a pull request.

## Acknowledgments
This project was developed as part of the CSE 572 Data Mining course. Special thanks to the course instructors and teaching assistants for their guidance and support.

