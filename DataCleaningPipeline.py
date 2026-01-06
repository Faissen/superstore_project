Class DataCleaner:
# A class to perform data cleaning operations on a dataset.
    def __init__(self):
    pass # Initialize any necessary attributes here.

#Functions
    def remove_duplicates(self,df):
        # Remove duplicate rows from the DataFrame.
        return df.drop_duplicates()

    def snake_case_columns(self,df):
        # Convert all columns names to snake_case.
        df.columns = (df.columns
                      .str.strip() # Remove spaces from the beginning and end
                      .str.lower() # Convert to lowercase
                      .str.replace(" ", "_") # Replace spaces with underscores
                      .str.replace("-", "_") # Replace hyphens with underscores
         ) 
        return df

    def convert_to_date(self, df, columns):
     # Convert date columns list to datetime format.
        for col in columns:
            df[col] = pd.to_datetime(df[col], errors='coerce')
        return df

    def convert_dtypes_not_date(self, df, columns, dtype):
     # Convert columns list to specified data type. Do not use datetime format - may lead to errors if the data
     #  is not in a date format.
        for col in columns:
            try:
                df[col] = df[col].astype(dtype, errors='ignore')
                print(f"Column '{col}' converted to {dtype}.")
            except Exception as e:
                print(f"Could not convert column '{col}' to {dtype}. Reason: {e}")
        return df

#Join everything
    def clean_data(self,df):
        # Perform all cleaning operations on the DataFrame.
        
        # 1. Ask user if they want to convert columns to dates
        choice = (input("Do you want to convert columns to dates? (y/n): ")
                  .strip() # Remove spaces from beginning and end
                  .lower() # Convert to lowercase
        ) 
        if choice == "y":
            # Ask user for columns to convert 
            print("\nExisting columns:", list(df.columns))
            cols = input("Write the columns separated by commas: ") 
            # Transformar string em lista 
            col_list = []
            for c in cols.split(","):
                col_list.append(c.strip())
            df = self.convert_to_date(df, col_list)

        # 2. Ask user if they want to convert columns to other data types rather than dates
        choice = (input("Do you want to convert columns data types to other data type than dates? (y/n): ")
                  .strip() # Remove spaces from beginning and end
                  .lower() # Convert to lowercase
        ) 
        if choice == "y":
            # Ask user for columns to convert 
            print("\nExisting columns:", list(df.columns))


            raw = input("Write column:type pairs (e.g. age:int, price:float): ")
            pairs = []
            for p in raw.split(","):
                pairs.append(p.strip())
            
            for pair in pairs: 
                col, dtype = pair.split(":") 
                col = col.strip() 
                dtype = dtype.strip() 
                df = self.convert_dtypes_not_date(df, [col], dtype)


        # 3. Transform columns to snake_case
        df = self.snake_case_columns(df)
        # 4. Remove duplicates
        df = self.remove_duplicates(df)
        return df # Return the cleaned DataFrame