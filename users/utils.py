import csv
from io import TextIOWrapper

def validate_csv_file(file):
    """
    Make sure that the file upload is csv by checking its extension is '.csv'
    """
    if not file:
        raise ValueError("File not found")
    if not file.name.endswith(".csv"):
        raise ValueError("Only CSV files are allowed")
    
def parse_csv(file):
    """
    Parse the CSV file and return the list of rows as dicts
    """
    try:
        decoded_file = TextIOWrapper(file.file,encoding="utf-8")
        reader = csv.DictReader(decoded_file)
        
        rows = []
        
        for row_number, row in enumerate(reader, start=1):
            cleaned_row = {key.strip(): value.strip() for key, value in row.items()}
            rows.append((row_number, cleaned_row))
            
        if not rows:
            raise ValueError("CSV file is empty")
        return rows
    
    except Exception as e:
        raise ValueError(f"Error parsing CSV: {str(e)}")
    