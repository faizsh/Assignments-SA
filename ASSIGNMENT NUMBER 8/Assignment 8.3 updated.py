#to print 3 maximum
D={'Maths':78,'Chem':76,'Phy':77,'Mech':67,'Java':72}
marks=list(D.values())
marks.sort()
print(marks)
Max1=marks[len(marks)-1]
Max2=marks[len(marks)-2]
Max3=marks[len(marks)-3]
print('The first number is',Max1)
print('The second number is',Max2)
print('The Third number is',Max3)


