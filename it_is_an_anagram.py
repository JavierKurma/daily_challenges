"""
Write a function that receives two words (String) and returns
true or false (Bool) depending on whether they are anagrams or not.
- An anagram consists of forming a word by rearranging ALL
  the letters of another original word.
- It is NOT necessary to check whether both words exist.
- Two exactly identical words are not an anagram.

"""
def anagram(word_1,word_2)->bool:

    if len(word_1)==len(word_2):
        word_1=word_1.lower()
        
