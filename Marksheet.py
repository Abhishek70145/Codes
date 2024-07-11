print("--------------","The entered marks should be less than 100!!!","--------------")

sub1=input("Enter first sub name=")
sub2=input("Enter secondsub name=")
sub3=input("Enter third sub name=")
sub4=input("Enter fourth sub name=")

mark1=int(input("Enter mark of first sub="))
mark2=int(input("Enter mark of second sub="))
mark3=int(input("Enter mark of third sub="))
mark4=int(input("Enter mark of fourth sub="))

sum=mark1+mark2+mark3+mark4
pe=(sum*100)/400

print("SUBJECT"," ","MARKS")
print(sub1," ",mark1)
print(sub2," ",mark2)
print(sub3," ",mark3)
print(sub4," ",mark4)

print(" ","Percentage=",pe,"%")

if pe>=90 and pe<=100:
    print("Your result is A+.\nExcellent!!!")
elif pe>=80 and pe<90:
    print("Your result is A.\nGood work..")
elif pe>=70 and pe<80:
    print("Your result is B+.\nIt's OK..")
elif pe>=60 and pe<70:
    print("Your result is B..\nTry to work harder next time0.")
elif pe>=50 and pe<60:
    print("Your result is C+..\nNeed more work!!!")
elif pe>=40 and pe<50:
    print("Your result id C..\nNeed more attention!!")
elif pe>=35 and pe<40:
    print("Your result is D.\nVery poor!!!!")
elif pe>=0 and pe<35:
    print("Your result is NG \nYou failed.Try next year.")
else:
    print("ERROR!!!!\nCheck again from beginning!!!")