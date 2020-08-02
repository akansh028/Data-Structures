# anagram check = from same letters multiple different word formation

def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

print(anagram('dog','God'))