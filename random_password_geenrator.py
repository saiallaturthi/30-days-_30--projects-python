import random
import string

def generate_password(length=12, use_digits=True, use_symbols=True):
    characters = list(string.ascii_letters)

    if use_digits:
        characters += list(string.digits)

    if use_symbols:
        characters += list(string.punctuation)

    if length < 4:
        raise ValueError("Password length should be at least 4")

    password = ''.join(random.sample(characters, length))
    return password

if __name__ == "__main__":
    print("🔐 Password Generator")

    try:
        length = int(input("Enter password length: "))
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        pwd = generate_password(length, use_digits, use_symbols)
        print(f"\n✅ Your generated password: {pwd}")
    except Exception as e:
        print(f"❌ Error: {e}")
