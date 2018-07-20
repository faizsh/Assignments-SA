#WAP To get Highest Three Value in a Dictionary
D,n={},0
D.setdefault(input('Enter the key:'),int(input('Enter the value:')))
D.setdefault(input('Enter the key:'),int(input('Enter the value:')))
D.setdefault(input('Enter the key:'),int(input('Enter the value:')))
D.setdefault(input('Enter the key:'),int(input('Enter the value:')))
marks=list(D.values())
marks.sort()
print(marks)
Max1=marks[len(marks)-1]
Max2=marks[len(marks)-2]
Max3=marks[len(marks)-3]
print('The first number is',Max1)
print('The second number is',Max2)
print('The Third number is',Max3)



