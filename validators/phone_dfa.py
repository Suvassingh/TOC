def is_valid_phone(input_str):
    state = 0
    digits = 0
    for char in input_str:
        if char.isdigit():
            digits += 1
        elif char not in [' ', '-', '(', ')', '+']:
            return False
    return 10 <= digits <= 15 
# and (input_str.startswith('+') or input_str[0].isdigit())
