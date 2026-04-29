#message =input("Tell me something: and i will repeat it back to you")
#print(message)

#name=input("Please enter your name: ")
#print(f"\nHello, {name} ")
#age=input("Please enter your age: ")
#print(age)

#number=input("Enter a number . and I'll tell you if it's even or odd: ")
#number=int(number) #convert the input to integer, type casting
#if number%2==0:
 #   print(f"{number} is an even number")
#else:
 #   print(f"{number} is an odd number")

prompt="\Tell me something, and I will repeat it back to you : "
# prompt +="\nEnter 'quit' to end the program. "
message=" "
while message != 'quit' :
    message=input(prompt)
    print(message)

