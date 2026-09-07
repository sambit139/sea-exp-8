def reverse_string(text):
    return text[::-1]

def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

if __name__ == "__main__":
    message = "DevOps"
    print(f"Original: {message}")
    print(f"Reversed: {reverse_string(message)}")
    print(f"Is 'racecar' a palindrome?: {is_palindrome('racecar')}")
    print("hello for continuos integration")
