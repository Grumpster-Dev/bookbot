def word_count(text):
    count = text.split()
    print(f"Found {len(count)} total words")

def char_count(text):
    text = text.lower()
    character_dict = {}
    for char in text:
        if char.isalpha():  # Count only alphabetic characters
            character_dict[char] = character_dict.get(char, 0) + 1
    
    return character_dict

def char_count_sorted(character_dict):
    character_list = []
    for char, count in character_dict.items():
        character_list.append((char, count))
    character_list.sort(reverse=True, key=lambda x: x[1])
    return character_list
