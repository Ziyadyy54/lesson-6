year =int(input("enter the year to find out if its a leap year "))
if(year%400==0)or(year%4==0 and year%100!=0):
    print("leap year")
else:
    print("not a leap year")