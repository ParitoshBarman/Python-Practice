sub1 = int(input("Enter 1st subject marks-->"))
sub2 = int(input("Enter 2nd subject marks-->"))
sub3 = int(input("Enter 3rd subject marks-->"))

if(sub1<33 or sub2<33 or sub3<33):
    print("You are fail beacause you have less then 33% in one of this subject")
elif(sub1+sub2+sub3)/3 < 40:
    print("You are fail due to total persentage lass then 40")
else:
    print("Congratulation! You passed the exam")