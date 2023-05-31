import pandas as pd
import numpy as np
import joblib

def predictRuns(input_test):

    with open('regression_model.joblib','rb') as f:
        regressor = joblib.load(f)
    with open('venue_encoder.joblib','rb') as f:
        venue_encoder = joblib.load(f)
    with open('team_encoder.joblib','rb') as f:
        team_encoder = joblib.load(f)
   
    test_case = pd.read_csv(input_test)
    test_case['venue']          =  venue_encoder.transform(test_case['venue'])
    test_case['batting_team']          =  team_encoder.transform(test_case['batting_team'])
    test_case['bowling_team']          =  team_encoder.transform(test_case['bowling_team'])
    test_case = test_case[['venue','innings','batting_team','bowling_team']]
    return regressor.predict(test_case)