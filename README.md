# File Organizer - JPG Automation

## 1. Project Description

This project is a simple Python automation program developed for the CodeAlpha Python Programming Internship - Task 3.

The program automatically finds JPG and JPEG image files from a source folder and moves them into a separate destination folder.

This project demonstrates basic file automation using Python.

## 2. Features

- Automatically checks files in a folder.
- Detects `.jpg` and `.jpeg` image files.
- Creates the destination folder automatically.
- Moves image files to the destination folder.
- Counts the number of files moved.
- Displays the result in the terminal.

## 3. Technologies Used

- Python
- VS Code
- `os` module
- `shutil` module

## 4. Project Structure

```text
CodeAlpha_TaskAutomation/
│
├── automation.py
├── README.md
├── test_files/
│   └── Test JPG/JPEG images
│
└── jpg_files/
    └── Moved JPG/JPEG images
```
## 5. How It Works

The program checks the `test_files` folder.

It reads all files using the `os` module.

It checks whether each file has a `.jpg` or `.jpeg` extension.

It creates the `jpg_files` folder if it does not already exist.

It moves the image files using the `shutil` module.

It displays the number of files moved.

## 6. How to Run

Open the project folder in VS Code.

Run the following command in the terminal:

```bash
python automation.py
```
## 7. Sample Output

```text
Moved: photo1.jpg.jpeg
Moved: photo2.jpg.jpeg
Moved: photo3.jpg.jpeg

File organization completed!
Total JPG files moved: 3
```
## 8. Concepts Learned

- File handling
- Folder management
- `os.listdir()`
- `os.path`
- `os.makedirs()`
- `shutil.move()`
- Loops
- Conditional statements
- String methods
- Basic automation

## 9. Project Objective

The objective of this project is to automate the process of organizing image files into a separate folder instead of moving them manually.

## 10. Internship Task

**Internship:** CodeAlpha Python Programming Internship

**Task:** Task 3 - Automation

**Project:** File Organizer - Move JPG/JPEG Files

## 11. Author

**Shravya**

## 12. Conclusion

This project demonstrates how Python can be used to automate simple file management tasks. It helped improve my understanding of Python modules, file handling, folder management, and automation.
