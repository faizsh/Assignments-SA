#WAP to take a sentence as an input and take a word as an input. Calculate how many times the word has occured in the sentence
sentence=(input('enter the sentence'))
s=sentence.lower().split()
word=(input('Enter the word'))
w=word.lower()
if w in s:
    print('The number of times this word has occured in sentence is:',s.count(w))
else:
    print('Entered word is out of sentence')
