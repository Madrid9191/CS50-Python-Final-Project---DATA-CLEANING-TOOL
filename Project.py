import pandas as pd
import os

def data_cleaner():
    while True:
        filename = input("Input csv: ").strip()

        if not filename.endswith(".csv"):
            print("❌ The file must have a '.csv' extension.\n")
            continue
        if not os.path.exists(filename):
            print("❌ File not found. Please check the name and try again.\n")
            continue
        try:
            df = pd.read_csv(filename)
            print("✅ File uploaded successfully.\n")
            break
        except Exception as e:
            print(f"⚠️ Error reading the CSV file: {e}\n")
            continue

    df = handle_missing(df)
    df = strip_spaces(df)
    df = convert_dtypes(df)
    df = capitalize_text(df)
    df = remove_duplicates(df)

    output = "cleaned_" + filename
    df.to_csv(output, index=False)
    print(f"✅ Clean file exported as {output}")


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:

    print("Missing values per column:")
    print(df.isnull().sum(), "\n")
    print("Handling missing values...", "\n")

    df = df.dropna()

    print("Missing values per column after cleaning:")

    print(df.isnull().sum(), "\n")

    print("✅ Missing values deleted.\n")
    return df

def strip_spaces(df: pd.DataFrame) -> pd.DataFrame:

    print("Stripping spaces in text columns...")

    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()

    print("✅ Spaces stripped.\n")
    return df

def convert_dtypes(df: pd.DataFrame) -> pd.DataFrame:

    print("Data types:")
    print(df.dtypes, "\n")

    while True:
        col = input("Enter the column you want to convert (or type 'No' to stop): ").strip()
        if col.lower() == "no":
            print("✅ Finished converting dtypes.\n")
            break
        if col not in df.columns:
            print("❌ Column name does not exist.\n")
            continue

        dtype = input("Enter the target dtype (int, float, str, datetime): ").strip().lower()

        try:
            if dtype == "int":
                df[col] = pd.to_numeric(df[col], errors="coerce").astype("Int64")
            elif dtype == "float":
                df[col] = pd.to_numeric(df[col], errors="coerce").astype(float)
            elif dtype == "str":
                df[col] = df[col].astype(str)
            elif dtype == "datetime":
                df[col] = pd.to_datetime(df[col], errors="coerce")
            else:
                print("⚠️ Invalid dtype option.\n")
                continue
            print(f"Column '{col}' converted to {dtype}.\n")
        except Exception as e:
            print(f"⚠️ Could not convert column '{col}': {e}\n")
    return df

def capitalize_text(df: pd.DataFrame) -> pd.DataFrame:

    print("Columns:")
    print(df.columns.tolist(), "\n")

    while True:
        cols = input("Enter column(s) to capitalize (comma separated, or 'No' to stop): ").strip()
        if cols.lower() == "no":
            print("✅ Finished capitalizing text.\n")
            break

        col_list = [c.strip() for c in cols.split(",")]
        for col in col_list:
            if col not in df.columns:
                print(f"❌ Column '{col}' does not exist.\n")
                continue

            if df[col].dtype == "object":
                df[col] = df[col].apply(lambda x: str(x).title() if isinstance(x, str) else x)
                print(f"✅ Column '{col}' text capitalized successfully.\n")
            else:
                print(f"⚠️ Column '{col}' is not text-based.\n")
    return df

def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    print("Duplicate values per column")
    for col in df.columns:
        n_dups = df[col].duplicated().sum()
        print(f"{col}: {n_dups}")

    while True:
        col = input("Enter the column name to delete duplicates (or type 'No' to stop): ").strip()

        if col.lower() == "no":
            break
        if col not in df.columns:
            print("❌ Column name does not exist.\n")
        else:
            df = df.drop_duplicates(subset=[col])
            print("✅ Duplicates were deleted.\n")
    return df

if __name__ == "__main__":
    data_cleaner()

