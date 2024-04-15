def check_password_strength(password):
    if len(password) < 8:
        return "Weak password: Too short (at least 8 characters required)."
    
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?`~" for char in password)

    complexity_score = sum([has_upper, has_lower, has_digit, has_special])

    if complexity_score < 3:
        return "Medium password: Lacks complexity (include uppercase, lowercase, digits, and special characters)."
    elif complexity_score == 3:
        return "Strong password: Good job with complexity!"
    else:
        return "Very strong password: Excellent complexity!"
