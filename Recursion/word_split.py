# split the words such that the element from the list
# is in the string

def word_split(phrase , words , output = None):

    if output is None:
        output = []
    
    for word in words:
        if phrase.startwith(word):
            output.append(word)
            return word_split(phrase[len(word):], words , output)
    
    return output

word_split('themanran', ['clown', 'man' , 'ran'])