# Sentence Similarity
'''You are given two strings sentence1 and sentence2, each representing a sentence composed of words.
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.
Each word consists of only uppercase and lowercase English characters.

Two sentences s1 and s2 are considered similar if it is possible to insert
an arbitrary sentence (possibly empty) inside one of these sentences such
that the two sentences become equal.
Note that the inserted sentence must be separated from existing words by spaces.

For example,

s1 = "Hello Jane" and s2 = "Hello my name is Jane" can be made equal by
inserting "my name is" between "Hello" and "Jane" in s1.
s1 = "Frog cool" and s2 = "Frogs are cool" are not similar, since although
there is a sentence "s are" inserted into s1, it is not separated from
"Frog" by a space.Given two sentences sentence1 and sentence2, return true
if sentence1 and sentence2 are similar. Otherwise, return false.'''


def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # Split both sentences into words
        s1 = sentence1.split()
        s2 = sentence2.split()
    
        # If sentence1 is longer, swap them so that sentence1 is always the shorter one
        if len(s1) > len(s2):
            s1, s2 = s2, s1
    
        # Compare the common prefix
        i = 0
        while i < len(s1) and s1[i] == s2[i]:
            i += 1
    
        # Compare the common suffix
        j = len(s1) - 1
        k = len(s2) - 1
        while j >= i and s1[j] == s2[k]:
            j -= 1
            k -= 1
    
        # If all words in sentence1 have been matched in sentence2
        return j < i


        
