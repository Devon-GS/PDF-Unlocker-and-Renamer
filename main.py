import os
import logging
import datetime
import re
from os import path
from tkinter import messagebox
from PyPDF2 import PdfReader
from pypdf import PdfReader, PdfWriter, errors
from cred import PASSWORD	#python file with the password for bundling

def current_time():
    return datetime.datetime.now().strftime('%d.%m.%Y %H.%M.%S')

# Start logging
logger = logging.getLogger('PDF Unlocker')
logging.basicConfig(filename="log.txt", level=logging.INFO)

# Create folders
locked_files_folder = path.exists('locked_files')
processed_files = path.exists('processed_files')

if locked_files_folder == False:
    os.mkdir('locked_files')
    logger.info(f"[{current_time()}] 'locked_files' folder Created!")
if processed_files == False:
    os.mkdir('processed_files')
    logger.info(f"[{current_time()}] 'processed_files' folder Created!")

# Get list of files
file_list = os.listdir('locked_files')

#############################################################################
# DECRYPT PDF FILES AND RENAME THEM
#############################################################################

# Decrypt PDF
error_counter = 0

for filename in file_list:
    try:
        logger.info(f'[{current_time()}] Processing file "{filename}"')

        file = f'locked_files/{filename}'
        output_path = 'processed_files/'
        
        # Open files with reader
        reader = PdfReader(file)
        writer = PdfWriter()
        
        # Check if encrypted
        if reader.is_encrypted:
            reader.decrypt(str(PASSWORD))

        # Add all pages to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Get page one from pdf
        page_one_text = writer.pages[0].extract_text()
        
        # Repalce all spaces with '-' to get rid of special character
        x = page_one_text.encode("ascii", "ignore")
        y = x.decode()
        new_data = y.replace(' ','-')
        
        # Match regex to date and replace '-' with '.'
        match = re.findall(r"\d{2}\/\d{2}\/\d{4}--\d{2}\/\d{2}\/\d{4}", new_data)
        new_file_name = match[0].replace('--',' - ').replace('/','.')

        # Save decrypted file with new name in ouput folder
        with open(f"{output_path}{new_file_name}.pdf", "wb") as f:
            writer.write(f)
    except errors.FileNotDecryptedError:
        error_counter += 1
        logger.error(f'[{current_time()}] ERROR Processing file "{filename}"')  

# Show message when program ended
if error_counter > 0:
    messagebox.showinfo(title='Unlocker Complete With Errors ', message='ERROR Processing files. Please check log file')
    messagebox.showinfo(title='Unlocker Complete', message='Unlocker Has Completed')
else:
    messagebox.showinfo(title='Unlocker Complete', message='Unlocker Has Completed')