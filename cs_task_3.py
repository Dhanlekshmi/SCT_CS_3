import re

def check_password_strength(password):
   
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"\d", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

 
    errors = [length_error, uppercase_error, lowercase_error, digit_error, special_char_error]
    score = errors.count(False)  # count passed conditions

    
    if score == 5:
        strength = "Strong Password ✅"
    elif 3 <= score < 5:
        strength = "Moderate Password ⚠️"
    else:
        strength = "Weak Password ❌"

    return {
        "Password": password,
         "Strength": strength,
        "Length OK": not length_error,
        "Uppercase OK": not uppercase_error,
        "Lowercase OK": not lowercase_error,
        "Digit OK": not digit_error,
        "Special Char OK": not special_char_error,
       
    }


if __name__ == "__main__":
    pwd = input("Enter a password to check: ")
    result = check_password_strength(pwd)
    for key, value in result.items():
        print(f"{key}: {value}")
