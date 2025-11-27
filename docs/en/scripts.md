# Scripts Documentation

This document describes the scripts available in the `scripts/` folder.

## update-tia-project.ps1

This script helps you update the TIA Portal V20 project on GitHub.

### What it does

The script adds the `TA_PORTAL_V20_PROJECT/` folder to Git and creates a commit. This folder contains binary files from TIA Portal V20. The folder is in `.gitignore` by default, so you need to use this script to update it on GitHub.

### How to use

Run the script from the project root:

```powershell
.\scripts\update-tia-project.ps1
```

You can also add your own commit message:

```powershell
.\scripts\update-tia-project.ps1 "Update TIA Portal project to latest version"
```

### What happens

1. The script goes to the project root folder
2. It adds the `TA_PORTAL_V20_PROJECT/` folder to Git (even though it is in `.gitignore`)
3. If there are changes, it creates a commit
4. You need to run `git push` to send changes to GitHub

### Notes

- The script only commits if there are changes
- The TIA Portal project folder is not tracked for changes in Git
- This script is used to keep the latest version on GitHub without tracking every change
- Binary files in this folder are large, so we do not track changes to save space

## hmi_tags_excel_converter.py

This script helps you work with HMI tags for WinCC Advanced V20. It can read CSV files, edit data, and write it back to Excel format.

### What it does

The script reads two CSV files:
- `Hmi Tags.csv` - Contains HMI tag definitions
- `Multiplexing.csv` - Contains multiplex tag mappings

It can convert these CSV files back to Excel format with two sheets:
- `hmi_tags` - HMI tag definitions
- `multiplexing` - Multiplex tag mappings

### Requirements

You need Python 3.7 or later and these libraries:
- pandas
- openpyxl

Install them with:
```powershell
pip install -r requirements.txt
```

### How to use

Read CSV files and show information:
```powershell
python scripts\hmi_tags_excel_converter.py --read-csv
```

Write CSV data to Excel file:
```powershell
python scripts\hmi_tags_excel_converter.py --write-excel
```

Do both (read and write):
```powershell
python scripts\hmi_tags_excel_converter.py --read-csv --write-excel
```

Or just run without arguments (does both by default):
```powershell
python scripts\hmi_tags_excel_converter.py
```

### File locations

The script works with files in:
- `CURSOR_PROJECT/examples/HMI_TAGS/Hmi Tags.csv`
- `CURSOR_PROJECT/examples/HMI_TAGS/Multiplexing.csv`
- `CURSOR_PROJECT/examples/HMI_TAGS/HMITags.xlsx`

### Notes

- CSV files use semicolon (;) as delimiter (standard for WinCC)
- The Excel file will have two sheets: `hmi_tags` and `multiplexing`
- You can edit CSV files in any text editor or spreadsheet program
- After editing CSV files, use `--write-excel` to update the Excel file
- The Excel file can be imported into WinCC Advanced V20

### Workflow

1. Extract Excel sheets to CSV (done manually in Excel)
2. Edit CSV files as needed
3. Run the script to convert CSV back to Excel
4. Import the Excel file into WinCC Advanced V20


