# TOPSIS Implementation with CLI
A Python package for implementing the TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution) algorithm. This package supports both CSV and Excel files as input and output formats, making it easy to analyze data directly from spreadsheets.

### Installation
Follow the steps below to install and use the package:  

Install the Package from PyPI (recommended):


```
pip install topsis_102203872
```

Clone the Repository (Optional for local development):


```
git clone https://github.com/arpitaggarwal0511/TOPSIS-pypyi.git
cd TOPSIS-pypi
```

(Optional) Install Locally: If you have the source code and want to install the package locally:

```
pip install setuptools wheel
python setup.py sdist bdist_wheel
pip install .
```

### Arguments
| Arguments | Description |
|------------| -----------------|
| input_file |  "CSV/Excel" file path |
| weights | Comma separated numbers |
| impacts | Comma separated '+' or '-' |
| output_file | Output CSV/Excel file path |

### Usage
- Command-Line Interface (CLI)
- Package installed from PyPi can be globally used irrespective of directory
- After installation, you can use the package directly from the command line using topsis-cli. 
- The CLI supports both .csv and .xlsx formats for input and output files.

```
topsis-cli <input_file> <weights> <impacts> <output_file>
```
**WARNING**  :  
Alternatively, if you have the file 'topsis_102203872.py' on your local machine, you can use the following command in your terminal , it is mandatory to be in the directory where this file is present:

```
python topsis_102203872.py <input_file> <weights> <impacts> <output_file>
```



### Arguments:
- input_file: Path to the input file (must be .csv or .xlsx).
- weights: Comma-separated list of weights for the criteria (e.g., 0.4,0.3,0.3).
- impacts: Comma-separated list of impacts for the criteria (+ for positive, - for negative).
- output_file: Path to save the output file (can be .csv or .xlsx).
### Example Commands:
- Example 1: Using CSV Files

```
topsis-cli data.csv 0.4,0.3,0.3 +,-,+ result.csv
```
- Example 2: Using Excel Files


```
topsis-cli data.xlsx 0.4,0.3,0.3 +,-,+ result.xlsx
```
- Example 3: Mixed Formats
Input as .xlsx and output as .csv:


```
topsis-cli data.xlsx 0.4,0.3,0.3 +,-,+ result.csv
```
**Input File Format**

The input file must have the following structure:

| Column 1 | Column 2 | Column 3 | ... | Column n |
|---|---|---|---|---|
| Alternative Name/ID | Criterion 1 Value | Criterion 2 Value | ... | Criterion n Value | 
| ... | ... | ... | ... | ... |

**Example Input File (data.csv or data.xlsx):**

| Alternative | Criterion 1 | Criterion 2 | Criterion 3 |
|---|---|---|---|
| A | 250 | 16 | 12 |
| B | 200 | 32 | 8 |
| C | 300 | 24 | 16 |
| D | 275 | 40 | 20 |

**Output File Format**

The output file will be the same as the input file but with two additional columns:

| Column 1 | Column 2 | Column 3 | ... | Column n | Column n+1 | Column n+2 |
|---|---|---|---|---|---|---|
| Alternative Name/ID | Criterion 1 Value | Criterion 2 Value | ... | Criterion n Value | Topsis Score | Rank |
| ... | ... | ... | ... | ... | ... | ... |

**Example Output File (result.csv or result.xlsx):**

| Alternative | Criterion 1 | Criterion 2 | Criterion 3 | Topsis Score | Rank |
|---|---|---|---|---|---|
| A | 250 | 16 | 12 | 0.67 | 2 |
| B | 200 | 32 | 8 | 0.33 | 4 |
| C | 300 | 24 | 16 | 0.75 | 1 |
| D | 275 | 40 | 20 | 0.50 | 3 | 

### Error Handling
Common Errors and Fixes:

__File Not Found:__

- Ensure the file path is correct.
 ###### Example: Use C:\\Users\\YourName\\Documents\\data.csv on Windows or data.csv if the file is in the current directory.

__Unsupported File Format:__

- Only .csv and .xlsx files are supported.

__Invalid Number of Weights or Impacts:__

- Ensure the number of weights and impacts matches the number of criteria (columns after the first column).
- Impacts Must Be Either + or -:

- Valid impacts are + for positive (higher values are better) and - for negative (lower values are better).
- 
### License
Licensed under the [MIT License](https://github.com/arpitaggarwal0511/TOPSIS-pypyi/blob/main/LICENSE.txt). 


### Contributing
Feel free to submit issues or pull requests for bugs, features, or improvements. For major changes, please open an issue first to discuss what you would like to change.

### Author
Arpit Aggarwal
