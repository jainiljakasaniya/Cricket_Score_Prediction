import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
import joblib

# Load the preprocessed data
data = pd.read_csv('myPreprocessed.csv')

# Initialize label encoders
venue_encoder = LabelEncoder()
team_encoder = LabelEncoder()

# Encode categorical features
data['venue'] = venue_encoder.fit_transform(data['venue'])
data['batting_team'] = team_encoder.fit_transform(data['batting_team'])
data['bowling_team'] = team_encoder.fit_transform(data['bowling_team'])

# Split the data into training and testing sets
train_df, test_df = train_test_split(data, test_size=0.3, random_state=42)

# Define target and predictor variables
target_var = 'total_runs'
predictor_vars = ['venue', 'innings', 'batting_team', 'bowling_team']

# Train a Random Forest Regressor
rfr = RandomForestRegressor(n_estimators=100, random_state=42)
rfr.fit(train_df[predictor_vars], train_df[target_var])

# Evaluate the model
predictions = rfr.predict(test_df[predictor_vars])
mse = mean_squared_error(test_df[target_var], predictions)
print(f'Mean Squared Error: {mse}')

# Save the trained model and encoders
joblib.dump(rfr, 'regression_model.joblib')
joblib.dump(venue_encoder, 'venue_encoder.joblib')
joblib.dump(team_encoder, 'team_encoder.joblib')
