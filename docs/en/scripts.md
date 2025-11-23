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

