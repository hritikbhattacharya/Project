import logging
import pandas as pd
from datetime import datetime
from dateutil.parser import parse

# Setup logging
logging.basicConfig(
    filename='customer_split.log',
    level=logging.INFO,
    format='Time : %(asctime)s || Type:%(levelname)s || Msg:%(message)s'
)

# Constants
FILE_PATH = "people-1000.csv"  # Path to the uploaded CSV file


def split_csv(file_path, dob_cutoff):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Convert 'Data of Birth' column to datetime
        df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors='coerce')
        
        # Parse the user-provided DoB cutoff date
        dob_cutoff = parse(dob_cutoff)
        
        # Split the data into two data frames based on the cutoff date
        below_cutoff = df[df['Date of birth'] < dob_cutoff]
        above_cutoff = df[df['Date of birth'] >= dob_cutoff]
        
        # Save the resulting data frames to new CSV files
        below_cutoff.to_csv('customers_below_cutoff.csv', index=False)
        above_cutoff.to_csv('customers_above_cutoff.csv', index=False)
        
        logging.info("Successfully split the CSV file based on Date of Birth.")
    except Exception as e:
        logging.error(f"Error processing {file_path}: {e}")
        raise

def main():
    try:
        # Prompt user for DoB cutoff
        dob_cutoff = input("Enter the date of birth cutoff : ")
        
        # Split the CSV file
        split_csv(FILE_PATH, dob_cutoff)
        
        logging.info("Program completed successfully.")
    except Exception as e:
        logging.error(f"Program failed: {e}")

if __name__ == "__main__":
    main()
