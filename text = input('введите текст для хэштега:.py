text = input('введите текст для хэштега: ')
words = text.split()
new_words = []
for word in words :
    new_words.append(word[0].upper()+ word[1:].lower())
print('#' + ''.join(new_words))
