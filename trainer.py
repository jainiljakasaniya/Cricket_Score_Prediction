import numpy as np 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score
import joblib

data = pd.read_csv('myPreprocessed.csv')

venue_encoder = LabelEncoder()
team_encoder = LabelEncoder()

data['venue'] = venue_encoder.fit_transform(data['venue'])
data['batting_team'] = team_encoder.fit_transform(data['batting_team'])
data['bowling_team'] = team_encoder.fit_transform(data['bowling_team'])


train_df, test_df = train_test_split(data, test_size=0.3, random_state=42)

target_var=['total_runs']
predictor_var = ['venue','innings','batting_team', 'bowling_team']

rfc = RandomForestClassifier(n_estimators=100)
rfc.fit(data[predictor_var], data[target_var].values.ravel())


joblib.dump(rfc,'regression_model.joblib')
joblib.dump(venue_encoder,'venue_encoder.joblib')
joblib.dump(team_encoder,'team_encoder.joblib')