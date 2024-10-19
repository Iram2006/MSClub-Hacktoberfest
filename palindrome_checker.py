import re

def is_palindrome(s):
    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    normalized = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return normalized == normalized[::-1]

if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    print(f'"{word}" is a palindrome: {is_palindrome(word)}')
