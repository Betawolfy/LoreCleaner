# compareNames.py
#
# * This simple script is comparing names in remove.txt and lore.txt files.
#
# * 0. Read the names from the remove.txt file.
# * 1. Read the names from the lore.txt file.
# * 2. Compare the names. If a name in remove.txt isn't in lore.txt, print it as a input.
# * 3. If a name in lore.txt isn't in remove.txt, print it as a input.

def compare_names(input_file_path, remove_path):
    # 0. Lire les noms depuis remove.txt
    with open(remove_path, 'r', encoding='utf-8') as file:
        remove_names = []
        for line in file:
            if ':' in line:
                name = line.split(':')[0].strip()
                remove_names.append(name)
    
    # 1. Lire les noms depuis lore.txt
    with open(input_file_path, 'r', encoding='utf-8') as file:
        lore_content = file.read()
        lore_names = []
        # Chercher les motifs comme [NomDuPersonnage] 
        import re
        pattern = r'\[(.*?)\]'
        matches = re.findall(pattern, lore_content)
        for match in matches:
            if match.strip():
                lore_names.append(match.strip())

    # 2. Comparer les noms
    missing_in_lore = set(remove_names) - set(lore_names)
    missing_in_remove = set(lore_names) - set(remove_names)

    # 3. Afficher les résultats
    if missing_in_lore:
        print("Noms dans remove.txt mais pas dans lore.txt:")
        for name in missing_in_lore:
            action = input(f"'{name}' n'est pas dans lore.txt. Que souhaitez-vous faire ? (garder/supprimer): ")
            if action.lower() == 'supprimer':
                remove_names.remove(name)

    if missing_in_remove:
        print("\nNoms dans lore.txt mais pas dans remove.txt:")
        for name in missing_in_remove:
            action = input(f"'{name}' n'est pas dans remove.txt. Voulez-vous l'ajouter ? (oui/non): ")
            if action.lower() == 'oui':
                replacement = input(f"Entrez le texte de remplacement pour '{name}': ")
                with open(remove_path, 'a', encoding='utf-8') as file:
                    file.write(f"\n{name}:{replacement}")

    return remove_names, list(missing_in_remove)