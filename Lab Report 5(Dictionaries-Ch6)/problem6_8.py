pet_1={'kind':'parrot','owner':'sidrat'}
pet_2={'kind':'cat','owner':'amrin'}
pet_3={'kind':'dog','owner':'nabaneeta'}

pets=[pet_1,pet_2,pet_3]
for pet_info in pets:
    print(f"\nEverything I know about this pet: ")
    print(f"\nKind: {pet_info['kind'].title()} \nOwner: {pet_info['owner'].title()}")
