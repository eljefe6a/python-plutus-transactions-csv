import fitz
import pandas as pd
import re
import argparse
import os

# Set up command line argument parsing
def parse_args():
    parser = argparse.ArgumentParser(description='Extract transactions from a Plutus PDF statement')
    parser.add_argument('--pdf-path', help='Path to the PDF file')
    parser.add_argument('--output', '-o', default='transactions.csv',
                       help='Output CSV file path (default: transactions.csv)')
    return parser.parse_args()

def main():
    # Parse command line arguments
    args = parse_args()

    # Verify PDF file exists
    if not args.pdf_path:
        print("Error: --pdf-path argument is required")
        exit(1)
        
    if not os.path.exists(args.pdf_path):
        print(f"Error: File not found: {args.pdf_path}")
        exit(1)

    # Open the PDF file
    doc = fitz.open(args.pdf_path)

    # Initialize an empty list to store the extracted data
    transactions = []

    # Iterate over each page in the PDF
    for page in doc:
        # Extract the text from the page
        page_text = page.get_text()

        # Split the text into lines
        lines = page_text.splitlines()

        for i in range(len(lines)):
            line = lines[i]

            if line == "Transaction":
                # Extract the date and amount from the next two lines
                try:
                    date_str = lines[i + 1].strip()
                    amount_str = lines[i + 2].strip()
                    payee_str = lines[i + 3].strip()
                except IndexError:
                    break  # Reached the end of the page

                # Parse the date string
                date = pd.to_datetime(date_str, dayfirst=True).date()

                # Convert the amount string to a numeric value
                amount = float(re.sub("[^0-9.-]", "", amount_str))

                # Append the extracted data to the list
                transactions.append({"Date": date, "Payee": payee_str, "Amount": amount})

    # Create a pandas DataFrame from the extracted data
    df = pd.DataFrame(transactions)

    # Write the DataFrame to a CSV file
    df.to_csv(args.output, index=False)

if __name__ == '__main__':
    main()