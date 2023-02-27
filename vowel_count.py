def get_count(sentence):

    return sum(c in 'aeiou' for c in sentence)

print(get_count('aeioujvfdfdgbfdbfdjj'))
