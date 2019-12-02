import re
def longestWord(text):
    return max(re.split("\W+",text),key=len)

def longestWord(text):
    return max(re.findall(r'\w+', text),key=len)

def longestWord(text):
        return max(re.split("\W|_",text),key=len)
