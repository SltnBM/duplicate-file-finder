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

## Setup
When prompted, enter the folder path you want to scan for duplicate files.

Example input:
```bash
Enter folder path to scan: C:\Users\YourName\Documents
```

## Example Output
Output example if duplicates found:
```bash
Duplicate files found:
C:\Users\YourName\Documents\file1.txt <==> C:\Users\YourName\Documents\backup\file1_copy.txt
C:\Users\YourName\Documents\image.jpg <==> C:\Users\YourName\Pictures\image_backup.jpg
```

## Contributing
Feel free to open issues or submit pull requests to improve this project.

## License
This project is open-source and free to use.