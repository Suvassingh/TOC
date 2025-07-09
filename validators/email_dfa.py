
def is_valid_email(input_str):
    state = 0
    for char in input_str:
        if state == 0:
            if char.isalpha() or char.isdigit():
                state = 1
            else:
                return False
        elif state == 1:
            if char.isalnum() or char in ['_', '.', '-', '+']:
                state = 1
            elif char == '@':
                state = 2
            else:
                return False
        elif state == 2:
            if char.isalpha():
                state = 3
            else:
                return False
        elif state == 3:
            if char.isalnum() or char == '-':
                state = 3
            elif char == '.':
                state = 4
            else:
                return False
        elif state == 4:
            if char.isalpha():
                state = 5
            else:
                return False
        elif state == 5:
            if char.isalpha():
                state = 5
            elif char == '.':
                state = 4  # Accept more domain levels like .edu.np
            else:
                return False
    return state == 5
