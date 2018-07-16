#WAP to take a sentence from the user and print only words which are not in the EXCLUDED_LIST
sentence=(input('Enter the sentence:'))
w=['is','am','are','of','as','on','a']
sent_list=sentence.lower().split()
new_list=[]
for each in sent_list:
    if each not in w:
        new_list.append(each)
print(" ".join(new_list))
