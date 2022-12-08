#100 days python bootcamp
#3rd ay
#Leap year

year = int(input("which year you want to check ? "))
if year % 4 == 0:
    if year % 100 == 0:
        print ("not leap year")
        if year % 400 == 0:
            print("leap year")
        else:
           print("not leap year")
    else:
       print("leap year")

else:
   print("not leap year")
