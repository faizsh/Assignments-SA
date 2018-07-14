lst = []
total=0
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    lst.append(numbers)
    total=total+numbers
    avg=total/num
print("Maximum element in the list is :", max(lst), "\nMinimum element in the list is :", min(lst))
print('Avg of number is:',avg)
print('Total addition of the given numbers',total )
