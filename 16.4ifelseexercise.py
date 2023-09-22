#ask marks if 80 above so a 70 above so b 60 above so c 50 above so d 50 below fail (add multiple conditions)
marks = int(input("Enter your marks: "))
if(marks >= 80 and marks <= 84):
    print("You Get Grade A")
elif(marks >= 85):
    print("You Get Grade A+")
elif(marks >= 70):
    print("You Get Grade B")
elif(marks >= 60):
    print("You Get Grade C")
elif(marks >= 50):
    print("You Get Grade D")
else:
    print("sorry to say but you are fail")