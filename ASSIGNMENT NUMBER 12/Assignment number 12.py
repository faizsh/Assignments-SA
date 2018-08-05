'''
Emp_data.txt
Empid,Name,B_sal,Exp,Contact_no
101,John,5000,2.5,99998899
102,Henry,6000,3,88674321
103,Dexter,7000,4,88674321

bonus
b.s       exp
<=2000     1   2% 
2001-5000  <=3 5%
5001-7000  <=5 7%
7000>      Any 10%

(Create Emp_Sal.txt)
Empid,B.Sal,Bonus,   Total
101,5000,  5%ofB.Sal ,B.Sal+Bonus
102,6000,  7%%ofB.Sal,B.Sal+Bonus
103,7000,  7%%ofB.Sal,B.Sal+Bonus'''


fo=open("\\Users\Faiz Shaikh\Documents\Emp-data.txt","r")
fa=open("\\Users\Faiz Shaikh\Documents\Emp-salary.txt","a")
all_data=fo.read()
print(all_data)

each_line=all_data.split("\n");
print(each_line)

for each in each_line:
    each_ent=each.split(",")
    print(each_ent)
    if len(each_ent)>1:
        sal=int(each_ent[2])
        exp=float(each_ent[3])
        if sal<=2000 and exp<=1:
            bonus=0.02*sal
        elif sal>=2001 and sal<=5000 and exp<=3:
            bonus=0.05*100
        elif sal>=5001 and sal<=7000 and exp<=5:
            bonus=0.07*sal
        else:
            bonus=0.1*sal
        print(bonus)
        total_sal=sal+bonus
        print(total_sal)
        output=each_ent[0]+','+str(sal)+','+str(bonus)+','+str(total_sal)+'\n'
        print(output)
        fa.write(output)
fa.close()
fo.close()
