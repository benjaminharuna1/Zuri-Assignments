# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

def find_anagram(word, anagram):
    # [assignment] Add your code here
    print("Checking Anagram")
    if(sorted(word)== sorted(anagram)):
        print(word, "=>", anagram )
        return True
    else:
        print(word, "=>", anagram )
        return False
word="hello"
anagram="check"

print(find_anagram(word,anagram))

word = "below"
anagram = "elbow"

print(find_anagram(word,anagram))