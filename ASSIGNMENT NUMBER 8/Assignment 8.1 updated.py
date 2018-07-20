#to print maximum and smallest value
D={'Maths':78,'Chem':76,'Phy':77,'Mech':67,'Java':72}
marks=list(D.values())
marks.sort()
print(marks)
Max=marks[len(marks)-1]
Min=marks[0]
print('smallest number is:',Min)
print('Largest number is:',Max)
