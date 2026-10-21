<div align="center">

# 🔓 PDF Unlocker & Renamer 🖋️

**A powerful Python script to batch decrypt, intelligently rename, and organize your password-protected PDF files automatically.**

</div>

<p align="center">
  <img alt="Python Version" src="https://img.shields.io/badge/python-3.x-blue.svg?style=for-the-badge&logo=python">
  <img alt="Dependencies" src="https://img.shields.io/badge/dependency-pypdf-brightgreen?style=for-the-badge">
  <img alt="License" src="https://img.shields.io/badge/license-MIT-purple?style=for-the-badge">
</p>

---
## 🚀 Key Features

-   **🤖 Fully Automated**: Just drop your files in a folder and run the script.
-   **📂 Smart Folder Management**: Automatically creates `locked_files` (input) and `processed_files` (output) folders on first run.
-   **🔑 Batch Decryption**: Unlocks multiple PDFs at once using a single, securely stored password.
-   **✍️ Intelligent Renaming**: Scans the first page of each PDF, finds a date range with Regex, and renames the file to a clean, standardized format.
-   **📝 Detailed Logging**: Creates and maintains a `log.txt` file, recording every successful operation and error with a timestamp.
-   **🔔 GUI Notifications**: Informs you with a pop-up message when the entire process is complete.

## 📋 Prerequisites

-   **Python 3.x**
-   The **pypdf** library

## 🛠️ Installation & Setup

Follow these steps to get the script up and running.

**1. Install the `pypdf` Library**
Open your terminal or command prompt and run the following command:
```bash
pip install poetry
```
```bash
poetry install
```
*(Note: This script uses the modern `pypdf` library. You do not need the older `PyPDF2` library).*

**2. Configure Your Password**
For security, the script loads the password from a separate, untracked file.

-   In the same directory as `main.py`, create a new file named `cred.py`.
-   Open it and add your password inside a string variable:

    ```python
    # cred.py
    password = "YOUR_SUPER_SECRET_PASSWORD_HERE"
    ```

> **Security Warning!** 🔒
> If you are using Git for version control, add `cred.py` to your `.gitignore` file immediately. This will prevent you from accidentally committing your password to a public repository.
> ```
> # .gitignore
> cred.py
> venv/
> __pycache__/
> ```

## ⚙️ How to Use

1.  **Place Your Files**: Drop all your locked PDFs into the `locked_files` folder. (The script will create this folder for you if it doesn't exist).
2.  **Run the Script**: Execute the main file from your terminal.
    ```bash
    python main.py
    ```
3.  **Check the Output**: A notification will appear once the process is finished. Your unlocked and renamed PDFs will be waiting for you in the `processed_files` folder!

## 🧩 How the Renaming Works

The script is configured to find a specific date range pattern on the **first page** of each PDF.

| Step                 | Description                                    | Example                               |
| -------------------- | ---------------------------------------------- | ------------------------------------- |
| **1. Find Pattern**  | Locates text matching `DD/MM/YYYY--DD/MM/YYYY` | `21/10/2026--25/10/2026`              |
| **2. Clean & Format**| Replaces slashes with dots and dashes with spaces | `21.10.2026 - 25.10.2026`             |
| **3. Save File**     | Saves the PDF with the new name.               | `21.10.2026 - 25.10.2026.pdf`         |

> **Note:** If a PDF is a scanned image (not text-selectable) or does not contain this exact date format, the script will log an error for that file and skip it.

## 💡 Troubleshooting

-   **`ImportError: cannot import name 'password' from 'decrypt'`**
    This is the most common error. It means you either forgot to create the `decrypt.py` file, or you accidentally installed a conflicting library with `pip install decrypt`.
    **Solution**: Run `pip uninstall decrypt` and then ensure your local `decrypt.py` file is created correctly as described in the setup guide.

-   **Files Fail to Decrypt**
    Check `log.txt` for `FileNotDecryptedError`. This means the password in your `decrypt.py` file is incorrect for those specific PDFs.

---
<div align="center">
Made with ❤️ and Python
</div>