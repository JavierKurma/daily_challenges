"""
Write a function that receives two words (String) and returns
true or false (Bool) depending on whether they are anagrams or not.
- An anagram consists of forming a word by rearranging ALL
  the letters of another original word.
- It is NOT necessary to check whether both words exist.
- Two exactly identical words are not an anagram.

"""
def anagram(word_1,word_2):
    word_1=word_1.lower()
    word_2=word_2.lower()
    clean_1=""
    clean_2=""
    for c in word_1:
        if c.isalnum():
            clean_1+=c
    for c in word_2:
        if c.isalnum():
            clean_2+=c
    if len(clean_1)==len(clean_2):
        pass
    else:
        return False
anagram("Facundo....    aguirre...12312","abc")
