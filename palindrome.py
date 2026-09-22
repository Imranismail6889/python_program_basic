text = input("Enter a word: ")

reverse = text[::-1]

if text.lower() == reverse.lower():
    print(text, "is a palindrome.")
else:
    print(text, "is not a palindrome.")
