mountains=['sylhet','bandarban','azad kashmir','meghalay','rangamati','everest']
print(mountains)
#accessing elements
print("Accessing :")
print(mountains[1].title())
#modifying
print("Modifying :")
mountains[0]='chittagong'
print(mountains)
#append
print("Appending :")
mountains.append('bhatiary')
print(mountains)
#insert()
print("Inserting:")
mountains.insert(3,'khagrachori')
print(mountains)
#del
print("Deleting:")
del mountains[4]
print(mountains)
#pop()
print("Delete by pop:")
mountains.pop()
print(mountains)
#remove()
print("Removing :")
mountains.remove('everest')
print(mountains)
#sorted
print("Sorted:")
print(sorted(mountains))
#reverse
print("Reverse:")
mountains.reverse()
print(mountains)
#sort
print("Sorting:")
mountains.sort()
print(mountains)
#len
print("Total length:")
print(len(mountains))