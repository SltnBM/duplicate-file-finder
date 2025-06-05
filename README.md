# File Duplicate Detector
A simple Python script to find and list duplicate files in a folder based on their content hash (MD5). Helps you clean up storage by identifying exact duplicate files.

## Features  
- Recursively scans the selected folder and its subdirectories.  
- Uses MD5 hashing to compare the content of files.  
- Detects duplicates even if the filenames or extensions are different.  
- Clearly lists duplicate files with their full paths.

## How To Use  
1. Make sure you have Python installed (Python 3 recommended). Download it from [python.org](https://www.python.org/downloads/).  
2. Clone the repository  
```bash
git clone https://github.com/SltnBM/duplicate-file-finder.git
```
3. Navigate to the project directory
```bash
cd file-duplicate-detector
```
4. Run the script using terminal or command prompt
```bash
python file_duplicate_detector.py
```