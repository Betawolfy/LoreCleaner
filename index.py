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

# Importing the required modules
# re module is used for regular expressions
import re

# Function to clean the text
# It takes the input file path and output file path as arguments
def clean_text(input_file_path, output_file_path):
    # Reading the input file
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Reading the remove.txt file to get the strings to remove and their replacements
    # Basic format of the rule: string_to_remove:replacement_string
    # * Note: you can add more rules to the remove.txt file as needed
    with open('remove.txt', 'r', encoding='utf-8') as file:
        remove_lines = file.readlines()
        replace_rules = {}
        for line in remove_lines:
            if ':' in line:
                remove_str, replace_str = line.strip().split(':', 1)
                replace_rules[remove_str] = replace_str.strip()

    # Cleaning the text
    # for each line in the input file, the following steps are performed:
    cleaned_lines = []
    for line in lines:
        # Removing leading/trailing whitespaces unless it's "----"
        if not line.strip() == '----':
            line = line.strip()
            
        # Check if the line is a dialogue line (starts with 'd')
        is_dialog = line.lstrip().startswith('d')
        
        # If it is a dialogue line:
        if is_dialog:
            # Remove timestamps for dialogue lines
            line = re.sub(r'd\d{2}:\d{2}', '', line)
            
            # For dialogue lines, apply the replace rules
            for remove_str, replace_str in replace_rules.items():
                if remove_str in line:
                    line = line.replace(remove_str, replace_str + " ")
        # If it is not a dialogue line (i.e., Lore story line):
        else:
            # Remove timestamps
            line = re.sub(r'\b\d{2}:\d{2}\b', '', line)
            
            # Removeing names
            for remove_str in replace_rules:
                if remove_str in line:
                    line = line.replace(remove_str, '')

        # Remove all spaces
        line = ' '.join(line.split())
    
        # Adding the cleaned line to the list
        if line.strip():
            cleaned_lines.append(line + '\n')

    # Saving the cleaned text to the output file
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)
        print(f'Cleaned text saved to {output_file_path}')

#Function to add the footer
#Optionally, you can add in footer.txt the name of the event, the date, and the name of the person who participated in the event
#It will put the footer at the beginning of the file
def add_footer(output_file_path):
    with open('footer.txt', 'r', encoding='utf-8') as file:
        footer = file.readlines()
    with open(output_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(footer)
        file.writelines(lines)
        print(f'Footer added to {output_file_path}')

# Main function
# The input file path and output file path are specified here
# The clean_text function is called with these arguments
if __name__ == "__main__":
    input_file_path = 'lore.txt'  # Chemin du fichier d'entrée
    output_file_path = 'lore_cleaned.txt'  # Chemin du fichier de sortie
    clean_text(input_file_path, output_file_path)
    add_footer(output_file_path)

# ----------------------------
# End of the script

# * Note: The script is designed to be simple and easy to use. It can be modified or extended as needed for specific requirements. For example, additional cleaning steps or processing can be added to the clean_text function. The script can also be integrated into a larger pipeline or workflow for text processing tasks.