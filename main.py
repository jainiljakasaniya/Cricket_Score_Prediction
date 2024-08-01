import sys
from predictor import predict_runs

def main(input_file):
    try:
        runs = predict_runs(input_file)
        print("Predicted Runs: ", runs)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_file>")
    else:
        input_file = sys.argv[1]
        main(input_file)
