marks = int(input("Enter your marks-->"))

if marks>=90:
    great = "Ex"
elif marks>=80:
    great = "A"    
elif marks>=70:
    great = "B"
elif marks>=60:
    great = "C"   
elif marks>=50:
    great = "D"
elif marks<50:
    great = "F"       

print("Your great is "+ great)