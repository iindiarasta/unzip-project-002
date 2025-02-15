This Python script automates the extraction and organization of compressed files from the user's Downloads folder. It performs the following tasks:

Finds the Latest ZIP File: Identifies the most recently modified .zip file in the Downloads folder.

Extracts the ZIP File: Extracts the contents of the identified ZIP file to a specified destination folder (Documents/extracted_pys).

Extracts GZIP Files: Recursively searches for .gz or .gzip files within the extracted folder and decompresses them. Files containing "XMLPAIN" in their names are renamed with a .xml extension.

Organizes Old Files: Moves previously extracted files and folders to an old subfolder within the destination directory, resolving naming conflicts by appending a random suffix if necessary.

Logs Actions: Prints status messages to the console for each step.

Key Features:
Automated Extraction: Handles both .zip and .gz/.gzip files.

File Organization: Keeps the destination folder clean by moving old files to an old subfolder.

Error Handling: Provides feedback if extraction fails for any file.

Usage:
Place the script in a convenient location.

Run the script using Python 3.

The script will automatically process the latest .zip file in the Downloads folder and organize the extracted files.

Dependencies:
Python 3.x

Standard libraries: os, zipfile, gzip, shutil, random, pathlib

