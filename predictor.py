import pandas as pd
import joblib

def predict_runs(input_test):
    """
    Predicts the total runs at the end of the 6th over for given test cases.

    Parameters:
    input_test (str): The path to the CSV file containing the test cases.

    Returns:
    np.ndarray: Predicted total runs at the end of the 6th over.
    """
    try:
        # Load the trained model and encoders
        with open('regression_model.joblib', 'rb') as f:
            regressor = joblib.load(f)
        with open('venue_encoder.joblib', 'rb') as f:
            venue_encoder = joblib.load(f)
        with open('team_encoder.joblib', 'rb') as f:
            team_encoder = joblib.load(f)
        
        # Load and preprocess the test cases
        test_case = pd.read_csv(input_test)
        test_case['venue'] = venue_encoder.transform(test_case['venue'])
        test_case['batting_team'] = team_encoder.transform(test_case['batting_team'])
        test_case['bowling_team'] = team_encoder.transform(test_case['bowling_team'])
        
        # Select the relevant features
        test_case = test_case[['venue', 'innings', 'batting_team', 'bowling_team']]
        
        # Predict and return the results
        predictions = regressor.predict(test_case)
        return predictions
    
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
# input_test = 'path_to_your_test_case.csv'
# predictions = predict_runs(input_test)
# print(predictions)
