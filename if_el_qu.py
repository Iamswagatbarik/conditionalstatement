#https://csiplearninghub.com/python-if-else-conditional-statement-practice/  ques link
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
    print("Invalid input: Please enter numbers between 1 to 7")
#ques5
per=int(input("Enter your age:-"))
if per>=18 :
    print("You are eligible to vote")
else :
    print("You are not eligible to vote")

#ques6
num=int(input("Enter the number:-"))
if num%2==0 :
    print("Even number")
else :
    print("Odd number")
#efficient way
num = int(input("Enter the number:-"))
r=num%2
if r == 0:
    print("Even number")
if r == 1:
    print("Odd number")

#ques7
num=int(input("Enter the number:-"))
if num%7==0 :
    print("Divisible by 7")
else :
    print("Not divisible by 7")
#ques8
num=int(input("Enter the number:-"))
if num%5==0 :
    print("Hello")
else :
    print("Bye")
#ques9
price=0
unit=eval(input("Enter total unit:-"))
if unit<=100 :
    price=unit*0
if unit>100 and unit<=200 :
    price= unit*5
if unit>200 :
    price = unit*10
print("Total amount to pay:",price)
#ques10
num=int(input("Enter the number:-"))
print("The lat digit is:-",num%10)
#ques11
num=int(input("Enter any number:-"))
id=num%10
if id%3==0:
    print("The number is divisible by 3")
else:
    print("The number is not divisible by 3")
#ques12
mnt=int(input("Enter any number between 1 to 12:-"))
year=0
if mnt==1:
    print("January-Number of days is 31")
if mnt == 2:
    input("Enter the year:-")
    if year%4==0:
        print("It is a leap year-Number of days is 29")
    else:
        print("It is not a leap year-Number of days is 28")
if mnt==3:
    print("March-Number of days is 31")
if mnt==4:
    print("April-Number of days is 30")
if mnt==5:
    print("May-Number of days is 31")
if mnt==6:
    print("June-Number of days is 30")
if mnt==7:
    print("July-Number of days is 31")
if mnt==8:
    print("August-Number of days is 31")
if mnt==9:
    print("September-Number of days is 30")
if mnt==10:
    print("October-Number of days is 31")
if mnt==11:
    print("November-Number of days is 30")
if mnt==12:
    print("December-Number of days is 31")
if mnt>12:
    print("Invalid input : Enter any number between 1 to 12")
#ques13
city=str(input("Enter the city:-"))
if city.lower()=="delhi":
    print("The best monument to visit is Red fort")
if city.lower()=="agra":
    print("The best monument to visit is Taj mahal")
if city.lower() == "jaipur":
    print("The best monument to visit is Jal mahal")
#ques14
