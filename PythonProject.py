print(" Calculating the grade of a student")
Bangla=int(62)
English=int(74)
Mathematics=int(92)
Social_Science=int(77)
Religion=int(83)
Physics=int(66)
Chemistry=int(87)
Higher_Math=int(83)
Total=Bangla+English+Mathematics+Social_Science+Religion+Physics+Chemistry+Higher_Math
Average=Total/8
if Average >=80 and Average <= 100:     
    print("The student obtained GPA 5.00 = A+")
elif Average >=70  and Average <= 79:
    print("The student obtained GPA 4.00 = A") 
elif Average >= 60  and Average <= 69:
    print("The Studenr obtained GPA 3.50 = A-") 
elif  Average >= 50 and Average <= 59:
    print("The student obtained GPA 3.00 = B")  
elif Average >= 40 and Average <= 49:
    print("The student obtained GPA 2.00 = C")   
elif Average >= 33 and Average <= 39:
    print("The student obtained GPA 1.00 = D") 
elif Average >= 0 and Average <= 32:
    print("The Student failed = F")  

print("END")                          
