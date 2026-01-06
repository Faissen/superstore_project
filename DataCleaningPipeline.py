Class DataCleaner:
# A class to perform data cleaning operations on a dataset.
    def __init__(self):
    pass # Initialize any necessary attributes here.

#Functions
    def remove_duplicates(self,df):
        # Remove duplicate rows from the DataFrame.
        return df.drop_duplicates()

    def snake_case_columns(self,df):
        # Convert all column names to snake_case.
        for col in df.columns:
            df.col = (df.col
                      .str.strip() # Remove spaces from the beginning and end
                      .str.lower() # Convert to lowercase
                      .str.replace([" ","-"], "_") # Replace spaces and hyphens with underscores
        return df

#Join everything
    def clean_data(self,df):
        # Perform all cleaning operations on the DataFrame.
        df = self.remove_duplicates(df)
        df = self.snake_case_columns(df)
        return df # Return the cleaned DataFrame