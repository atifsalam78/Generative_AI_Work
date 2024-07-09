from first.palin import palindrome

def test_palindrome_t1():
    assert palindrome("racecar") == "Palindrome"

def test_palindrome_t2():
    assert palindrome("Mother") == "Not Palindrome"

def test_palindrome_t3():
    assert palindrome("rotator") == "Palindrome"