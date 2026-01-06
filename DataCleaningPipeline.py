import pandas as pd

class DataCleaner:
    # A class to perform data cleaning operations on a dataset.
    def __init__(self):
        pass

    # Functions
    def remove_duplicates(self, df):
        return df.drop_duplicates()

    def snake_case_columns(self, df):
        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
        )
        return df

    def convert_to_date(self, df, columns):
        for col in columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        return df

    def convert_dtypes_not_date(self, df, columns, dtype):
        for col in columns:
            try:
                df[col] = df[col].astype(dtype)
                print(f"Column '{col}' converted to {dtype}.")
            except Exception as e:
                print(f"Could not convert column '{col}' to {dtype}. Reason: {e}")
        return df

    # Join everything
    def clean_data(self, df):

        # 1. Convert to dates
        choice = input("Do you want to convert columns to dates? (y/n): ").strip().lower()
        if choice == "y":
            print("\nExisting columns:", list(df.columns))
            cols = input("Write the columns separated by commas: ")
            col_list = [c.strip() for c in cols.split(",")]
            df = self.convert_to_date(df, col_list)

        # 2. Convert to other dtypes
        choice = input("Do you want to convert columns to other data types than dates? (y/n): ").strip().lower()
        if choice == "y":
            print("\nExisting columns:", list(df.columns))
            raw = input("Write column:type pairs (e.g. age:int, price:float): ")

            pairs = [p.strip() for p in raw.split(",")]

            for pair in pairs:
                col, dtype = pair.split(":")
                col = col.strip()
                dtype = dtype.strip()
                df = self.convert_dtypes_not_date(df, [col], dtype)

        # 3. snake_case
        df = self.snake_case_columns(df)

        # 4. remove duplicates
        df = self.remove_duplicates(df)

        return df
