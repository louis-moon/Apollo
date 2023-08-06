import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error

data = pd.read_csv("table.csv")
data = data.set_index('Nutrients').T

vitamin_c_col = data["Vitamin C, mg"]
X = data.drop("Vitamin C, mg", axis=1)
y = vitamin_c_col

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/13, random_state=42)

regressor = RandomForestRegressor(random_state=42)

param_grid = {
    'n_estimators': [200],
    'max_depth': [None, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
    'min_samples_split': [2, 3, 4, 5, 6]
}

grid_search = GridSearchCV(estimator=regressor, param_grid=param_grid, cv=3, scoring='neg_mean_squared_error', verbose=1, n_jobs=-1)
grid_search.fit(X_train, y_train)

best_parameters = grid_search.best_params_

best_regressor = RandomForestRegressor(n_estimators=best_parameters['n_estimators'], 
                                       max_depth=best_parameters['max_depth'], 
                                       min_samples_split=best_parameters['min_samples_split'], 
                                       random_state=42)

best_regressor.fit(X_train, y_train)

predicted_vitamin_c = best_regressor.predict(X_test)

mse = mean_squared_error(y_test, predicted_vitamin_c)
print("Mean squared error:", round(mse, 2))