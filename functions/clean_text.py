# clean_text.py
#
# * This function will clean the text in the input file and save the cleaned text to the output file.
#
# * 0. read the lines from the input file.
# * 1. read the remove strings from the remove.txt file.
# * 2. clean the text contained in input by removing timestamps, remove strings, and extra whitespaces.
# * 3. save the cleaned text to the output file.
#
# * Note: The console will show all modifications made to the text.

import re

def clean_text(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('remove.txt', 'r', encoding='utf-8') as file:
        remove_lines = file.readlines()
        replace_rules = {}
        print("remove_lines: ", remove_lines)
        for line in remove_lines:
            if ':' in line:
                remove_str, replace_str = line.strip().split(':', 1)
                replace_rules[remove_str] = replace_str.strip()

    cleaned_lines = []
    for line in lines:
        print("--------------------")
        print("cleaning line: ", line)
        if not line.strip() == '----':
            line = line.strip()
        is_dialog = line.lstrip().startswith('d')
        if is_dialog:
            print("-> This is a dialog")
            line = re.sub(r'd\d{2}:\d{2}', '', line)
            print("-> Removing dialog IDs and timestamps")
            for remove_str, replace_str in replace_rules.items():
                if remove_str in line:
                    print(f"-> Removing {remove_str} and replacing with {replace_str}")
                    line = line.replace(remove_str, replace_str + " ")
        else:
            print("-> This is not a dialog")
            line = re.sub(r'\b\d{2}:\d{2}\b', '', line)
            print("-> Removing timestamps")
            for remove_str in replace_rules:
                if remove_str in line:
                    print(f"-> Removing {remove_str}")
                    line = line.replace(remove_str, '')
        line = ' '.join(line.split())
        if line.strip():
            cleaned_lines.append(line + '\n')

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)
        print('-' * 20)
        print(f'Cleaned text saved to {output_file_path}')