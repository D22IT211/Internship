import re

def assess_password_strength(password):
    
    # Initialize the strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[\W_]', password) is not None

    # Assess strength based on the criteria
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Provide feedback based on the number of criteria met
    if criteria_met == 5:
        return "Strong: Your password is very strong!"
    elif criteria_met == 4:
        return "Moderate: Your password is strong, but could be stronger."
    elif criteria_met == 3:
        return "Weak: Your password is somewhat strong, but could use improvement."
    else:
        return "Very Weak: Your password is too weak. Consider improving it."

def main():
    print("Password Strength Assessment Tool")
    password = input("Enter your password: ").strip()
    feedback = assess_password_strength(password)
    print(feedback)

if __name__ == "__main__":
    main()
