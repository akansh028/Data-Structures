# reverse the words with spaces

def rev_word(s):

    words = []
    length = len(s)
    space = [' ']

    i = 0
    while i < length:
        if s[i] not in space:
            start = i           # start of the word index
            while i < length and s[i] not in space:
                i += 1              # end of the word index
            words.append(s[start:i])    # clipping of the word
        i += 1
    
    return ' '.join(reversed(words))

print(rev_word('   Hello john   how are you  '))

