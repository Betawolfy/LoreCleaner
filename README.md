# Lore Cleaner
A simple Python script in order to clean text files containing RP logs.
## Authors / Contributors

[@betawolfy](https://www.github.com/Betawolfy)


## Features
- Removes time (format HH:MM).
- Removes and, optionnaly, replaces names in the cleared log.
- Removes empty lines.
- Keeps format and RP special character.



## Installation
```bash
git clone https://github.com/Betawolfy/LoreCleaner
cd lore-cleaner
```
    
## Usage/Examples
1. Place the lore.txt file in the same directory as this script
2. Add any strings that need to be removed to the remove.txt file
3. Optionnaly, add a footer in footer.txt
4. Run the script using ```python index.py```
5. The cleaned text will be saved to lore_cleaned.txt


## Setups
`lore.txt` - Lore uncleaned.

`remove.txt` - Specify all rules here.

`footer.txt` - Optionnal, display a custom text at the beginning of the output.

`lore_cleaned.txt` - The output, with all removed times, rules, etc..
## Mendatory format
- The correct format for `remove.txt` is:
  ```txt
  [String to delete]:Optionnal replacement string
  ```
- Story lines must be between [ Brackets ]
- Dialogues lines must begin by d (put a d before time)

#### Exemple: | File: lore.txt
```txt
10:00[{TFR} Adm. Betawolfy] [ This is a Story line]
d10:00[{TFR} Adm. Betawolfy] "This is a dialogue line"
```
## Roadmap
- Planning making it a website.
- Adding more rules.
## Feedback

If you have any feedback, please reach out to me by discord: `betawolfy`
