#WAP to combine two dictionary by adding common keys.
D,D1,D2={},{},{}
D1.setdefault(input('Enter the key for D1:'),int(input('Enter the value for d1:')))
D1.setdefault(input('Enter the key for D1:'),int(input('Enter the value for d1:')))
D1.setdefault(input('Enter the key for D1:'),int(input('Enter the value for d1:')))
D1.setdefault(input('Enter the key for D1:'),int(input('Enter the value for d1:')))
D2.setdefault(input('Enter the key for D2:'),int(input('Enter the value for d2:')))
D2.setdefault(input('Enter the key for D2:'),int(input('Enter the value for d2:')))
D2.setdefault(input('Enter the key for D2:'),int(input('Enter the value for d2:')))
D2.setdefault(input('Enter the key for D2:'),int(input('Enter the value for d2:')))
for each in D1.keys():
    if each in D2.keys():
        D.setdefault(each,D1[each]+D2[each])
    else:
        D.setdefault(each,D1[each])
for each in D2.keys():
    if each not in D:
        D.setdefault(each,D2[each])
print(D)
