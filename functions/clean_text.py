import re

def clean_text(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open('remove.txt', 'r', encoding='utf-8') as file:
        remove_lines = file.readlines()
        replace_rules = {}
        for line in remove_lines:
            if ':' in line:
                remove_str, replace_str = line.strip().split(':', 1)
                replace_rules[remove_str] = replace_str.strip()

    cleaned_lines = []
    for line in lines:
        if not line.strip() == '----':
            line = line.strip()
        is_dialog = line.lstrip().startswith('d')
        if is_dialog:
            line = re.sub(r'd\d{2}:\d{2}', '', line)
            for remove_str, replace_str in replace_rules.items():
                if remove_str in line:
                    line = line.replace(remove_str, replace_str + " ")
        else:
            line = re.sub(r'\b\d{2}:\d{2}\b', '', line)
            for remove_str in replace_rules:
                if remove_str in line:
                    line = line.replace(remove_str, '')
        line = ' '.join(line.split())
        if line.strip():
            cleaned_lines.append(line + '\n')

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(cleaned_lines)
        print(f'Cleaned text saved to {output_file_path}')