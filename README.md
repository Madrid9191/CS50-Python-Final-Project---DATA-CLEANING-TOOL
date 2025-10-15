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
For this reason, a function was added to remove unnecessary spaces. This operation is automatic and shows progress messages. 
To achieve this, the data type of every column is converted to text (astype(str)), allowing the .str.strip() method to be applied safely. 
This also removes spaces from numeric or date values such as ' 42 ' or ' 2024-10-01 '.

---

### 3. Converting Column Data Types
Because stripping spaces changes column data types—and inconsistent formatting is common—a function was added to convert the data type of specific columns.

-First, the function displays the current data types of all columns so that the user can identify which ones need to be converted.
-Then, it asks the user to enter the name of a column or type “No” to skip the step. 
-If a valid column name is provided, the program prompts for a target data type and shows the available options: int, float, str, and datetime. 
-If the user enters a non-existent column or invalid data type, an error message is displayed, and the input is requested again. 
-If the conversion fails, a warning message is shown.

---

### 4. Normalizing Text Capitalization
To standardize text values, a function was included that capitalizes the first letter of each word and makes the rest lowercase. 
This helps prevent values like “dog” and “Dog” from being treated as different due to case differences. 
The program lists all column names and asks the user to specify one or several columns to apply this normalization. 
If the user doesn’t wish to perform this step, they can simply type “No.” 
If an invalid or non-text column is selected, the program displays an error message and asks again.

---

### 5. Removing Duplicates
To remove duplicates, the program first displays the name of each column along with the number of duplicate values it contains. 
Then, it asks the user to enter the name of a column from which to delete duplicate rows or type "No" to skip this step. 

If an invalid name is entered the message **"❌ Column name does not exist.”** is shown, and the input is requested again. 

It was intentionally designed to let users choose a specific column rather than remove all duplicates globally, since in some cases, repeated values in certain columns are not errors. 
This function was placed at the end to ensure that no duplicates caused by capitalization or spacing issues remain undetected.

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
