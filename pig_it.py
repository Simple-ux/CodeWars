# Move the first letter of each word to the end of it, then add "ay" to the end of the word. 
# Leave punctuation marks untouched.

# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !

def pig_it(text):
    splited = text.split()
    return " ".join([word[1:] + word[0] + "ay" if word[0].isalpha() else word[0]  for word in splited])

# Tests
assert pig_it('O tempora o mores !') == "Oay emporatay oay oresmay !"
assert pig_it('School is cool') == "choolSay siay oolcay"
assert pig_it('Over the rainbow bird is fly') == "verOay hetay ainbowray irdbay siay lyfay"