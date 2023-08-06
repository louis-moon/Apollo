# Health Supplement Modeling
## Introduction
This repository contains modeling code tailored to predict health supplement outputs, specifically focusing on macronutrients, vitamins, and minerals. By using a dataset containing information about gender and age, our primary objective is to make accurate predictions on an individual's Vitamin C requirements. This project is designed for the nonprofit startup Equity A1.

## Features
- Data Loading and Processing: The data is sourced from table.csv and reshaped to make it suitable for modeling.
- Predictive Modeling: Uses RandomForestRegressor, a popular ensemble learning method, to predict the Vitamin C requirements based on other nutrient data.
- Parameter Tuning: Employs GridSearchCV to search for the best hyperparameters for the RandomForestRegressor model.
## Code Overview
1. Data Processing:

- The data is loaded from table.csv and then transposed to have nutrients as columns.
- The column "Vitamin C, mg" is used as the target variable (y), while the rest of the columns are used as features (X).
2. Train-Test Split:

- The data is split into training and testing datasets. The test size is set to 1/13 of the total dataset.
3. Hyperparameter Tuning:

- GridSearchCV is used with a RandomForestRegressor to find the best parameters (n_estimators, max_depth, and min_samples_split) based on a 3-fold cross-validation.
4. Model Evaluation:

- The model is trained with the best parameters from GridSearchCV and used to predict Vitamin C requirements on the test set.
- The performance of the model is then evaluated using the Mean Squared Error (MSE).
## Usage
To use this code:

1. Ensure you have a table.csv in the root directory with the appropriate format.
2. Run the code. At the end, the Mean Squared Error of the model on the test dataset will be printed.
Dependencies
- numpy
- pandas
- scikit-learn
## Future Directions
Further refinements can be done by:

1. Incorporating more features and data.
2. Exploring different regression algorithms and ensemble techniques.
3. Enhancing hyperparameter tuning and model evaluation processes.
