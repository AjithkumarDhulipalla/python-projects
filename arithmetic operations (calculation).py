a = float(input("\n enter the value"))
b = float(input("\n enter the value"))
print("enter the choice(1,2,3,4,5)\n1.addition\n2.subtraction\n3.multiplication\n4.division\n5.remainder")
choice=int(input())
if choice==1:
  print(f"addition of {a} and {b} is {a+b}")
elif choice==2:
  print(f"subtraction of {a} and {b} is {a-b}")
elif choice==3:
  print(f"multipication of {a} and {b} is {a*b}")
elif choice==4:
  print(f"divison of {a} and {b} is {a//b}")
elif choice==5:
  print(f"remainder of {a} and {b} is {a%b}")
else:
  print("enter a vaild choice")
  
  
  
