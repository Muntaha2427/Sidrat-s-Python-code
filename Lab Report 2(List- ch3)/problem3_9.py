guests=['amrin','nabaneeta','arian']

guests.insert(0,'sadia')
guests.insert(3,'ruhi')
guests.append('humaira')

#print(f"Hi {guests[0].title()}, I will be happy if you come in my home for take dinner.")
#print(f"Please {guests[1].title()}, join in my this special occasison at tonight's dinner.")
#print(f"Hello... {guests[2].title()}, please accept my invitation.")
#print(f"Hi {guests[3].title()}, I will be happy if you come in my home for take dinner.")
#print(f"Please {guests[4].title()}, join in my this special occasison at tonight's dinner.")
#print(f"Hello... {guests[5].title()}, please accept my invitation.")

total_inviting_people = len(guests)
print(f"Total guests = {total_inviting_people}")