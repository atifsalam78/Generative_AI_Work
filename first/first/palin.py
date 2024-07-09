def palindrome(text: str):
    if text == text[::-1]:
        return "Palindrome"
    else:
        return "Not Palindrome"
    
if __name__ == "__main__":

    text = input("Enter the text you want to check... ")
    result = palindrome(text)
    print(result)