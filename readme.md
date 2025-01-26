# Plutus PDF Statement Extractor

This script extracts transactions from a Plutus PDF statement and saves them to a CSV file.

## Usage

```bash
python read_plutus.py --pdf-path <path-to-pdf-file> --output <output-csv-file>
```

## Getting PDF

1. Go to Plutus site and login.
1. Click on "Statements".
1. Make "All Time" is selected. You can delete the other dates if you want later once the CSV is created.
1. Click on "Download".
1. Run the script on the downloaded PDF.
