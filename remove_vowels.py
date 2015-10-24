text = raw_input("Input your phrase:")
vowel = ('A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u')
def anti_vowel (text):
    empty = ""
    for letter in text:
        if letter not in vowel:
                empty += letter
    return empty
anti_vowel(text)