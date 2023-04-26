#QUES1
tot=int(input("Enter your marks:-"))
if tot>90 :
    print("Your grade is A")
if tot>80 and tot <=90 :
    print("Your grade is B")
if tot>=60 and tot<=80:
    print("Your grade is C")
if tot<60 and tot>=35 :
    print("Your grade is D")
if tot<35 :
    print("FUCK YOU")

#sol2 tax=0 (in first line)why?
cost=int(input("Enter the price of Bike:-"))
if cost>100000:
    tax=15/100*cost
if cost>50000 and cost<=100000:
    tax = 10/100*cost
if cost<=50000 :
    tax = 5 / 100 * cost
print("Tax to be paid",tax)
#ques3
year=int(input("Enter the year:-"))
if year%4==0:
    print("It is a leap year")
else:
    print("It is not a leap year")
#ques4
day=int(input("Enter numbers between 1 to 7:-"))
if day==1:
    print("It is Sunday")
if day==2:
    print("It is Monday")
if day==3:
    print("It is Tuesday")
if day==4:
    print("It is Wednesday")
if day==5:
    print("It is Thursday")
if day==6:
    print("It is Fridayy")
if day==7:
    print("It is Saturday")
else:
    print("Please enter numbers between 1 to 7")
#ques5











