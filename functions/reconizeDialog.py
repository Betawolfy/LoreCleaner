def recognize_dialogs(input_file, uncleared_file_path):
    dialog_count = 0
    action_count = 0
    
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        
    processed_lines = [] 
    
    for line in lines:
        line = line.strip()
        
        if not line:
            continue
            
        # Check number of square bracket pairs and quotes 
        bracket_pairs = min(line.count('['), line.count(']'))
            
        # Line with brackets and quotes = dialogue
        if bracket_pairs >= 1 and '"' in line:
            if not line.startswith('d'):
                line = 'd' + line
            processed_lines.append(line)
            dialog_count += 1
            
        # Line with brackets but no quotes = action    
        elif bracket_pairs >= 1:
            processed_lines.append(line)
            action_count += 1
            
        else:
            print(f"Unclear line: {line}")
            answer = input("Is this a dialogue (d) or action (a)? ")
            if answer.lower() == 'd':
                if not line.startswith('d'):
                    line = 'd' + line
                processed_lines.append(line)
                dialog_count += 1
            elif answer.lower() == 'a':
                processed_lines.append(line)
                action_count += 1
                
    with open(uncleared_file_path, 'w', encoding='utf-8') as file:
        for line in processed_lines:
            file.write(line + '\n')
            
    print(f"Recognized {dialog_count} dialogues and {action_count} actions")
    return dialog_count, action_count