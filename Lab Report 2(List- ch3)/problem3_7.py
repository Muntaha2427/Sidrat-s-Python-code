guests=['amrin','nabaneeta','arian']

guests.insert(0,'sadia')
guests.insert(3,'ruhi')
guests.append('humaira')

print(f"Hi {guests[0].title()}, I will be happy if you come in my home for take dinner.")
print(f"Please {guests[1].title()}, join in my this special occasison at tonight's dinner.")
print(f"Hello... {guests[2].title()}, please accept my invitation.")
print(f"Hi {guests[3].title()}, I will be happy if you come in my home for take dinner.")
print(f"Please {guests[4].title()}, join in my this special occasison at tonight's dinner.")
print(f"Hello... {guests[5].title()}, please accept my invitation.")

print(f"\nSorry! I can now only invite two people for dinner..")

popped_names=guests.pop()
print(f"Sorry {popped_names.title()}, I can't invite you to dinner!!")

popped_names=guests.pop()
print(f"Sorry {popped_names.title()}, I can't invite you to dinner!!")

popped_names=guests.pop()
print(f"Sorry {popped_names.title()}, I can't invite you to dinner!!")

popped_names=guests.pop()
print(f"Sorry {popped_names.title()}, I can't invite you to dinner!!")

print(f"\n{guests[0].title()}, you are still invited..")
print(f"\n{guests[1].title()}, you are still invited..")

del guests[0]
del guests[0]
print(f"\nNow the guests list is : Empty",guests)
