def keep_alnum(s):
    result = ''.join(ch for ch in s if ch.isalnum())
    return result

text = input("Enter a string: ")
print("After removing special characters:", keep_alnum(text))