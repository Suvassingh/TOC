def is_valid_date(date_str):
    if len(date_str) != 10:
        return False
    if date_str[2] != '/' or date_str[5] != '/':
        return False
    day = date_str[0:2]
    month = date_str[3:5]
    year = date_str[6:]
    return day.isdigit() and month.isdigit() and year.isdigit()
