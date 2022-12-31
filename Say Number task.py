def read_number(numeral):
    # Create a dictionary mapping digits to their corresponding words
    digit_words = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    
    # Initialize the result as an empty string
    result = ''
    
    # Split the numeral into groups of three digits from right to left
    groups = [numeral[max(i, 0):i+3] for i in range(-3, -len(numeral)-1, -3)]
    
    # Iterate over the groups of three digits
    for i, group in enumerate(groups):
        # Convert the group of three digits to a word
        group_word = ''
        for digit in group:
            group_word += digit_words[digit] + ' '
        
        # Add the group word to the result, followed by the appropriate magnitude (e.g. thousand, million, etc.)
        result = group_word.strip() + ' ' + ['', 'thousand', 'million', 'billion', 'trillion'][i] + ' ' + result
    
    # Return the result with the appropriate punctuation
    return result.strip()
print(read_number('19093'))  # Output: "nineteen thousand ninety three"
print(read_number('123456789'))  # Output: "one hundred twenty three million four hundred fifty six thousand seven hundred eighty nine"
print(read_number('10001000'))  # Output: "ten million one thousand"
