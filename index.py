# * Lore cleaner
# * By: @betawolfy
# * Version: 1.0

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


# import functions
from functions.clean_text import clean_text
from functions.add_footer import add_footer
from functions.saveLore import save_lore

# Input and output file paths
input_file_path = 'lore.txt'  # Chemin du fichier d'entrée
output_file_path = 'lore_cleaned.txt'  # Chemin du fichier de sortie

# Clean the text and add footer
clean_text(input_file_path, output_file_path)
add_footer(output_file_path)

# Main function
# The input file path and output file path are specified here
# The clean_text function is called with these arguments
if __name__ == "__main__":
    print("Cleaning lore.txt file...")
    input_file_path = 'lore.txt'  # Chemin du fichier d'entrée
    output_file_path = 'lore_cleaned.txt'  # Chemin du fichier de sortie
    clean_text(input_file_path, output_file_path)
    add_footer(output_file_path)
    save_lore()
    input("Press Enter to exit...")

# ----------------------------
# End of the script

# * Note: The script is designed to be simple and easy to use. It can be modified or extended as needed for specific requirements. For example, additional cleaning steps or processing can be added to the clean_text function. The script can also be integrated into a larger pipeline or workflow for text processing tasks.