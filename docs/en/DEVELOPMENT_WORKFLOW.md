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

## Notes

- All documentation is written in English first
- Russian documentation is translated manually by the user
- Documentation uses simple language and common English words
- Code comments and variable names are in Russian
- Commits are made in English

