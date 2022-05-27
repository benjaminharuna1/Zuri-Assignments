from msilib.schema import ControlEvent
import re


### my favoutite life saver but a bit hard to learn and comprehend sometimes

# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    file = open(filename,'r')
    contents = file.read()
    file.close()
    print(contents)
    return contents

def count_words(contents):
    
#     # [assignment] Add your code here
    dict_words={}
    # words = re.sub(r'[^\w\s]','',words) 
#     #### to strip all punctuations
    words = contents.strip().split(' ')
    for word in  words:
        counts = re.findall(r'{0}'.format(word), contents)
        dict_words[word]= len(counts)
    return dict_words

print(count_words(read_file_content('story.txt')))
file_content = read_file_content('story.txt') 
# ## ensure the story.txt file is in the same directory as this python file.

output = count_words(file_content)
print(output)
 