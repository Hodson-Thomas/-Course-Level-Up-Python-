def is_palindrome(string: str) -> bool:
    string = "".join([c for c in string if c.isalpha()])
    string = string.lower()
    return string == string[::-1]

if __name__ == "__main__":
    assert is_palindrome("Hello world") == False
    assert is_palindrome("level") == True
    assert is_palindrome("Go hang a salami - I'm a lasagna hog.") == True
