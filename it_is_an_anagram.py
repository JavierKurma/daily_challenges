"""
Write a function that receives two words (String) and returns
true or false (Bool) depending on whether they are anagrams or not.
- An anagram consists of forming a word by rearranging ALL
  the letters of another original word.
- It is NOT necessary to check whether both words exist.
- Two exactly identical words are not an anagram.

"""
def anagram(word_1,word_2)->bool:
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
    if clean_1==clean_2:
        return False
    if not len(clean_1)==len(clean_2):
        return False
    for i in clean_1:
        if i not in clean_2:
            return False
        if not clean_1.count(i)==clean_2.count(i):
            return False
    return True
def init(op)->bool:
    if op=="n":
        return False
    else: return True
op=1
while init(op):
    print("Verifiying Anagram:")
    w_1=input("First one->")
    w_2=input("Second one->")
    if anagram(w_1,w_2):
        print("It is an anagram")
    else:
        print("Is not an anagram")
    op=input("Wish to continue? y/n: ")


    
