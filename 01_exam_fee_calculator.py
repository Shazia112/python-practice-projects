# Write a program to sum the fees submitted by students and exit if user press q.
sum = 0
while(True):
    user_input = input("Enter fees submitted by students: \n")
   
    if(user_input!= 'q'):
         sum= sum + int(user_input)
         print(f"The fees submitted so far: {sum}")
    else:
         print("No more submission")
         break
