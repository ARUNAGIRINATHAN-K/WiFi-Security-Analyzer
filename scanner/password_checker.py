import string

def check_password_strength(password):
    """
    Checks the strength of the given WiFi password based on simple rules:
    - Length
    - Use of uppercase, lowercase, digits, and special characters
    """

    analysis = {}

    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    if length < 8:
        analysis['strength'] = "❌ Very Weak (Too short)"
    elif length < 12:
        if has_upper and has_lower and has_digit:
            analysis['strength'] = "⚠️ Moderate (Consider making it longer and adding special characters)"
        else:
            analysis['strength'] = "❌ Weak (Mix uppercase, lowercase, digits, and special characters)"
    else:
        if has_upper and has_lower and has_digit and has_special:
            analysis['strength'] = "✅ Strong"
        else:
            analysis['strength'] = "⚠️ Fair (Add more variety to make it stronger)"

    analysis['details'] = {
        'length': length,
        'has_uppercase': has_upper,
        'has_lowercase': has_lower,
        'has_digits': has_digit,
        'has_special_chars': has_special
    }

    return analysis
