import math
import re

def calculate_entropy(password):
    charset = 0

    if re.search(r"[a-z]", password):
        charset += 26
    if re.search(r"[A-Z]", password):
        charset += 26
    if re.search(r"[0-9]", password):
        charset += 10
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        charset += 32

    if charset == 0:
        return 0

    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)


def password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add numbers.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add special characters.")

    return score, feedback


def crack_time(entropy):
    guesses_per_second = 1e9  # 1 billion guesses/sec
    seconds = (2 ** entropy) / guesses_per_second

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"


def analyze_password(password):
    entropy = calculate_entropy(password)
    score, feedback = password_strength(password)
    crack_estimation = crack_time(entropy)

    print("\n🔐 Password Analysis")
    print("-" * 30)
    print(f"Password length: {len(password)}")
    print(f"Entropy: {entropy} bits")
    print(f"Estimated crack time: {crack_estimation}")

    if score <= 2:
        print("Strength: ❌ Weak")
    elif score <= 4:
        print("Strength: ⚠️ Medium")
    else:
        print("Strength: ✅ Strong")

    if feedback:
        print("\nRecommendations:")
        for tip in feedback:
            print(f"- {tip}")


if __name__ == "__main__":
    pwd = input("Enter a password to analyze: ")
    analyze_password(pwd)
