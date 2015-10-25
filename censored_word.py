text = input("Enter what you want")
word = input("Enter what you want 2")
def censor(text, word):
    asterisk = len(word)
    if word in text:
            cens_text = text.replace(word, asterisk * "*")
    return (cens_text)