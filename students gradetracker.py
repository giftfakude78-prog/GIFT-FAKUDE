name=(input("Enter your name " ))
num=int(input("Enter your student number " ))
grades=int(input("Enter your grades : " ))
print(f"Hello  {name} Your grade is {grades}" )

if  grades< 30:
 
  print(f"Hello {name} your grade is low")
elif grades >= 50 :
 
 print(f"Hello {name} your grade is average ")

else:
 print(f"Excellent work, you passed your grades")
