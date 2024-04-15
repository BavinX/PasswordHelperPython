import re

def check_password_strength(password):
    # Define patterns for various strength levels
    patterns = {
        'weak': r'^.{1,5}$',
        'medium': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{6,10}$',
        'strong': r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{11,}$'
    }

    # Check the password against each pattern
    for strength, pattern in patterns.items():
        if re.match(pattern, password):
            return strength
    return 'very strong'

def main():
    password = input("Enter your password: ")
    strength = check_password_strength(password)
    
    # Emoji representations
    emoji = {
        'weak': '❌',
        'medium': '⚠️',
        'strong': '✅',
        'very strong': '💪'
    }
    
    print(f"Password strength: {strength.capitalize()} {emoji.get(strength, 'Unknown')}")

if __name__ == "__main__":
    main()