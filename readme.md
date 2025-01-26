# Plutus PDF Statement Extractor

This script extracts transactions from a Plutus PDF statement and saves them to a CSV file.

## Usage

```bash
python read_plutus.py --pdf-path <path-to-pdf-file> --output <output-csv-file>
```

## Getting PDF

#. Go to Plutus site and login.
#. Click on "Statements".
#. Make "All Time" is selected. You can delete the other dates if you want later once the CSV is created.
#. Click on "Download".
#. Run the script on the downloaded PDF.