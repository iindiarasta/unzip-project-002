# Automated ZIP and GZIP File Extractor

A Python script that automatically finds and extracts the latest ZIP file from your Downloads folder and handles nested GZIP files.

## Features

- 🔍 Automatically finds the most recently downloaded ZIP file
- 📂 Creates organized extraction directories
- 📤 Extracts ZIP files with nested structure
- 🗜️ Handles GZIP (.gz, .gzip) files automatically
- 🔄 Moves previous extractions to an "old" folder
- 🎯 Special handling for XMLPAIN files

## Requirements

- Python 3.6+
- Standard library modules:
  - `os`
  - `zipfile`
  - `gzip`
  - `shutil`
  - `pathlib`

## Installation

1. Clone or download this repository
2. No additional dependencies needed - uses Python standard library only

## Usage

```python
# Simply run the script
python unzip-script.py
```

The script will:
1. Move any existing extracted folders to "old" directory
2. Find the latest ZIP file in your Downloads folder
3. Extract it to Documents/extracted_pys/extracted_[zipname]
4. Process any GZIP files found in the extraction

## Default Paths

- Source: `~/Downloads`
- Destination: `~/Documents/extracted_pys`

## Functions

- `find_latest_zip(folder)`: Locates most recent ZIP file
- `extract_zip(zip_path, dest_folder)`: Extracts ZIP contents
- `extract_gz_files(folder)`: Processes GZIP files
- `oldify_files(destination_folder)`: Archives previous extractions

## License

MIT License

## Author

Your Name