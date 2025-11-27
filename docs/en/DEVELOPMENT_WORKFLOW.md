# Development Workflow

This document describes the step-by-step workflow and processes used during the development of this project. It serves as a reference for future projects.

## Workflow Steps

### Initial Setup

1. Project structure creation
2. Documentation setup (English and Russian versions)
3. Git repository initialization

### Development Process

#### Data Extraction from TIA Portal

We extract data from the TIA Portal V20 project and save it to the `CURSOR_PROJECT/` folder. This allows us to work with the project data in Cursor IDE.

**Process:**

1. The TIA Portal V20 project files are stored in `TA_PORTAL_V20_PROJECT/` folder
2. Data is extracted from the TIA Portal project and saved as XML files in `CURSOR_PROJECT/`
3. The extracted data is organized by PLC controller:
   - `CURSOR_PROJECT/PLC_1/` - Configuration files for PLC_1 controller
   - `CURSOR_PROJECT/PLC_2/` - Configuration files for PLC_2 controller

**Extracted Data:**

- IO channel configurations (XML format)
- Station, rack, and module information
- Address mappings and tag names
- Separate files for each device (main PLC, slaves, MOV modules, etc.)

**File Structure:**

The extracted XML files contain structured data about:
- Stations (e.g., "S7-300/ET200M station_1")
- Racks and modules
- IO channels with addresses and tags

**Notes:**

- The `TA_PORTAL_V20_PROJECT/` folder is in `.gitignore` because it contains binary files
- The `CURSOR_PROJECT/` folder contains the extracted data in text format (XML)
- Extracted data can be processed and analyzed in Cursor IDE

#### Working with HMI Tags for WinCC Advanced V20

HMI tags are stored in Excel format with two sheets: `hmi_tags` and `multiplexing`. To work with these tags:

**Process:**

1. Extract Excel sheets to CSV format (done manually in Excel):
   - Save `hmi_tags` sheet as `Hmi Tags.csv` (CSV UTF-8, semicolon delimiter)
   - Save `multiplexing` sheet as `Multiplexing.csv` (CSV UTF-8, semicolon delimiter)

2. Edit CSV files:
   - CSV files are text-based and easy to edit
   - Can be edited in any text editor or spreadsheet program
   - Files are located in `CURSOR_PROJECT/examples/HMI_TAGS/`

3. Convert CSV back to Excel:
   - Use `scripts/hmi_tags_excel_converter.py` to convert CSV files back to Excel
   - The script creates an Excel file with both sheets: `hmi_tags` and `multiplexing`

4. Import to WinCC Advanced V20:
   - Use the Excel file to import tags into WinCC Advanced V20 project

**File Locations:**

- Excel file: `CURSOR_PROJECT/examples/HMI_TAGS/HMITags.xlsx`
- CSV files: `CURSOR_PROJECT/examples/HMI_TAGS/Hmi Tags.csv` and `Multiplexing.csv`

**Tools:**

- `scripts/hmi_tags_excel_converter.py` - Python script to convert between CSV and Excel formats
- Requires: Python 3.7+, pandas, openpyxl (see `requirements.txt`)

## Notes

- All documentation is written in English first
- Russian documentation is translated manually by the user
- Documentation uses simple language and common English words
- Code comments and variable names are in Russian
- Commits are made in English

## Action Log

| Date | Action | Description |
|---|---|---|
| 2025-11-23 | Documentation | Created documentation for `FB_MOV01.scl` including inputs, outputs, logic flow, and state diagrams. |
| 2025-11-23 | Bug Fix | Fixed typo in `FB_MOV01.md` input table formatting. |
| 2025-11-23 | Documentation | Clarified Limit Switch logic (NO vs NC) in `FB_MOV01.md`. |
| 2025-11-23 | Documentation | Corrected limit switch fault detection logic - both X21=1 & X22=1 triggers fault after 2s (T_ON01). Added GSL alarm flag. |
| 2025-11-23 | Documentation | Added truth table for limit switch states (X21/X22 combinations) in `FB_MOV01.md`. |
| 2025-11-23 | Git Commit | Committed and pushed PLC project structure: added source blocks, hardware structure, tags, and PLC_2 configuration (32 files, 8315 insertions). |
| 2025-01-XX | Documentation | Added note to `FB_MOV01.md` indicating that this function block is taken from the WKKUL_SB&SCADA project from the S7-400 controller (МНС Кульсары). |
| 2025-01-XX | Script | Created `hmi_tags_excel_converter.py` script to convert HMI tags between CSV and Excel formats for WinCC Advanced V20. |
| 2025-01-XX | Documentation | Added HMI tags workflow section to `DEVELOPMENT_WORKFLOW.md` and script documentation to `scripts.md`. |
