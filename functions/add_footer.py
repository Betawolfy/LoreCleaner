def add_footer(output_file_path):
    with open('footer.txt', 'r', encoding='utf-8') as file:
        footer = file.readlines()
    with open(output_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(footer)
        file.writelines(lines)
        print(f'Footer added to {output_file_path}')