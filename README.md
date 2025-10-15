# 🧹 DATA CLEANING TOOL

**Video Demo:** <URL HERE>  
**Description:**  

This project is a Python-based tool for data cleaning in CSV files.  
It performs common preprocessing tasks such as:

- Handling missing values  
- Removing extra spaces  
- Converting the data type of selected columns  
- Normalizing text capitalization  
- Removing duplicates  
- Exporting the cleaned file  

---

##  How It Works

The main function prompts the user to enter the name of a CSV file.

- If the file does not exist, the message  
  **❌ “File not found. Please check the name and try again.”**  
  is displayed, and the user is prompted again—preventing the need to restart the program.  

- If the file is not a CSV, the message  
  **❌ “The file must have a '.csv' extension.”**  
  appears.

Several exceptions are also included to catch errors, for example, when an empty file is uploaded.  
The function is tolerant of extra spaces in user input.  
Once a valid filename is provided, the file is read into a DataFrame using `pd.read_csv()`.

---

##  Features Explained

### 1. Handling Missing Values
The program first displays how many null values each column contains.  
Then, it removes all rows with missing data and displays the updated count—now expected to be zero.  
Since this step requires no user interaction, only informative progress messages are displayed.

---

### 2. Removing Extra Spaces
In many cases, values with spaces before or after them can be treated as different, even if they are the same.  
To fix this, a function automatically removes unnecessary spaces.

All columns are temporarily converted to text using `astype(str)` so that `.str.strip()` can be safely applied.  
This removes spaces from both text and numeric values such as `' 42 '` or `' 2024-10-01 '`.  

---

### 3. Converting Column Data Types
Because stripping spaces changes column data types—and inconsistent formatting is common—a function was added to convert the data type of specific columns.

- First, it displays the current data types of all columns.  
- Then, it asks the user for a column name or allows skipping by typing “No”.  
- If a valid column is entered, the program asks for a target data type: `int`, `float`, `str`, or `datetime`.  
- If invalid input is detected, the user is prompted again.  
- Failed conversions trigger a warning message.

---

### 4. Normalizing Text Capitalization
To standardize text values, another function capitalizes the **first letter of each word** and makes the rest lowercase.  
This helps prevent values like “dog” and “Dog” from being treated as different.

The program lists all columns and lets the user specify which ones to normalize.  
Typing “No” skips this step.  
If a non-text column is selected, an error message is displayed.

---

### 5. Removing Duplicates
The program first displays the name of each column along with the number of duplicate values it contains.  
Then, it asks for a specific column name to remove duplicates from.

If an invalid name is entered, it shows:  
**❌ “Column name does not exist.”**  
and asks again.  

Unlike global deduplication, this approach lets the user decide which column to clean—useful when repeated values in some columns are legitimate.  
This function is placed at the end to ensure duplicates caused by capitalization or spacing are properly handled.

---

### 6. Exporting the Cleaned File
Once all cleaning steps are complete, the DataFrame is exported back to a new CSV file.  
It keeps the original filename but adds the prefix **“cleaned_”**, for example:  
`cleaned_data.csv`.

---

##  Files Included

| File | Description |
|------|--------------|
| **project.py** | Main code and data cleaning functions |
| **test_project.py** | Unit tests implemented with `pytest` |
| **requirements.txt** | List of required Python libraries |
| **sample_data.csv** | Example dataset |
