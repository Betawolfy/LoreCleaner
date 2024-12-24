# * Lore cleaner
# * By: @betawolfy
# * Version: 1.1

# * Made for TFR

# * This script is used to clean the lore.txt file
# * It removes timestamps, removes all strings contained in the remove.txt file, removes all non-alphanumeric characters, removes extra whitespaces, and removes leading/trailing whitespaces.
# * The cleaned text is saved to lore_cleaned.txt

# * Usage:
# * 1. Place the lore.txt file in the same directory as this script
# * 2. Add any strings that need to be removed to the remove.txt file
# * 3. Run the script using ```python index.py```
# * 4. The cleaned text will be saved to lore_cleaned.txt

# * Note: The remove.txt file contains strings that are removed from the text. You can add more strings to this file if needed.
# * Normally, you don't need to modify the script. Just add the lore.txt file and run the script.

# ----------------------------

Intro = """
Lore Cleaner
* By: @betawolfy
* Version: 1.1
* Made for TFR

Before running the script:
1. Place the your lore in the lore.txt file (make sure your respect the format of rules.)
2. Add any strings that need to be removed to the remove.txt file
3. Follow the instructions in the console if needed.
"""

# ----------------------------

# import functions
from functions.clean_text import clean_text
from functions.add_footer import add_footer
from functions.saveLore import save_lore
from functions.reconizeDialog import recognize_dialogs
from functions.compareNames import compare_names

# ----------------------------

# Input and output file paths
input_file_path = 'lore.txt'  # Chemin du fichier d'entrée
uncleared_file_path = 'lore_uncleared.txt'  # Chemin du fichier de sortie
output_file_path = 'lore_cleaned.txt'  # Chemin du fichier de sortie

remove_path = 'remove.txt' # Chemin du fichier des règles de suppression
# ----------------------------

# Main function
# The input file path and output file path are specified here
# The clean_text function is called with these arguments
if __name__ == "__main__":
    print(Intro)

    print("--------------------")
    input("Press Enter to continue...")
    print("Cleaning lore.txt file...")
    

    # Is broken. My bad, team!
    # compare_names(input_file_path, remove_path)
    
    print("--------------------")
    print("Sorting Dialogues and actions...")
    recognize_dialogs(input_file_path, uncleared_file_path)
    input("Normally, Dialogues and actions are sorted... Press Enter to continue...")

    print("--------------------")
    print("Cleaning the text...")
    clean_text(uncleared_file_path, output_file_path)

    print("--------------------")
    print("Adding the footer...")
    add_footer(output_file_path)

    print("--------------------")
    save_lore()

    print("--------------------")
    input("Press Enter to exit...")

# ----------------------------
# End of the script

# * Note: The script is designed to be simple and easy to use. It can be modified or extended as needed for specific requirements. For example, additional cleaning steps or processing can be added to the clean_text function. The script can also be integrated into a larger pipeline or workflow for text processing tasks.