# age=int(input("Enter your age:-"))
# if age>18:
#     print("You are eligible to Vote")
# else:
#     print("You are not eligible to Vote")
#
#
# num=int(input("Enter any number:-"))
# x=num%2
# if x==0:
#     print("EVEN")
# else:
#     print("ODD")
#
# num=int(input("Enter any number:-"))
# x=num%7
# if x==0:
#     print("IT IS DIVISIBLE BY 7")
# else:
#     print("IT IS NOT DIVISIBLE BY 7")
#
#
# num=int(input("Enter any number:-"))
# x=num%5
# if x==0:
#     print("HELLO")
# else:
#     print("BYE")
#
#
# unit=eval(input("Enter total electricity consumed:-"))
# if unit<=100:
#     print("you have to pay:-Rs",unit*0)
# if unit>100 and unit<200 :
#     print("you have to pay:-Rs", unit * 5)
# if unit>200:
#     print("you have to pay:-Rs",unit*100)
#
#
#
# day=int(input("Enter any number between 1 to 7:-"))
# if day==1:
#     print("Sunday")
# if day==2:
#     print("Monday")
# if day==3:
#     print("Tuesday")
# if day==4:
#     print("Wednesday")
# if day==5:
#     print("Thursday")
# if day==6:
#     print("Friday")
# if day==7:
#     print("Saturday")
# else:
#     print("Invalid input : Enter any number between 1 to 7")
#
# w="welcome to my home"
# s=len(w)
# print(s)
# for a in range(s-1,-1,-1):
#     print(w[a])
# for a in w:
#     print(a)
# for n in range(1,11):
#     print("2 *",n,"=",2*n)
#
#
# num=int(input("Enter any number:-"))
# for i in range(1,11):
#     print(num,"*",i,"=",num*i)
# q1
# movies = ["Jurassic World","Spider-man","Titanic","Avengers-Endgame","Avatar"]
# x=movies[-3:]
# print(x)
#
#
# h="I am Swagat Barik"
# print(h[0::2])
# # l=len(h)
# # print(l)
# print(h[0:10])
# print(h[-1::-2])
#
# y=chr(69)
# print(type(y),y)



India = ["Mumbai", "Delhi", "Kolkata", "Chennai", "Bangalore", "Hyderabad", "Ahmedabad", "Pune", "Jaipur", "Surat"]
USA = ["New York City", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"]
UK = ["London", "Manchester", "Birmingham", "Glasgow", "Edinburgh", "Liverpool", "Bristol", "Leeds", "Newcastle", "Cardiff"]

city1 = input("Enter the 1st city:-")
city2 = input("Enter the 2nd city:-")
if city1 in India and city2 in India:
    print('Both cities are in India')
elif city1 in USA and city2 in USA:
    print('Both cities are in USA')
elif city1 in UK and city2 in UK:
    print('Both cities are in UK')
else:
    print("They don't belong to same country")
