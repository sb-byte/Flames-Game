def flames_game(name1, name2):
    name1, name2 = name1.replace(" ", "").lower(), name2.replace(" ", "").lower()
    
    # Remove common characters
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    
    # Count remaining characters
    count = len(name1) + len(name2)
    
    # FLAMES logic
    flames = ["F", "L", "A", "M", "E", "S"]
    while len(flames) > 1:
        index = (count % len(flames)) - 1
        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames.pop()
    
    # Relationship mapping
    result = {
        "F": "Friendship",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Sibling"
    }
    
    return result[flames[0]]

if __name__ == "__main__":
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")
    print("The relationship is:", flames_game(name1, name2))
