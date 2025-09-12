# 🗂️🔍 Duplicate File Finder 
A simple Python script to find and list duplicate files in a folder based on their content hash (MD5). Helps you clean up storage by identifying exact duplicate files.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey)

## ✨ Features  
- 📁 Recursively scans the selected folder and its subdirectories.  
- 🔐 Uses MD5 hashing to compare the content of files.  
- 🧭 Detects duplicates even if the filenames or extensions are different.  
- 📄 Clearly lists duplicate files with their full paths.

## 📋 Requirements  
- 🐍 Python 3.x  
- ✅ No external dependencies (only uses built-in Python modules)

## 🚀 How To Use  
1. 🐍 Make sure you have Python installed (Python 3 recommended). Download it from [python.org](https://www.python.org/downloads/).  
2. 📥 Clone the repository  
```bash
git clone https://github.com/SltnBM/duplicate-file-finder.git
```
3. 📂 Navigate to the project directory
```bash
cd duplicate-file-finder
```
4. ▶️ Run the script using terminal or command prompt
```bash
python main.py
```

## ⚙️ How It Works
The script will prompt you to input the path to the folder you want to scan, then it will:
- Traverse all subdirectories
- Calculate MD5 hash for each file
- Group files with identical hashes
- Print out pairs or groups of duplicate files

🖥️ Example:
```bash
Enter folder path to scan: C:\Users\YourName\Documents

Duplicate files found:
C:\Users\YourName\Documents\file1.txt <==> C:\Users\YourName\Documents\backup\file1_copy.txt
C:\Users\YourName\Documents\image.jpg <==> C:\Users\YourName\Pictures\image_backup.jpg
```

## 📁 Folder Structure
```plaintext
📂 duplicate-file-finder/
├── 🐍 main.py
├── 📄 README.md
└── 📜 LICENSE
```

## 🤝 Contributing
Feel free to open issues or submit pull requests to improve this project.

## 📬 Connect With Me
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Sultan%20Badra-blue?logo=linkedin\&logoColor=white\&style=flat-square)](https://www.linkedin.com/in/sultan-badra)

## 📜 License
This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.
