#prompt="Please enter the name of s city you have visited: "
#prompt +="\n(Enter 'quit' to end the program. )"

#while True:
    #city=input(prompt)
    #if city=='quit':
    ###    print(f"I'd love to go to {city.title()}!")

pets=['dog','cat','dog','goldfish','cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)