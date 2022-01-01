def duplicate_count(text):
    
    # Create dictionary of all lower-case characters and their counts
    char_count = {}
    for char in text:
        if char.lower() not in char_count.keys():
            char_count[char.lower()] = 1
        else:
            char_count[char.lower()] += 1
    
    # Find the count of characters that have been duplicated
    duplicate_count = 0
    for char, count in char_count.items():
        if count > 1:
            duplicate_count += 1
    
    return duplicate_count
     
