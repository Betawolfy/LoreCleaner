# saveLore.py
# 
# * This function will allow to save the cleaned lore to a new file in a new directory.
#
# * 0. The program will ask the user if they want to save.
# * 1. Create a new directory with the actual date and time as name (exemple: 2021-09-01_13-45-00)
# * 2. Save the lore.txt file in this directory (the file will be named loreUncleared.txt)
# * 3. Save the cleaned lore in this directory (the file will be named loreCleared.txt)
# * 4. Print the path of the directory where the files are saved

# Importing the necessary libraries
import os
import shutil
from datetime import datetime

# Function to save the lore to a new directory
def save_lore():
    # Ask the user if they want to save the files
    save_files = input("Do you want to save the files? (yes/no): ")
    if save_files.lower() == "yes":
        # Get the current date and time
        now = datetime.now()
        date_time = now.strftime("%Y-%m-%d_%H-%M-%S")

        # Create a new directory with the current date and time as name
        directory_name = date_time
        os.mkdir(directory_name)

        # Save the lore.txt file in the new directory
        shutil.copy("lore.txt", f"{directory_name}/loreUncleared.txt")

        # Save the cleaned lore in the new directory
        shutil.copy("lore_cleaned.txt", f"{directory_name}/loreCleared.txt")

        # Print the path of the directory where the files are saved
        print(f"The files are saved in the directory: {directory_name}")
    else:
        print("The files are not saved.")