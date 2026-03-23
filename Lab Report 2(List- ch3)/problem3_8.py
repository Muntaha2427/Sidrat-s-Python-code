world_places=['sylhet','kashmir','meghalay','bandarban','chittagong']
print("Original list :")
print(world_places)

print(f"In Alphabetical order : {sorted(world_places)}")
print("Still Original list :")
print(world_places)

print(f"\nReverse in Alphabetical order :")
print(sorted(world_places,reverse=True))
print("Again Stil Original list :")
print(world_places)

world_places.reverse()
print(f"\nOrder changed : ")
print(world_places)

world_places.reverse()
print(f"\nBack to original Order:")
print(world_places)

world_places.sort()
print(f"In Alphabetical order :")
print(world_places)

world_places.sort(reverse=True)
print("Reverse alphabetical order:")
print(world_places)
