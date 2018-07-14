#WAP to take 5 string from user and store in the list and show the greatest number
words=[]
for i in range(5):
    words.append(input('Enter the word'))
max_len=0
largest_word=""
for each in words:
    if(max_len<len(each)):
        max_len=len(each)
        largest_word=each
print('The largest word is:',largest_word)












'''l1=[]
l2=[]
l3=[]
l4=[]
l5=[]
for n in range(5):
    m=(input('Enter a word'))
    l1.append(n)
    l2.append(n)
    l3.append(n)
    l4.append(n)
    l5.append(n)
    print(l1)
    print(l2)
    print(l3)
    print(l4)
    print(l5)
    max1=len(l1)
    max2=len(l2)
    max3=len(l3)
    max4=len(l4)
    max5=len(l5)
    club=[max1,max2,max3,max4,max5]
    print(club)
print('The maximum character that string has:',max(club))'''
