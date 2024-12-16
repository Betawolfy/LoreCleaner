# add_footer.py
#
# * This function will add a footer to the output file.
#
# * 0. The function will read the footer from the footer.txt file.
# * 1. The function will read the content of the output file.
# * 2. The function will write the footer at the beginning of the output file.

def add_footer(output_file_path):
    with open('footer.txt', 'r', encoding='utf-8') as file:
        footer = file.readlines()
    with open(output_file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.writelines(footer)
        file.writelines(lines)
        print(f'Footer added to {output_file_path}')