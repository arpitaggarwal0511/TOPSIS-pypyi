import numpy as np
import pandas as pd
import argparse
import os

def validate_inputs(file, weights, impacts):
    # Check if file exists
    if not os.path.exists(file):
        raise FileNotFoundError(f"Input file '{file}' not found.")
    
    # Check file extension and load the dataset
    file_extension = os.path.splitext(file)[1].lower()
    if file_extension == ".csv":
        df = pd.read_csv(file)
    elif file_extension in [".xlsx", ".xls"]:
        df = pd.read_excel(file)
    else:
        raise ValueError("Unsupported file format. Please provide a .csv or .xlsx file.")
    
    # Check if the dataset contains at least three columns
    if df.shape[1] < 3:
        raise ValueError("Input file must contain three or more columns.")
    
    # Check if 2nd to last columns contain only numeric values
    if not np.issubdtype(df.iloc[:, 1:].dtypes.values, np.number):
        raise ValueError("Columns from 2nd to last must contain numeric values only.")
    
    # Check if weights and impacts are properly formatted
    weights_list = weights.split(",")
    impacts_list = impacts.split(",")
    if len(weights_list) != len(impacts_list) or len(weights_list) != df.shape[1] - 1:
        raise ValueError("Number of weights, impacts, and columns (excluding the first) must be the same.")
    
    # Check if impacts are either '+' or '-'
    if not all(impact in ["+", "-"] for impact in impacts_list):
        raise ValueError("Impacts must be either '+' or '-'.")
    
    # Return validated weights and impacts
    return np.array([float(w) for w in weights_list]), np.array(impacts_list), df

def topsis(data, weights, impacts):
    # Step 1: Normalize the decision matrix
    norm_matrix = data / np.sqrt((data**2).sum(axis=0))
    
    # Step 2: Multiply by weights
    weighted_matrix = norm_matrix * weights
    
    # Step 3: Determine ideal best and worst
    ideal_best = np.where(impacts == "+", weighted_matrix.max(axis=0), weighted_matrix.min(axis=0))
    ideal_worst = np.where(impacts == "+", weighted_matrix.min(axis=0), weighted_matrix.max(axis=0))
    
    # Step 4: Calculate distances from ideal best and worst
    dist_best = np.sqrt(((weighted_matrix - ideal_best)**2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst)**2).sum(axis=1))
    
    # Step 5: Calculate performance scores
    scores = dist_worst / (dist_best + dist_worst)
    return scores

def main(input_file, weights, impacts, result_file):
    try:
        # Validate inputs
        weights, impacts, df = validate_inputs(input_file, weights, impacts)
        data = df.iloc[:, 1:].values  # Exclude the first column (alternatives)
        
        # Calculate TOPSIS scores
        scores = topsis(data, weights, impacts)
        df["Topsis Score"] = scores
        df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)
        
        # Save results to the output file (determine file type)
        result_extension = os.path.splitext(result_file)[1].lower()
        if result_extension == ".csv":
            df.to_csv(result_file, index=False)
        elif result_extension in [".xlsx", ".xls"]:
            df.to_excel(result_file, index=False)
        else:
            raise ValueError("Unsupported output file format. Please provide a .csv or .xlsx file.")
        
        print(f"Results saved to {result_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TOPSIS Algorithm Implementation with Validations")
    parser.add_argument("input_file", type=str, help="Path to the input file (.csv or .xlsx)")
    parser.add_argument("weights", type=str, help="Comma-separated weights for the criteria")
    parser.add_argument("impacts", type=str, help="Comma-separated impacts for the criteria (+ or -)")
    parser.add_argument("result_file", type=str, help="Path to the output file to save results (.csv or .xlsx)")
    args = parser.parse_args()
    main(args.input_file, args.weights, args.impacts, args.result_file)
