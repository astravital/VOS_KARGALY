# VOS Kargaly Automation Project

## Project Overview

This is an automation project for a water treatment facility in the village of Kargaly near Almaty city, Kazakhstan.

## System Architecture

The system is based on two Simatic S7-300 controllers:

- **PLC_1**: Controls horizontal settling tanks and filters
- **PLC_2**: Controls the reagent workshop

## Project Structure

- `CURSOR_PROJECT/PLC_1/` - Configuration files for PLC_1 controller
- `CURSOR_PROJECT/PLC_2/` - Configuration files for PLC_2 controller (if exists)
- `CURSOR_PROJECT/examples/` - Example code and reference files. This codebase serves as the foundation on which changes will be made to the real project
- `TA_PORTAL_V20_PROJECT/` - TIA Portal V20 project files
- `scripts/` - Automation scripts for project management
- `docs/en/` - English documentation
- `docs/ru/` - Russian documentation (for user only)

## Documentation

- [Scripts Documentation](scripts.md) - Information about scripts and tools
- [Development Workflow](DEVELOPMENT_WORKFLOW.md) - Step-by-step workflow and processes used during development

